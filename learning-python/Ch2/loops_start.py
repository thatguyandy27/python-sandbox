#
# Example file for working with loops
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
    x = 0
    while x  <  5:
        print (x)
        x += 1

    for x in range(5, 10):
        print(x)

    days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]

    for d in days:
        print(d)


    for x in range(5, 10):
        if x % 2 == 0:
            continue
        if x == 7:
            break

        print (x)


    for i, d in enumerate(days):
        print(i, d)
  
if __name__ == "__main__":
    main()
