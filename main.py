from DoublyLinkedList import DoublyLinkedList


def main():
    dll = DoublyLinkedList()
    dll.add_first(1)
    dll.add_last(2)
    dll.add_first(3)
    dll.add_first(4)
    dll.add_last(5)
    dll.add_last(6)

    print(dll.remove_first())
    print(dll.remove_last())
    print(dll.remove_first())


if __name__ == "__main__":
    main()
