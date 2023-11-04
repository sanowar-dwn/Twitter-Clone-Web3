// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TwitterClone {
    struct Tweet {
        address author;         // Address of the tweet author
        string content;        // Content of the tweet
        uint256 timestamp;      // Timestamp when the tweet was created
        address[] likers;       // List of users who liked the tweet
    }

    Tweet[] public tweets;      // Array to store tweets

    event TweetCreated(address indexed author, string content, uint256 timestamp);
    event TweetLiked(uint256 indexed tweetIndex, address indexed liker);
    event TweetUnliked(uint256 indexed tweetIndex, address indexed unliker);

    function createTweet(string memory _content) external {
        require(bytes(_content).length > 0, "Tweet content can't be empty");

        // Create a new tweet and push it to the tweets array
        tweets.push(Tweet(msg.sender, _content, block.timestamp, new address[](0)));

        // Emit a TweetCreated event to notify that a new tweet was created
        emit TweetCreated(msg.sender, _content, block.timestamp);
    }

    function likeTweet(uint256 _index) external {
        require(_index < tweets.length, "Tweet index out of bounds");

        Tweet storage tweet = tweets[_index];

        require(tweet.author != address(0), "Tweet does not exist");
        require(tweet.author != msg.sender, "Cannot like your own tweet");
        require(!hasLikedTweet(_index, msg.sender), "You have already liked this tweet");

        // Add the liker's address to the list of likers
        tweet.likers.push(msg.sender);

        // Emit a TweetLiked event to notify that a tweet was liked
        emit TweetLiked(_index, msg.sender);
    }

    function unlikeTweet(uint256 _index) external {
        require(_index < tweets.length, "Tweet index out of bounds");

        Tweet storage tweet = tweets[_index];

        require(tweet.author != address(0), "Tweet does not exist");
        require(hasLikedTweet(_index, msg.sender), "You haven't liked this tweet");

        // Remove the unliker's address from the list of likers
        for (uint256 i = 0; i < tweet.likers.length; i++) {
            if (tweet.likers[i] == msg.sender) {
                tweet.likers[i] = tweet.likers[tweet.likers.length - 1];
                tweet.likers.pop();
                break;
            }
        }

        // Emit a TweetUnliked event to notify that a tweet was unliked
        emit TweetUnliked(_index, msg.sender);
    }

    function hasLikedTweet(uint256 _index, address _liker) public view returns (bool) {
        require(_index < tweets.length, "Tweet index out of bounds");

        Tweet storage tweet = tweets[_index];

        // Check if the liker's address exists in the list of likers
        for (uint256 i = 0; i < tweet.likers.length; i++) {
            if (tweet.likers[i] == _liker) {
                return true;
            }
        }

        return false;
    }

    function getTweetsCount() external view returns (uint256) {
        return tweets.length;  // Return the total number of tweets
    }

    function getTweet(uint256 _index) external view returns (address, string memory, uint256, uint256) {
        require(_index < tweets.length, "Tweet index out of bounds");

        Tweet storage tweet = tweets[_index];

        // Return tweet information including author, content, timestamp, and the number of likes
        return (tweet.author, tweet.content, tweet.timestamp, uint256(tweet.likers.length));
    }
}
