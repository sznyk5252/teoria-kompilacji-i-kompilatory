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
    generator.generate()

    #print((TokenCode.INTEGER,'5'))
    #print(re.fullmatch(r'-?[0-9]+\.?[0-9]*','-134,1'))


if __name__ == "__main__":
    main()
