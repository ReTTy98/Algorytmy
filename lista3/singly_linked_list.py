import unittest

class SinglyLinkedListElement:
    def __init__(self, value):
        self.next = None
        self.value = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_element = SinglyLinkedListElement(value)
        if self.head == None:
            self.head = new_element
            return
        else:
            new_element.next = self.head
            self.head = new_element

    def pop(self):
        if self.head == None:
            return None

        result = self.head
        self.head = self.head.next

        return result.value

    def print(self):
        if self.head == None:
            return

        current = self.head
        while current.next != None:
            print(current.value)
            current = current.next

    def __len__(self):
        length = 0

        if self.head == None:
                    return length
 
        current = self.head
        length += 1
        
        while current.next != None:
            length += 1
            current = current.next

        return length


class TestSinglyLinkedList(unittest.TestCase):
    def test_add_elements(self):
        mylist = SinglyLinkedList()

        mylist.add(1)

        assert mylist.head.value == 1


    def test_list_len_empty(self):
        mylist = SinglyLinkedList()
        assert len(mylist) == 0


    def test_list_len_filled(self):
        mylist = SinglyLinkedList()

        mylist.add(1)
        mylist.add(2)
        mylist.add(3)

        assert len(mylist) == 3


    def test_list_pop(self):
        mylist = SinglyLinkedList()

        mylist.add(1)
        mylist.add(2)
        mylist.add(3)

        assert 3 == mylist.pop()
        assert 2 == len(mylist)
        
        assert 2 == mylist.pop()
        assert 1 == len(mylist)
        
        assert 1 == mylist.pop()
        assert 0 == len(mylist)

        assert None == mylist.pop()
        assert 0 == len(mylist)
        

if __name__ == '__main__':
    unittest.main()





