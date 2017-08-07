# 
# Example file for retrieving data from the internet
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import urllib.request


def main():
    webUrl = urllib.request.urlopen("http://joemarini.com")

    print("Result code: " + str(webUrl.getcode()))

    data = webUrl.read()
    print(data)

if __name__ == "__main__":
    main()
