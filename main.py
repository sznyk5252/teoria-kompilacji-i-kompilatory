from scaner import Scaner
from tokens import TokenCode


def main():
    input_str = input()
    my_scaner = Scaner(input_str)
    my_scaner.tokenize()
    print(my_scaner)
    # print((TokenCode.INTEGER,'5'))


if __name__ == "__main__":
    main()
