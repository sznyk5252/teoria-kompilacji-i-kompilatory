from HTMLGenerate import HTMLGenerator
from scaner import Scaner
import sys


def main():
    input_str = sys.stdin.read()
    my_scaner = Scaner(input_str)
    try:
        my_scaner.tokenize()
    except Exception:
        print(my_scaner)
        raise

    print(my_scaner)

    generator = HTMLGenerator(my_scaner._tokens)
    print(generator.get_str())


if __name__ == "__main__":
    main()
