from .queue_number import SList
import pytest

new_person = 'Emma'

# Singly List instance with 4 people already in queue.
@pytest.fixture
def contestant_line():
    line = SList(['Emily', 'Sandy', 'Jenny', 'Sally'])
    return line


def test_new_candidate_is_first(contestant_line):
    """Validates new person is added to the back of the line(First Node)."""
    contestant_line.get_queue(new_person)
    assert contestant_line.head.get_value() == new_person


def test_position_ticket(contestant_line):
    """
    Validates that the person was added and was given the correct ticket
    queue number.
    """
    assert contestant_line._len == 4
    contestant_line.get_queue(new_person)
    assert contestant_line._len == 5
