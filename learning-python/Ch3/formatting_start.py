#
# Example file for formatting time and date output
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import datetime

def main():
    now = datetime.now()

    print(now.strftime("%Y"))
    print(now.strftime("%y"))

    print(now.strftime("%a, %d, %B, %y"))

    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))

    print(now.strftime("%I:%M:%S %p"))
    print(now.strftime("%H:%M"))

if __name__ == "__main__":
    main();

