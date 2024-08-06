"""--- LINKED LIST ---

version: 1.0
author: J@nu$
date: 03.aug.2024
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next_link = None

class Llist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # définir la méthode magique __str__() pour afficher la liste chaînée
    def __str__(self) -> str:
        return f"[{', '.join((str(element) for element in self.list_from_llist()))}]"

    # définir la méthode magique __len__() pour renvoyer le nombre d'éléments contenus dans la liste chaînée
    def __len__(self) -> int:
        return len(self.list_from_llist())

    # définir la méthode print_list_from_llist() qui permet de transformer la liste chaînée en liste standard
    def list_from_llist(self):
        llist = []
        current_node = self.head
        while current_node is not None:
            # llist.append(str(current_node.value))
            llist.append(current_node.value)
            # print(llist)  # print de vérification
            current_node = current_node.next_link
        return llist

    # définir la méthode append() pour ajouter un élément à la fin de la liste
    def append(self, value: int|str) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # current_node = self.head
            # while current_node.next_link is not None:
            #     current_node = current_node.next_link
            # current_node.next_link = new_node
            last_node = self.tail
            self.tail = new_node
            last_node.next_link = self.tail

    # définir la méthode remove_at() qui retire un élément à l'index donné
    def remove_at(self, index: int) -> None:
        if self.head is None:
            print("Linked list empty. Cannot remove an element.")
        elif index >= self.__len__():
            print("List index out of range.")
        else:
            current_node = self.head
            index_count = 0
            while current_node.next_link is not None and index_count < index:
                previous_node = current_node
                current_node = current_node.next_link
                index_count += 1
            if current_node == self.head:
                self.head = self.tail = None
            elif current_node == self.tail:
                previous_node.next_link = None
                self.tail = previous_node
            else:
                previous_node.next_link = current_node.next_link
            del current_node

    # définir la méthode insert() qui insère un élément à l'index donné

    # définir la méthode contains() qui vérifie que value est présent dans la liste

    # définir la méthode index_of() qui renvoie l'index de la première valeur rencontrée

    # définir la méthode at_index()) qui renvoie la valeur à l'index donné

    # définir la méthode is_unique() qui vérifie que la liste ne contient pas de doublons

    # définir la méthode reversed() qui inverse le sens de la liste chaînée


if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(30)
    node3 = Node(50)
    llist = Llist()
    print(llist)
    llist.remove_at(3)
    print(llist)

    # llist.head = node1
    # node1.next_link = node2
    # node2.next_link = node3

    # print(node1.value)
    # print(node1.next_link)
    # print(llist.head.value)
    # print(llist.head.next_link)

    llist.append(node1.value)
    print(llist.tail.value)
    llist.append(node2.value)
    print(llist.tail.value)
    llist.append(node3.value)
    print(llist.tail.value)
    print(llist)
    print(len(llist))
    # llist.remove_at(0)
    # print(llist)
    # print(llist.head)
    # llist.remove_at(1)
    # print(llist.tail.value)
    # print(llist)
    llist.remove_at(2)
    print(llist)
    print(llist.tail.value)
    # llist.remove_at(3)
    # print(llist)
    # llist.remove_at(4)
    # print(llist)