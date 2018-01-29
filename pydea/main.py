from twitter_searcher import TwitterSearcher,write_list_to_file
def main():
    searcher = TwitterSearcher()
    write_list_to_file(searcher.simple_search(1), 'test.txt')


if __name__ == "__main__":
    main()
