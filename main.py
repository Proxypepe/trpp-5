import sys


from C_converter import convert


def main():
    if len(sys.argv) > 3:
        try:
            result = convert(float(sys.argv[1]), sys.argv[2], sys.argv[3])
            print(result)
            return result
        except Exception:
            print("Error")
            return "Error"
    else:
        print("Invalid enter")
        return "Invalid enter"


if __name__ == '__main__':
    main()
