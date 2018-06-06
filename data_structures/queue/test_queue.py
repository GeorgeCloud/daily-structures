from random import randrange
from queue import Queue
import pytest

random_value = randrange(100)

@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def populated_queue():
    return Queue([randrange(100) for _ in range(10)])


def test_queue_length(empty_queue):
    """Validates if length updates."""
    assert empty_queue._len == 0
    empty_queue.enqueue(random_value)
    assert empty_queue._len == 1


def test_queue_appends(populated_queue):
    """Validates that node queued is added to the back."""
    assert populated_queue.back.val != random_value
    populated_queue.enqueue(random_value)
    assert populated_queue.back.val == random_value


def test_queue_dequeues(populated_queue):
    """Validates"""
    previous_head = populated_queue.head

    # Remove head node
    populated_queue.dequeue()

    # Compare previous_head and current head
    assert populated_queue.head.val != previous_head.val
