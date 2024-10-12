Stack Data Structure

    •	Definition: A stack is a data structure that allows adding and removing elements only from one end, known as the “top” of the stack.
    •	Physical World Analogy: Can be thought of as a stack of plates—where you can only add or remove plates from the top, not the middle or bottom.
    •	LIFO Principle: Stacks operate on a Last In, First Out (LIFO) basis, meaning the last element added is the first to be removed.

Stack Operations

    1.	Push:
    •	Adds an element to the top of the stack.
    •	Efficient operation with time complexity of O(1).
    •	Involves appending an element to the end of a dynamic array.
    •	Example pseudocode:

def push(self, n):
self.stack.append(n)

    2.	Pop:
    •	Removes the last (top) element from the stack.
    •	Efficient operation with time complexity of O(1).
    •	Before popping, it’s advisable to check if the stack is empty to avoid errors.
    •	Example pseudocode:

def pop(self):
return self.stack.pop()

    3.	Peek:
    •	Returns the top element without removing it from the stack.
    •	Efficient operation with time complexity of O(1).
    •	Example pseudocode:

def peek(self):
return self.stack[-1]

Time Complexity of Stack Operations

    •	Push: O(1)
    •	Pop: O(1) (Ensure to check if the stack is empty before popping to avoid errors)
    •	Peek/Top: O(1) (Retrieves the top element without removing it)

Additional Notes

    •	Dynamic Array Simulation: In many programming languages, there is no built-in stack structure. However, you can use dynamic arrays to simulate stack behavior.
    •	Reversing Sequences: Since a stack removes elements in the reverse order they were added, it can be used to reverse sequences, such as strings (which are sequences of characters).
