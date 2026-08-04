"""Deterministic Virtual Terminal. MIR node ID: terminal.virtual"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from runtime.virtual_card.card import VirtualCard

@dataclass
class VirtualTerminal:
    card: Optional[VirtualCard] = None
    log: List[dict] = field(default_factory=list)

    def connect(self, card: VirtualCard) -> bytes:
        self.card = card
        atr = card.power_on()
        self.log.append({"event": "connect", "atr": atr.hex()})
        return atr

    def transmit(self, c_apdu: bytes) -> bytes:
        if not self.card:
            raise RuntimeError("No card connected")
        r_apdu = self.card.exchange(c_apdu)
        self.log.append({"event": "exchange", "c_apdu": c_apdu.hex(), "r_apdu": r_apdu.hex()})
        return r_apdu

    def disconnect(self) -> None:
        self.card = None
        self.log.append({"event": "disconnect"})
