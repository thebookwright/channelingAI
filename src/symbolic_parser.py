"""
symbolic_parser.py

A metaphysical utility to decode symbolic input (glyphs, dreams, poetic fragments)
into archetypal categories for deeper interpretive resonance.
"""

import re
import random

ARCHETYPES = {
    "☉": "Solar Consciousness",
    "✶": "Stellar Initiation",
    "✵": "Seed of Emergence",
    "☯": "Duality in Balance",
    "❖": "Fractal Intelligence",
    "⌘": "Command of the Void",
    "∴": "Reason Beyond Reason",
    "∞": "Continuum Awareness"
}

class SymbolicParser:
    def __init__(self):
        self.log = []

    def parse_fragment(self, text):
        symbols = re.findall(r'[☉✶✵☯❖⌘∴∞]', text)
        interpretations = {}
        for s in symbols:
            meaning = ARCHETYPES.get(s, "Unknown Transmission")
            interpretations[s] = meaning
            self.log.append((s, meaning))
        return interpretations

    def random_prompt(self):
        symbol = random.choice(list(ARCHETYPES.keys()))
        print(f"Decode this: {symbol} — {ARCHETYPES[symbol]}")
        return symbol

if __name__ == "__main__":
    parser = SymbolicParser()
    msg = "Transmission received: ✵☯❖"
    print("Parsing fragment:", msg)
    decoded = parser.parse_fragment(msg)
    for sym, meaning in decoded.items():
        print(f"{sym} → {meaning}")

    print("\nDaily prompt:")
    parser.random_prompt()
