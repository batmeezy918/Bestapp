"""Deterministic ISO 7816 APDU parser. MIR node ID: parser.apdu"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

class ApduError(ValueError):
    pass

@dataclass(frozen=True)
class CommandApdu:
    cla: int
    ins: int
    p1: int
    p2: int
    lc: Optional[int]
    data: bytes
    le: Optional[int]

    def to_bytes(self) -> bytes:
        body = bytes([self.cla, self.ins, self.p1, self.p2])
        if self.lc is not None:
            body += bytes([self.lc]) + self.data
        if self.le is not None:
            body += bytes([self.le])
        return body

@dataclass(frozen=True)
class ResponseApdu:
    data: bytes
    sw1: int
    sw2: int

    @property
    def sw(self) -> int:
        return (self.sw1 << 8) | self.sw2

    def to_bytes(self) -> bytes:
        return self.data + bytes([self.sw1, self.sw2])

def parse_c_apdu(raw: bytes) -> CommandApdu:
    if len(raw) < 4:
        raise ApduError("C-APDU too short")
    cla, ins, p1, p2 = raw[0], raw[1], raw[2], raw[3]
    rest = raw[4:]
    lc = data = le = None
    if not rest:
        pass
    elif len(rest) == 1:
        le = rest[0]
    else:
        lc = rest[0]
        if len(rest) < 1 + lc:
            raise ApduError("C-APDU data truncated")
        data = rest[1:1+lc]
        if len(rest) > 1 + lc:
            le = rest[1+lc]
    return CommandApdu(cla, ins, p1, p2, lc, data or b"", le)

def parse_r_apdu(raw: bytes) -> ResponseApdu:
    if len(raw) < 2:
        raise ApduError("R-APDU too short")
    return ResponseApdu(data=raw[:-2], sw1=raw[-2], sw2=raw[-1])
