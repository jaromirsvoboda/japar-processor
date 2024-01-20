import re
from dataclasses import dataclass

@dataclass
class ElbowJoData():
    names: list[str]
    loads: list[int]
    load_limit: int
    
    @property
    def name(self) -> str:
        return " - ".join(self.names)
    

class JoParser():
    @staticmethod
    def parse(jo_content: str) -> dict[str, list[ElbowJoData]]:
        pattern = r"(NAPETI S\[MPa\]  <_LIMITY L\[MPa\]_>  ZATEZOVACI STAV (\d+)[\s]+kSei[\s\S]*?________________________________________________________________________________________)"
        matches = re.findall(pattern, jo_content, re.DOTALL)
        
        cases_to_elbows: dict[str, list[ElbowJoData]] = {}

        for match in matches:
            substring, load_case_number = match
            all_lines = [line for line in substring.splitlines() if "{pipe_id:" not in line]
            
            assert load_case_number not in cases_to_elbows
            cases_to_elbows[load_case_number] = []
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
                if lines_by_elements_tuple[0][48] == " ": # this is not an elbow
                    continue
                assert len(lines_by_elements_tuple[0].strip().split()) == 23
                loads = []
                for line in lines_by_elements_tuple[:-1]:
                    split_line = line.strip().split()
                    loads.append(int(split_line[7].replace(":", "")))
                    loads.append(int(split_line[8].replace(":", "")))
                
                load_limit = int(lines_by_elements_tuple[-1].split("<_____", 1)[1].split("_____>", 1)[0])
                cases_to_elbows[load_case_number].append(ElbowJoData(
                    names=[first_part.split()[0].strip() for first_part in lines_by_elements_tuple[:-1]],
                    loads=loads,
                    load_limit=load_limit
                ))
                
        return cases_to_elbows