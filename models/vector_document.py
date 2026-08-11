from dataclasses import dataclass
from typing import List, Dict

@dataclass
class VectorDocument:
    id:str
    content: str
    embedding: List[float]
    metadata: Dict[str,str]

