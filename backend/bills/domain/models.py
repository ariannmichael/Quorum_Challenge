from dataclasses import dataclass

@dataclass
class Bill:
    id: int
    title: str
    primary_sponsor: int