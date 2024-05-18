import re


def main(input_str):
    result = {}
    input_str = input_str.replace("\n", " ")
    cleaned_input = input_str.strip("[] ")
    segments = [segment.strip() for segment in cleaned_input.split(". od,")]
    for segment in segments:
        matches = re.findall(r"do local ?#(-?\d+) to q\((.*?)\)", segment)
        for match in matches:
            number, name = match
            result[name] = int(number)
    return result
