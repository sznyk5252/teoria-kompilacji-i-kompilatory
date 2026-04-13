from dataclasses import dataclass, field
from typing import Iterable
from tokens import Token

@dataclass
class HTMLGenerator:
    tokens: Iterable[Token]
    _output: str = field(init=False)

    def __post_init__(self):
        self._generate()

    def _generate(self):
        html_output = "<html>\n<body style='background-color: black;'>\n<pre>\n"
        for token_code, token_value in self.tokens:
            color = token_code.get_color()
            safe_value = str(token_value).replace("<", "&lt;").replace(">", "&gt;")

            if color != "":
                html_output += f"<span style='color:{color}'>{safe_value}</span>"
            else:
                html_output += safe_value

        html_output += "\n</pre>\n</body>\n</html>"
        self._output = html_output

        
    def get_str(self):
        return self._output
    
    def write_to_file(self, filename: str):
        with open(filename, "w") as f:
            f.write(self._output)
    

