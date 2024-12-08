# test with pytest --spec

import pytest
from battery import Battery
from unittest.mock import Mock

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b

def describe_Battery():

    def describe_getCapacity():
        def test_returns_initial_capacity(charged_battery):
            assert charged_battery.getCapacity() == 100

    def describe_getCharge():
        def test_returns_initial_charge(charged_battery):
            assert charged_battery.getCharge() == 100

        def test_returns_partial_charge(partially_charged_battery):
            assert partially_charged_battery.getCharge() == 70

    def describe_recharge():
        def test_recharge_increases_charge(partially_charged_battery):
            before = partially_charged_battery.getCharge()
            partially_charged_battery.recharge(20)
            assert partially_charged_battery.getCharge() == before + 20

        def test_recharge_does_not_exceed_capacity(partially_charged_battery):
            partially_charged_battery.recharge(1000)
            assert partially_charged_battery.getCharge() == 100

        def test_recharge_fails_with_non_positive_amount(partially_charged_battery):
            result = partially_charged_battery.recharge(0)
            assert result is False
            assert partially_charged_battery.getCharge() == 70

        def test_recharge_fails_if_already_full(charged_battery):
            result = charged_battery.recharge(10)
            assert result is False
            assert charged_battery.getCharge() == 100

        def test_recharge_with_external_monitor(partially_charged_battery):
            mock_monitor = Mock()
            b = Battery(100, external_monitor=mock_monitor)
            b.mCharge = 50
            b.recharge(30)
            # Check that notify_recharge was called with the updated charge
            mock_monitor.notify_recharge.assert_called_once_with(80)

        def test_recharge_with_external_monitor_no_call_on_failure(charged_battery):
            mock_monitor = Mock()
            b = Battery(100, external_monitor=mock_monitor)
            b.mCharge = 100
            # Trying to recharge full battery should fail and not call monitor
            result = b.recharge(10)
            assert result is False
            mock_monitor.notify_recharge.assert_not_called()

    def describe_drain():
        def test_drain_decreases_charge(charged_battery):
            before = charged_battery.getCharge()
            charged_battery.drain(10)
            assert charged_battery.getCharge() == before - 10

        def test_drain_does_not_go_below_zero(charged_battery):
            charged_battery.drain(1000)
            assert charged_battery.getCharge() == 0

        def test_drain_fails_with_non_positive_amount(charged_battery):
            result = charged_battery.drain(0)
            assert result is False
            assert charged_battery.getCharge() == 100

        def test_drain_fails_if_empty_battery():
            b = Battery(100)
            b.mCharge = 0
            result = b.drain(10)
            assert result is False
            assert b.getCharge() == 0

        def test_drain_with_external_monitor(charged_battery):
            mock_monitor = Mock()
            b = Battery(100, external_monitor=mock_monitor)
            b.mCharge = 50
            b.drain(20)
            # Check that notify_drain was called with the updated charge
            mock_monitor.notify_drain.assert_called_once_with(30)

        def test_drain_with_external_monitor_no_call_on_failure():
            mock_monitor = Mock()
            b = Battery(100, external_monitor=mock_monitor)
            b.mCharge = 0
            # Attempt to drain empty battery should fail and not call monitor
            result = b.drain(10)
            assert result is False
            mock_monitor.notify_drain.assert_not_called()