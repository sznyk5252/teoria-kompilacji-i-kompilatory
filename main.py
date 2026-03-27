from scaner import Scaner
from tokens import TokenCode
# import re
import sys

def main():
    input_str = sys.stdin.read()
    my_scaner = Scaner(input_str)
    try:
        my_scaner.tokenize()
    except Exception:
        print(my_scaner)
        raise
    # print(my_scaner)
    # print((TokenCode.INTEGER,'5'))
    print(my_scaner)

    # print(re.fullmatch(r'-?[0-9]+\.?[0-9]*','-134,1'))

if __name__ == "__main__":
    main()
