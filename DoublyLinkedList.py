from typing import Any


class ListNode:
    def __init__(self, data, prev=None, link=None) -> None:
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = None
        self._prev = None
        self._tail = None
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def _add_node(self, item, before, after) -> None:
        node = ListNode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def _remove_node(self, node: ListNode) -> Any:
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1
        return node.data

    def add_first(self, item):
        self._add_node(item, None, self._head)

    def add_last(self, item):
        self._add_node(item, self._tail, None)

    def remove_first(self) -> Any:
        return self._remove_node(self._head)

    def remove_last(self) -> Any:
        return self._remove_node(self._tail)
