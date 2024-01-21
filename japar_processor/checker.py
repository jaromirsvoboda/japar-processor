from .jo_parser import ElbowJoData
from dataclasses import dataclass

@dataclass
class ElbowCheckResult:
    output_line: str

class Checker():
    @staticmethod
    def check_elbows(elbow_data: dict[str, list[ElbowJoData]]) -> dict[str, ElbowCheckResult]:
        for load_case_name, elbows in elbow_data.items():
            for elbow in elbows:
                max_load = max(elbow.loads)