import re


def main(text):
    regex_nums = r"'(.+?)'"
    regex_names = r'"(.+?)"'
    names = re.findall(regex_names, text)
    nums = re.findall(regex_nums, text)
    res = list(zip(names, nums))
    return res


print(
    main(
        """<sect> begin variable'leerbe_736' to "tere". end. begin
variable'arela_574'to "isxequ". end.</sect>"""
    )
)
