"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        # self.value = value

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        # print(f'self.storage {self.storage}')
        self.size += 1
        return self.storage

    def pop(self):
        if self.size == 0:
            return None

        if self.size > 0:
            new_value = self.storage.pop()
            self.size -= 1

        # print(f'storage: {self.storage}')
        print(f'{len(self.storage)}')
        return new_value
