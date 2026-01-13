import pytest
from bank_app import transfer, calculate_interest

# ---------------- transfer ----------------

def test_transfer_valid():
    from_balance, to_balance = transfer(1000, 500, 300)
    assert from_balance == 700
    assert to_balance == 800

def test_transfer_boundary():
    from_balance, to_balance = transfer(500, 200, 500)
    assert from_balance == 0
    assert to_balance == 700

def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, 0)

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(300, 200, 500)

# ---------------- Integration Workflow ----------------

def test_transfer_then_interest():
    from_balance, to_balance = transfer(1000, 500, 500)
    new_balance = calculate_interest(to_balance, 10, 1)
    assert new_balance == 1100.0
