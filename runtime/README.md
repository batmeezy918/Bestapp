# CVR EMV Runtime

Deterministic runtime modules projected from the MIR.

| Module | MIR Node ID | Role |
|--------|-------------|------|
| apdu/ | parser.apdu | ISO 7816 C-APDU / R-APDU parser |
| tlv/ | parser.tlv | BER-TLV / EMV TLV parser |
| virtual_card/ | card.virtual | Virtual Smart Card |
| virtual_terminal/ | terminal.virtual | Virtual Terminal |
| emv_kernel/ | runtime.emv_kernel | Linked EMV transaction engine |
