"""--- LINKED LIST ---

version: 1.0
author: J@nu$
date: 03.aug.2024
"""

# Définition de la classe Node() qui permet de créer les noeuds de la liste chaînée
class Node:
    def __init__(self, value) -> None:
        self.value = value  # Chaque noeud contient une valeur
        self.next_link = None  # Et un lien vers le noeud suivant

# Définition de la classe Llist() qui permet de générer la liste chaînée à partir de la classe Node()
class Llist:
    def __init__(self) -> None:
        self.head = None  # La chaîne contient une 'tête' qui pointe vers le 1er élément de la liste
        self.tail = None  # Et une 'queue' qui point vers le dernier élément de la liste

    # définir la méthode magique __str__() pour afficher la liste chaînée
    def __str__(self) -> str:
        return f"[{', '.join((str(element) for element in self.list_from_llist()))}]"

    # définir la méthode magique __len__() pour renvoyer le nombre d'éléments contenus dans la liste chaînée
    def __len__(self) -> int:
        return len(self.list_from_llist())  # récupération de la longueur de la liste standard générée à partir de la liste chaînée

    # définir la méthode list_from_llist() qui permet de transformer la liste chaînée en liste standard
    def list_from_llist(self) -> list:
        """Permet de transformer la liste chaînée en liste standard.

        Returns:
            list: liste standard contenant les valeurs des noeuds de la liste chaînée
        """
        llist = []
        # Parcourir tous les noeuds de la liste chaînée
        current_node = self.head  # En affectant le noeud en cours au départ sur la tête de la liste
        # Récupérer une par une les valeurs de chaque noeud dans une liste
        while current_node is not None:  # Tant qu'on n'arrive pas à la fin de la liste
            llist.append(current_node.value)
            # print(llist)  # print de vérification
            current_node = current_node.next_link  # Passer au noeud suivant
        return llist

    # définir la méthode append() pour ajouter un élément à la fin de la liste
    def append(self, value: int|str) -> None:
        """Permet d'ajouter un élément à la fin de la liste chaînée.

        Args:
            value (int | str): valeur à donner au noeud ajouté
        """
        # Créer le nouveau noeud à ajouter avec sa valeur à partir de la classe Node()
        new_node = Node(value)
        # Cas où la liste est vide, la tête et la queue de la liste pointent vers le nouveau noeud
        if self.head is None:
            self.head = self.tail = new_node
        # Cas où la liste n'est pas vide
        else:
            # current_node = self.head
            # while current_node.next_link is not None:
            #     current_node = current_node.next_link
            # current_node.next_link = new_node
            last_node = self.tail  # Récupération du dernier noeud de la liste à partir de la 'queue'
            self.tail = new_node  # La 'queue' devient le nouveau noeud ajouté à la fin de la liste
            last_node.next_link = self.tail  # Relier l'ancien dernier noeud à la nouvelle 'queue' de la liste

    # définir la méthode remove_at() qui retire un élément à l'index donné
    def remove_at(self, index: int) -> None:
        """Permer de retirer un élément de la liste chaînée à l'index donné

        Args:
            index (int): index souhaité pour retirer un élément de la liste
        """
        # Cas où la liste est vide, indiquer un message le précisant
        if self.head is None:
            print("Linked list empty. Cannot remove an element.")
        # Cas où l'index est en dehors de la range de la liste, indiquer un message le précisant
        elif index >= self.__len__():
            print("List index out of range.")
        # Autres cas
        else:
            # Parcourir tous les noeuds de la liste chaînée jusqu'à l'index indiqué
            current_node = self.head  # En affectant le noeud en cours au départ sur la tête de la liste
            index_count = 0  # Et initier un compteur d'index
            # Tant qu'on n'arrive pas à l'index indiqué ni à la fin de la liste
            while current_node.next_link is not None and index_count < index:
                previous_node = current_node  # Le noeud courant devient le noeud précédant
                current_node = current_node.next_link  # Puis le noeud courant devient le noeud suivant
                index_count += 1  # On avance dans l'index

            # Une fois à l'index indiqué
            # Cas où il n'y a qu'un élément dans la liste
            if current_node == self.head and current_node == self.tail:  # A VOIR SI POSSIBLE DE REDUIRE CETTE LIGNE DE CODE
                # La liste devient vide : la 'tête' et la 'queue' retrouvent leur valeur par défaut 'None'
                self.head = self.tail = None
                # print("OK1")  # print de test
            # Cas où on est à l'index 0 et que la liste contient > 1 élément
            elif current_node == self.head:
                self.head = current_node.next_link  # La 'tête' pointe désormais vers le noeud suivant le 1er noeud de la liste
                # print("OK2")  # print de test
            # Cas où l'index correspond au dernier élément de la liste
            elif current_node == self.tail:
                previous_node.next_link = None  # Le noeud précédent ne pointe vers plus rien ('None')
                self.tail = previous_node  # La 'queue' pointe désormais vers le noeud précédent
                # print("OK3")  # print de test
            # Autres cas
            else:
                # Le noeud précédent va pointer désormais vers le noeud correspondant au noeud suivant de celui qui était à l'index donné
                previous_node.next_link = current_node.next_link
                # print("OK4")  # print de test
            del current_node  # Suppression du noeud à l'index donné

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
    # print(llist)
    # llist.remove_at(3)
    # print(llist)

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
    # llist.append(node3.value)
    # print(llist.tail.value)
    print(llist)
    print(len(llist))
    llist.remove_at(0)
    print(llist)
    print(llist.head.value)
    print(llist.tail.value)
    # llist.remove_at(1)
    # print(llist.head.value)
    # print(llist.tail.value)
    # print(llist)
    # llist.remove_at(2)
    # print(llist)
    # print(llist.head.value)
    # print(llist.tail.value)
    # llist.remove_at(3)
    # print(llist)
    # llist.remove_at(4)
    # print(llist)