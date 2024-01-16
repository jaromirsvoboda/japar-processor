import re

class JoParser():
    @staticmethod
    def parse(jo_content: str) -> object:
        # regex pattern
        pattern = r"(NAPETI S\[MPa\]  <_LIMITY L\[MPa\]_>  ZATEZOVACI STAV (\d+) kSei[\s\S]*?________________________________________________________________________________________)"

        # find matches
        matches = re.findall(pattern, jo_content)

        # matches is a list of tuples, where each tuple contains the entire matched string and the number
        for match in matches:
            substring, number = match
            print(f"Substring: {substring}")
            print(f"Number: {number}")