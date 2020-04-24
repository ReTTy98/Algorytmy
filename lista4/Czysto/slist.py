class QueueElement:
    def __init__(self, value):
        self.previous = None
        self.value = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_element = QueueElement(value)
        
        # Jeśli kolejka jest pusta
        if self.head == None:
            self.head = new_element
            self.tail = new_element
        else:
            self.tail.previous = new_element
            self.tail = new_element

    def pop(self):

        if self.head == None:
            raise ValueError("Queue empty")

        result = self.head
        self.head = result.previous

        return result.value

    @property
    def is_empty(self):
        return self.head == None


class StackElement:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.stack_top = None

    def push(self, value):
        new_element = StackElement(value)

        if self.stack_top == None:
            self.stack_top = new_element
        
        else:
            new_element.next = self.stack_top
            self.stack_top = new_element

    def pop(self):
        if self.stack_top == None:
            raise ValueError("Stack is empty")

        result = self.stack_top
        self.stack_top = result.next

        return result.value
        
    @property
    def is_empty(self):
        return self.stack_top == None
