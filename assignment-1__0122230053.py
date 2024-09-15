class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function 1: Find the length of the linked list
    def find_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Function 2: Find the middle element and delete it
    def delete_middle(self):
        length = self.find_length()
        if length == 0:
            print("List is empty.")
            return
        
        mid = length // 2
        current = self.head

        if mid == 0:
            self.head = current.next  # Deleting the only element
        else:
            prev = None
            for _ in range(mid):
                prev = current
                current = current.next
            if prev:
                prev.next = current.next

        print(f"Deleted middle element: {current.data}")

    # Function 3: Exchange the first and last element
    def exchange_first_last(self):
        if self.head is None or self.head.next is None:
            return  # Empty list or single element

        first = self.head
        current = self.head
        prev = None

        # Traverse to the last node
        while current.next:
            prev = current
            current = current.next

        # Swap first and last node
        last = current
        if prev:
            prev.next = first  # Set second last node's next to first node

        last.next, first.next = first.next, None  # Swap connections
        self.head = last  # Set new head to last node

    # Function 4: Display elements in reverse order (without modifying the list)
    def display_reverse(self, node):
        if node is None:
            return
        self.display_reverse(node.next)
        print(node.data, end=" ")

    # Function 5: Find and display the smallest element in the list
    def find_smallest(self):
        if self.head is None:
            print("List is empty.")
            return

        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next

        print(f"Smallest element: {min_val}")

    # Helper functions for insertion and deletion
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        prev = None

        if current and current.data == key:
            self.head = current.next
            return

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    # Helper function to print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)

print("Original list:")
ll.print_list()

# 1. Find length
print(f"Length of the list: {ll.find_length()}")

# 2. Delete middle element
ll.delete_middle()
print("After deleting middle element:")
ll.print_list()

# 3. Exchange first and last
ll.exchange_first_last()
print("After exchanging first and last:")
ll.print_list()

# 4. Display in reverse order
print("List in reverse order:")
ll.display_reverse(ll.head)
print()

# 5. Find smallest element
ll.find_smallest()
