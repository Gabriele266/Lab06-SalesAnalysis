from dataclasses import dataclass

@dataclass(frozen=True)
class RetailerDTO:
    code: int
    name: str
    type: str
    country: str