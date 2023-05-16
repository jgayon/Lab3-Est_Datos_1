class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, name, score):
        new_node = Node(name, score)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_scores(self):
        current = self.head
        while current:
            print(f"Name: {current.name}, Score: {current.score}")
            current = current.next
    def sort_scores(self):
        sorted_head = None

        while self.head:
            current = self.head
            max_node = self.head
            prev_max = None

            while current.next:
                if current.next.score > max_node.score:
                    max_node = current.next
                    prev_max = current
                current = current.next

            if prev_max:
                prev_max.next = max_node.next
            else:
                self.head = max_node.next

            max_node.next = sorted_head
            sorted_head = max_node

        self.head = sorted_head
    def save_scores(self, filename):
        with open(filename, "w") as file:
            current = self.head
            while current:
                file.write(f"{current.name},{current.score}\n")
                current = current.next

    @staticmethod
    def load_scores(filename):
        score_list = LinkedList()
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                name, score = line.strip().split(",")
                score_list.add_node(name, int(score))
        return score_list


score_list = LinkedList()
name = "Juan"
score = 100
score_list.add_node(name, score)
name = "Andres"
score = 120
score_list.add_node(name, score)
name = "Miguel"
score = 10
score_list.add_node(name, score)
name = "Felipe"
score = 110
score_list.add_node(name, score)
name = "luis"
score = 300
score_list.add_node(name, score)
score_list.sort_scores()
score_list.display_scores()
score_list.save_scores("puntajes.txt")