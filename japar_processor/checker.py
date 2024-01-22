from .jo_parser import ElbowJoData
from dataclasses import dataclass

@dataclass
class ElbowCheckResult:
    start_element: str
    end_element: str
    max_load: int
    # output_line: str
    load_limit: int
    
    @property
    def sl(self) -> float:
        return self.max_load / self.load_limit
    
    @property
    def ls(self) -> float:
        return self.load_limit / self.max_load
    
    @property
    def output_line(self) -> str:
        start_element_name = self.start_element.split("'")[0].split("\"")[0].split("~")[0]
        end_element_name = self.end_element.split("'")[0].split("\"")[0].split("~")[0]
        
        return (
            f"│        │        kol.│{start_element_name.rjust(6, ' ')} {end_element_name.rjust(6, ' ')} │{format(self.max_load, '.1f').rjust(8, ' ')}  │"
            + f"{format(self.load_limit, '.1f').rjust(7, ' ')}  │{format(self.sl, '.3f').rjust(8, ' ')} {' ' if self.sl < 1 else '*'}│{format(self.ls, '.3f').rjust(11, ' ')} {' ' if self.ls > 1 else '*'}│"
        )

class Checker():
    @staticmethod
    def check_elbows(elbow_data: dict[str, list[ElbowJoData]]) -> dict[str, list[ElbowCheckResult]]:
        all_elbow_results: dict[str, list[ElbowCheckResult]] = {}
        for load_case_name, elbows in elbow_data.items():
            elbow_results_for_this_case: list[ElbowCheckResult] = []
            for elbow in elbows:
                max_load = max(elbow.loads)
                elbow_results_for_this_case.append(ElbowCheckResult(
                    start_element=elbow.names[0],
                    end_element=elbow.names[-1],
                    max_load=max_load,
                    load_limit=elbow.load_limit
                ))
            all_elbow_results[load_case_name] = sorted(elbow_results_for_this_case, key=lambda x: x.sl, reverse=True)
        return all_elbow_results
