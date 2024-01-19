import re

class JoParser():
    @staticmethod
    def parse(jo_content: str) -> object:
        # regex pattern
        pattern = r"(NAPETI S\[MPa\]  <_LIMITY L\[MPa\]_>  ZATEZOVACI STAV (\d+)[\s]+kSei[\s\S]*?________________________________________________________________________________________)"

        matches = re.findall(pattern, jo_content, re.DOTALL)

        for match in matches:
            substring, load_case_number = match
            
            all_lines = [line for line in substring.splitlines() if "{pipe_id:" not in line]
            
            lines_by_elements: list[list[str]] = []
            for index, line in enumerate(all_lines):
                if line.startswith("           ___|"): # this is the line with limits
                    lines_of_one_element = [line]
                    temp_index = index - 1
                    while not all_lines[temp_index].startswith("           ___|") and not all_lines[temp_index].startswith("              |"):
                        lines_of_one_element.insert(0, all_lines[temp_index])
                        temp_index -= 1
                    lines_by_elements.append(lines_of_one_element)
            
        for lines_by_elements_tuple in lines_by_elements:
            if lines_by_elements_tuple[0][50] == "": # this is not an elbow
                continue