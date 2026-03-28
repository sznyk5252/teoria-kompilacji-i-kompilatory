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

    html_output = "<html>\n<body style='background-color: black;'>\n<pre>\n"
    for token_code, token_value in my_scaner._tokens:
        color = token_code.get_color()

        safe_value = str(token_value).replace("<", "&lt;").replace(">", "&gt;")

        if color != "":
            html_output += f"<span style='color:{color}'>{safe_value}</span>"
        else:
            html_output += safe_value

    html_output += "\n</pre>\n</body>\n</html>"

    with open("Colored_code.html", "w") as f:
        f.write(html_output)

    # print((TokenCode.INTEGER,'5'))
    # print(re.fullmatch(r'-?[0-9]+\.?[0-9]*','-134,1'))


if __name__ == "__main__":
    main()
