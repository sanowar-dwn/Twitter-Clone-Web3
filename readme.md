# TwitterClone Smart Contract

The TwitterClone smart contract is a simple Ethereum-based contract that allows users to create tweets, like tweets, and unlike tweets. It is designed to replicate some of the basic features of a Twitter-like social platform.

## Features

1. **Create Tweet**: Users can create tweets with a content string. The content must not be empty, and the tweet's timestamp is automatically recorded.

2. **Like Tweet**: Users can like tweets created by others. You cannot like your own tweet, and you cannot like the same tweet multiple times.

3. **Unlike Tweet**: Users can unlike a tweet they previously liked.

4. **Get Tweet Information**: You can retrieve information about a tweet, including the author's address, content, timestamp, and the number of likes it has received.

## Structs

- `Tweet`: A struct representing a tweet with the following properties:
  - `author`: The Ethereum address of the tweet's author.
  - `content`: The content of the tweet.
  - `timestamp`: The timestamp when the tweet was created.
  - `likers`: An array of Ethereum addresses of users who have liked the tweet.

## Events

- `TweetCreated`: Triggered when a new tweet is created. It records the author's address, tweet content, and the creation timestamp.

- `TweetLiked`: Triggered when a tweet is liked. It records the index of the liked tweet and the address of the liker.

- `TweetUnliked`: Triggered when a tweet is unliked. It records the index of the unliked tweet and the address of the unliker.

## Functions

- `createTweet(string memory _content)`: Allows users to create a new tweet. The tweet content must not be empty.

- `likeTweet(uint256 _index)`: Allows users to like a tweet by its index.

- `unlikeTweet(uint256 _index)`: Allows users to unlike a previously liked tweet by its index.

- `hasLikedTweet(uint256 _index, address _liker)`: Checks if a specific user has liked a tweet.

- `getTweetsCount()`: Returns the total number of tweets.

- `getTweet(uint256 _index)`: Retrieves the details of a tweet by its index, including author, content, timestamp, and the number of likes.

## Usage

You can interact with this smart contract through Ethereum-compatible wallets or by deploying it to the Ethereum blockchain. To get started, you can compile and deploy the contract using a development environment like Remix or Truffle.

## License

This smart contract is provided under the MIT License.

For more information, please see the [License](LICENSE.md) file.

## Author

- [Your Name]

Feel free to make any necessary adjustments and include your author information as appropriate. This documentation provides a clear and informative overview of your contract's features and usage, making it easier for others to understand and use your contract when it's hosted on your GitHub repository.
