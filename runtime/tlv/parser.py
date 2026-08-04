"""Deterministic BER-TLV / EMV TLV parser. MIR node ID: parser.tlv"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List

class TlvError(ValueError):
    pass

@dataclass(frozen=True)
class TlvNode:
    tag: str
    length: int
    value: bytes
    children: tuple

def _read_tag(data: bytes, i: int):
    if i >= len(data):
        raise TlvError("truncated tag")
    first = data[i]
    i += 1
    tag = f"{first:02X}"
    if (first & 0x1F) == 0x1F:
        while i < len(data):
            b = data[i]
            i += 1
            tag += f"{b:02X}"
            if b & 0x80 == 0:
                break
        else:
            raise TlvError("truncated multi-byte tag")
    return tag, i

def _read_length(data: bytes, i: int):
    if i >= len(data):
        raise TlvError("truncated length")
    b = data[i]
    i += 1
    if b & 0x80 == 0:
        return b, i
    n = b & 0x7F
    if n == 0 or i + n > len(data):
        raise TlvError("invalid length")
    length = int.from_bytes(data[i:i+n], "big")
    return length, i + n

def parse_tlv(data: bytes) -> List[TlvNode]:
    nodes = []
    i = 0
    while i < len(data):
        tag, i = _read_tag(data, i)
        length, i = _read_length(data, i)
        if i + length > len(data):
            raise TlvError("truncated value")
        value = data[i:i+length]
        i += length
        nodes.append(TlvNode(tag=tag, length=length, value=value, children=()))
    return nodes
