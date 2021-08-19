# from bookstoscrap.category import get_books_url
from bookstoscrap.fetch import Fetch
from bookstoscrap.csv import fetch_data
from bcolors.colors import Color
import sys


def main(argv):
    if len(argv) >= 3 and argv[1] == "bookurl":
        book_url = [argv[2]]
        if fetch_data(argv, book_url, "book") == True:
            return

    elif len(argv) >= 3 and argv[1] == "category":
        categories = Fetch.categories('http://books.toscrape.com')
        for category in categories:
            if (category.name == argv[2].capitalize()):
                print(category.name)
        return
        # if categories == None:
        #     return
        # for category in categories:
        #     if category == argv[2].capitalize():
        #         books_urls = get_books_url(categories[category])
        #         if fetch_data(argv, books_urls, category) == True:
        #             return
        # print(Color.FAIL + "Error: category doesn't exist" + Color.ENDC)

    # elif len(argv) >= 2 and argv[1] == "getall":
    #     categories = get_categories('http://books.toscrape.com')
    #     if categories == None:
    #         return
    #     print(
    #         Color.WARNING +
    #         "Warning: this operaton will take some time. Please wait..."
    #         + Color.ENDC)
    #     for category in categories:
    #         if category != 'Books':
    #             books_urls = get_books_url(categories[category])
    #             if fetch_data(argv, books_urls, category) == False:
    #                 return
    else:
        print(Color.HEADER + "Usage: python main.py [OPTIONS]")
        print(
            "OPTIONS: getall, --save-img, bookurl [URL], category [CATEGORY]" +
            Color.ENDC)


if __name__ == "__main__":
    main(sys.argv)
