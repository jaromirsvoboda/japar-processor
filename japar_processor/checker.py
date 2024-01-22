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
        return ""
        # return f"{self.start_element} - {self.end_element} - {self.max_load} - {self.load_limit} - {self.sl} - {self.ls}"

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
            all_elbow_results[load_case_name] = elbow_results_for_this_case
        return all_elbow_results