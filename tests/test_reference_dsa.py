import pytest

from src.dsa.queue import Queue
from src.dsa.searching import binary_search, linear_search
from src.dsa.sorting import merge_sort
from src.dsa.stack import Stack


def test_linear_search():
    assert linear_search([4, 2, 9], 2) == 1
    assert linear_search([4, 2, 9], 7) == -1


def test_binary_search():
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5, 7, 9], 2) == -1


def test_merge_sort():
    assert merge_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]


def test_stack():
    stack = Stack()
    stack.push("a")
    stack.push("b")

    assert stack.peek() == "b"
    assert stack.pop() == "b"
    assert stack.pop() == "a"
    with pytest.raises(IndexError):
        stack.pop()


def test_queue():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")

    assert queue.dequeue() == "a"
    assert queue.dequeue() == "b"
    with pytest.raises(IndexError):
        queue.dequeue()
