"""EMV Runtime Kernel. MIR node ID: runtime.emv_kernel"""
from __future__ import annotations
from dataclasses import dataclass
from runtime.virtual_card.card import VirtualCard
from runtime.virtual_terminal.terminal import VirtualTerminal

@dataclass
class EmvKernel:
    card: VirtualCard
    terminal: VirtualTerminal

    def __post_init__(self):
        self.terminal.connect(self.card)

    def run_purchase(self) -> list:
        steps = []
        sel = bytes.fromhex("00A404000E325041592E5359532E4444463031")
        r = self.terminal.transmit(sel)
        steps.append({"command": "SELECT", "request": sel.hex(), "response": r.hex()})
        gpo = bytes.fromhex("80A80000028300")
        r = self.terminal.transmit(gpo)
        steps.append({"command": "GPO", "request": gpo.hex(), "response": r.hex()})
        rr = bytes.fromhex("00B2010C00")
        r = self.terminal.transmit(rr)
        steps.append({"command": "READ RECORD", "request": rr.hex(), "response": r.hex()})
        ac = bytes.fromhex("80AE800000")
        r = self.terminal.transmit(ac)
        steps.append({"command": "GENERATE AC", "request": ac.hex(), "response": r.hex()})
        return steps
