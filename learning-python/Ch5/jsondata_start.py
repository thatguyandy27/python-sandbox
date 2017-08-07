# 
# Example file for parsing and processing JSON
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
import urllib.request
import json


def printResults(data):
    jsonObject = json.loads(data)

    if "title" in jsonObject["metadata"]:
        print(jsonObject["metadata"]["title"])

    count = jsonObject["metadata"]["count"]
    print(str(count) + " events recorded")

    for i in jsonObject["features"]:
        print(i["properties"]["place"])

    for i in jsonObject["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

    for i in jsonObject["features"]:
        if (i["properties"]["felt"]) and (i["properties"]["felt"] > 0):
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
                  " reported " + str(i["properties"]["felt"]) + " times")


def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)

    if webUrl.getcode() == 200:
        data = webUrl.read()

        printResults(data)
  

if __name__ == "__main__":
    main()
