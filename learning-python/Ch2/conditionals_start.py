#
# Example file for working with conditional statements
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
    x, y = 10, 100

    if x < y :
        str = "x is less than y"
    elif x > y:
        str = "y is less than x";
    else:
        str = "x is equal to y"

    print(str)

    st = "x is less than y" if x < y else "x is greater than or equal to y"
    print(st)
  
if __name__ == "__main__":
    main()
