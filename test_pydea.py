from twitterSearcher import TwitterSearcher
from tweet import Tweet



def main():
    twitter_searcher = TwitterSearcher()
    tweet_list = twitter_searcher.simple_search(1)
    
    retrieved_tweet= tweet_list[0]

    user = retrieved_tweet.user.name
    text = retrieved_tweet.text
    timestamp = retrieved_tweet.created_at


    tweet = Tweet()
    tweet.initialize_from_tweet(user, text, timestamp)
    print(str(tweet))


if __name__ == "__main__":
    main()
