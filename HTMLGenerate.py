class HTMLGenerator:
    def __init__(self, tokens):
        self.filename = "Colored_code.html"
        self.tokens = tokens

    def generate(self):
        html_output = "<html>\n<body style='background-color: black;'>\n<pre>\n"
        for token_code, token_value in self.tokens:
            color = token_code.get_color()
            safe_value = str(token_value).replace("<", "&lt;").replace(">", "&gt;")

            if color != "":
                html_output += f"<span style='color:{color}'>{safe_value}</span>"
            else:
                html_output += safe_value

        html_output += "\n</pre>\n</body>\n</html>"

        with open(self.filename, "w") as f:
            f.write(html_output)


