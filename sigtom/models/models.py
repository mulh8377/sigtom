from dataclasses import dataclass

@dataclass
class SDR:
    name: int 
    date: str
    description: str


@dataclass
class RecvSignal:
    freq: int
    date: int
    stream: bytes
    