from dataclasses import dataclass, field
from typing import List


@dataclass
class Point:
    x: float
    y: float
    neihbours: List["Point"] = field(default_factory=lambda: [])


point = Point(1.0, 2.0)
print(point)
