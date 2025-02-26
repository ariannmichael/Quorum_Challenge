from dataclasses import dataclass


@dataclass
class VoteResult:
    id: int
    legislator_id: int
    vote_id: int
    vote_type: int # 1 for yea, 2 for nay.