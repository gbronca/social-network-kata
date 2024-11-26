from dataclasses import dataclass
from datetime import datetime

@dataclass
class Post:
    time: datetime
    name: str
    message: str
