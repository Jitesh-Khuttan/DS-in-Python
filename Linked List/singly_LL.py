
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class SingleLL:

    def __init__(self, value=None):
        self.root = self.__get_new_node(value, None) if value else None

    def __get_new_node(self, value, next):
        return Node(value, next)

    @property
    def is_empty(self):
        return True if self.root is None else False

    def append(self, value):
        node = self.__get_new_node(value, None)
        if self.is_empty:
            self.root = node
            return

        temp, previous = self.root, None
        while temp:
            previous, temp = temp, temp.next
        previous.next = node

    def prepend(self, value):
        node = self.__get_new_node(value, self.root)
        self.root = node

    def insert(self, position, value):
        if position == 0:
            self.prepend(value)
            return
        index, temp = 1, self.root
        while temp and index != position:
            index, temp = index+1, temp.next

        if temp is None:
            return IndexError(f"Index {position} is out of range.")
        node = self.__get_new_node(value, temp.next)
        temp.next = node

    def pop(self, position=None):
        """
        If no position is given, it pops the last element of linked list.
        """
        if self.is_empty:
            return "Can't delete from an empty list."

        index, temp, previous = 0, self.root, None
        while temp.next and (True if position is None else index != position):
            previous, temp, index = temp, temp.next, index + 1

        if previous is None: #=> position = 0
            self.root = temp.next
        else:
            previous.next = temp.next
        popped_value = temp.value
        del temp
        return popped_value

    def clear(self):
        while self.root:
            self.pop()


    def print_list(self):
        if self.is_empty:
            return None

        temp = self.root
        while temp:
            print(f"{temp.value} ")
            temp = temp.next

