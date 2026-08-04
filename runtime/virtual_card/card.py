"""Deterministic Virtual Smart Card. MIR node ID: card.virtual"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from runtime.apdu.parser import parse_c_apdu

@dataclass
class VirtualCard:
    atr: bytes = bytes.fromhex("3B00")
    state: str = "idle"
    history: List[bytes] = field(default_factory=list)

    def power_on(self) -> bytes:
        self.state = "idle"
        return self.atr

    def reset(self) -> bytes:
        return self.power_on()

    def exchange(self, c_apdu: bytes) -> bytes:
        self.history.append(c_apdu)
        cmd = parse_c_apdu(c_apdu)
        if cmd.ins == 0xA4:  # SELECT
            self.state = "selected"
            return bytes.fromhex("6F00") + bytes([0x90, 0x00])
        if cmd.ins == 0xA8:  # GPO
            self.state = "initiated"
            return bytes.fromhex("8000") + bytes([0x90, 0x00])
        if cmd.ins == 0xB2:  # READ RECORD
            self.state = "data_read"
            return bytes([0x90, 0x00])
        if cmd.ins == 0xAE:  # GENERATE AC
            self.state = "completed"
            return bytes.fromhex("9F270180") + bytes([0x90, 0x00])
        return bytes([0x6D, 0x00])
