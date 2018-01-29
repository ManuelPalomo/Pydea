from twitterSearcher import TwitterSearcher, write_list_to_file


def main():
    twitter_searcher = TwitterSearcher()
    write_list_to_file(twitter_searcher.simple_search(1), 'test.txt')

if __name__ == "__main__":
    main()
