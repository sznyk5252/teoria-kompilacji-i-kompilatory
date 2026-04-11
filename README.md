komenda do testów:
```
uv run universal-checker/test.py -dp ./main.py tests/
```

|          Token         | TokenCode (Enum) |     Description     |     Example Matches     |
|:----------------------:|:----------------:|:-------------------:|:-----------------------:|
|     LEFT_PARENTESE     |        LP        |   Left parenthesis  |            (            |
|     RIGHT_PARENTESE    |        RP        |  Right parenthesis  |            )            |
|        SEPARATOR       |        SEP       |        Comma        |            ,            |
|         NUMBER         |       NUMB       |       Numbers       |   10, -15, 12.3, -0.9   |
|         STRING         |        STR       |       Strings       |     abc, x + y == 10    |
|          SPACE         |       SPACE      |     Single space    |           ' '           |
|         NEWLINE        |      NEWLINE     |  Newline character  |            \n           |
|         COMMENT        |        COM       | Single-line comment |            #            |
|        VAR(name)       |        TAG       |   Variable capture  |          VAR(x)         |
|       FINALCHECK       |        TAG       |   Final assertion   | FINALCHECK(x + y == 10) |
|     MATCH(pattern)     |        TAG       |  Felxible matching  |       MATCH(x > 0)      |
| ANYOF(opt1, opt2, ...) |        TAG       |   Multiple choice   |   ANYOF(yes, YES, yES)  |
|     DEF(var, value)    |        TAG       |  Constant definiton |   DEF(max_limit, 100)   |
|         REP(n)         |        TAG       |   Loop validation   |         REP(10)         |
|      THROWS(error)     |        TAG       |   Negative testing  |    THROWS(Exception)    |
|     RANGE(from, to)    |        TAG       |    Boundary check   |       RANGE(0, 10)      |