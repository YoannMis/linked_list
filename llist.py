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
        self.end = None

    # définir la méthode magique __str__() pour afficher la liste chaînée
    def __str__(self) -> str:
        return self.print_llist()

    # définir la méthode magique __len__() pour renvoyer le nombre d'éléments contenus dans la liste chaînée
    def __len__(self) -> int:
        pass

    # définir la méthode print_llist() qui permet de récupérer la llist sous forme de str afin de pouvoir l'imprimer
    def print_llist(self):
        llist = []
        current_node = self.head
        while current_node is not None:
            llist.append(str(current_node.value))
            # print(llist)  # print de vérification
            current_node = current_node.next_link
        return f"[{', '.join(llist)}]"

    # définir la méthode append() pour ajouter un élément à la fin de la liste

    # définir la méthode remove_at() qui retire un élément à l'index donné

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

    llist.head = node1
    node1.next_link = node2
    node2.next_link = node3

    # print(node1.value)
    # print(node1.next_link)
    # print(llist.head.value)
    # print(llist.head.next_link)
    print(llist)