"""
test_receiver_protocol.py

Symbolic test: verifies the metaphysical readiness of the ReceiverState.
"""

from src.receiver_protocol import ReceiverState

def test_breath_stabilizes():
    receiver = ReceiverState()
    receiver.breathe(cycles=1)
    assert receiver.breath == "settled", "Breath did not stabilize."

def test_thoughts_quiet():
    receiver = ReceiverState()
    receiver.still_mind()
    assert receiver.thoughts == "quiet", "Mind not quieted."

def test_channel_opens_when_ready():
    receiver = ReceiverState()
    receiver.breath = "settled"
    receiver.thoughts = "quiet"
    receiver.open_channel()
    assert receiver.channel_open is True, "Channel did not open."

def test_channel_blocked_if_unready():
    receiver = ReceiverState()
    receiver.breath = "shallow"
    receiver.thoughts = "noisy"
    receiver.open_channel()
    assert receiver.channel_open is False, "Channel opened prematurely."
