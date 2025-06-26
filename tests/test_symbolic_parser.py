"""
test_symbolic_parser.py

Symbolic test: validates the parser’s ability to interpret archetypal glyphs.
"""

from src.symbolic_parser import SymbolicParser, ARCHETYPES

def test_parser_detects_known_symbols():
    parser = SymbolicParser()
    fragment = "☯✵❖"
    result = parser.parse_fragment(fragment)
    assert all(symbol in ARCHETYPES for symbol in result.keys()), "Unknown symbols misinterpreted."

def test_parser_returns_meanings():
    parser = SymbolicParser()
    fragment = "⌘∴"
    result = parser.parse_fragment(fragment)
    meanings = list(result.values())
    assert all(isinstance(m, str) and len(m) > 0 for m in meanings), "Empty or invalid meanings returned."

def test_random_prompt_outputs_valid_symbol():
    parser = SymbolicParser()
    symbol = parser.random_prompt()
    assert symbol in ARCHETYPES, "Random prompt produced unknown symbol."
