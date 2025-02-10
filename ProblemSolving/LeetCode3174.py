class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to represent the stack

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top item
        else:
            return None  # Return None if the stack is empty (or raise an exception)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item without removing it
        else:
            return None  # Return None if the stack is empty

    def size(self):
        return len(self.items)  # Return the number of items in the stack

def clearDigit(s: str) -> str:
    s = list(s)
    index = 0
    while index < len(s):
        if s[index].isdigit():
            del s[index]
            if index > 0:
                del s[index - 1]
                index -= 1
        else:
            index += 1

    return "".join(s)

test_1 = "abc"
test_2 = "ac16"
test_3 = "3"
test_4 = "61"
print(f'ket qua: {clearDigit(test_1)}')
print(f'ket qua: {clearDigit(test_2)}')
print(f'ket qua: {clearDigit(test_3)}')
print(f'ket qua: {clearDigit(test_4)}')