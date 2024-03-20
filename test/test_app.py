import pytest
from unittest.mock import Mock
from ohce import Ohce
from clock import Clock, PartOfDay

def test_ohce_greet_morning():
    ohce = Ohce("fr")
    ohce.clock = Mock(spec=Clock)
    ohce.clock.get_hour.return_value = 7
    ohce.clock.what_part_of_day.return_value = PartOfDay.MORNING
    assert ohce.greet() == "Bonjour"

def test_ohce_echo_palindrome():
    ohce = Ohce("fr")
    assert ohce.echo("level") == "level (Bien dit!)"

def test_ohce_farewell():
    ohce = Ohce("fr")
    assert ohce.farewell() == "Au revoir"

def test_ohce_greet_afternoon():
    ohce = Ohce("fr")
    ohce.clock = Mock(spec=Clock)
    ohce.clock.get_hour.return_value = 15
    ohce.clock.what_part_of_day.return_value = PartOfDay.AFTERNOON
    assert ohce.greet() == "Bon après-midi"

def test_ohce_greet_evening():
    ohce = Ohce("fr")
    ohce.clock = Mock(spec=Clock)
    ohce.clock.get_hour.return_value = 20
    ohce.clock.what_part_of_day.return_value = PartOfDay.EVENING
    assert ohce.greet() == "Bonsoir"
