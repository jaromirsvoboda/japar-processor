import re

class JoParser():
    @staticmethod
    def parse(jo_content: str) -> object:
        # regex pattern
        pattern = r"(NAPETI S\[MPa\]  <_LIMITY L\[MPa\]_>  ZATEZOVACI STAV (\d+)[\s]+kSei[\s\S]*?________________________________________________________________________________________)"

        # find matches
        matches = re.findall(pattern, jo_content, re.DOTALL)

        # matches is a list of tuples, where each tuple contains the entire matched string and the number
        for match in matches:
            substring, load_case_number = match
            
            all_lines = [line for line in substring.splitlines() if "{pipe_id:" not in line]
            
            lines_by_elements: list[list[str]] = []
            for index, line in enumerate(all_lines):
                if line.startswith("           ___|"): # this is the line with limits
                    lines_of_one_element = [line]
                    temp_index = index - 1
                    while not all_lines[temp_index].startswith("           ___|") or not all_lines[index].startswith("              |"):
                        lines_of_one_element.insert(0, all_lines[temp_index])
                        temp_index -= 1
                    lines_by_elements.append(lines_of_one_element)
            print(lines_by_elements)