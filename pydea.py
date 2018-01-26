from TwitterSearcher import TwitterSearcher

def main():
    twitter_searcher = TwitterSearcher()
    write_list_to_file(twitter_searcher.simple_search(), 'test.txt')   

if __name__ == "__main__":
    main()