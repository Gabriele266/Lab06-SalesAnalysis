from dataclasses import dataclass

@dataclass
class ProductDTO:
    number: int
    line: str
    type: str
    name: str
    brand: str
    color: str
    unit_cost: int
    unit_price: int

    def __hash__(self):
        return hash(self.number)