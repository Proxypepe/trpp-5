import sys

from converter import Converter


def main():
    if len(sys.argv) > 3:
        try:
            print(Converter.convert(float(sys.argv[1]), sys.argv[2], sys.argv[3]))
        except Exception as e:
            print("Error")
    else:
        print("Invalid enter")

if __name__ == '__main__':
    main()
