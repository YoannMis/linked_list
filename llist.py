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
        self.llist_length = 0  # Longueur de la liste chaînée
    
    # Définir la méthode magique __str__() pour afficher la liste chaînée
    def __str__(self) -> str:
        """Permet d'afficher sous forme de str l'instance de la class.

        Returns:
            str: str à afficher
        """ 
        return f"[{', '.join(str(element) for element in self.list_from_llist())}]"

    # Définir la méthode magique __len__() pour renvoyer le nombre d'éléments contenus dans la liste chaînée
    def __len__(self) -> int:
        """Permet de renvoyer la longueur de la liste chaînée créée à partir de la class.

        Returns:
            int: longueur de la liste chaînée
        """
        return self.llist_length

    # Définir la méthode append() pour ajouter un élément à la fin de la liste
    def append(self, value: int|str) -> None:
        """Permet d'ajouter un élément à la fin de la liste chaînée.

        Args:
            value (int | str): valeur à donner au noeud ajouté
        """
        # Créer le nouveau noeud à ajouter avec sa valeur à partir de la classe Node()
        new_node = Node(value)
        # Cas où la liste est vide, la 'tête' et la 'queue' de la liste deviennent le nouveau noeud
        if not self.head:
            self.head = self.tail = new_node
        # Cas où la liste n'est pas vide
        else:
            # La 'queue' va pointer vers le nouveau noeud ajouté puis devenir à nouveau le dernier noeud de la liste  
            self.tail.next_link = self.tail = new_node
        
        self.llist_length += 1  # On augmente la longueur de la liste chaînée de 1

    # Définir la méthode at_index() qui renvoie la valeur à l'index donné
    def at_index(self, index: int) -> int|str:
        """Renvoie la valeur dans la liste chaînée correspondant à l'index donné.

        Args:
            index (int): index donné

        Returns:
            int|str: la valeur correspondante
        """
        # Cas où l'index est en dehors de la range de la liste, indiquer un message le précisant
        if index >= self.llist_length:
            print("List index out of range.")
        # Vérifier d'abord si l'index correspond à la queue de la liste chaînée
        elif index == self.llist_length-1:
            return self.tail.value
        # Sinon parcourir la liste chaînée jusqu'à l'index donné
        else:
            current_node = self.head  # On part de la 'tête'
            for _ in range(index):
                current_node = current_node.next_link  # On passe au noeud suivant
            return current_node.value  # On récupère la valeur du noeud

    # Définir la méthode contains() qui vérifie que value est présent dans la liste
    def contains(self, value: int|str) -> bool:
        """Vérifie que la valeur donnée en argument est présente dans la liste chaînée.

        Args:
            value (int | str): valeur à vérifier

        Returns:
            bool: True si la valeur est présente, False sinon
        """
        # Vérifier si la valeur est présente dans la liste chaînée grâce à la méthode index_of()
        return self.index_of(value) >= 0

    # Définir la méthode index_of() qui renvoie l'index de la première valeur rencontrée
    def index_of(self, value: int|str) -> int:
        """Renvoie l'index de la première valeur rencontrée.

        Args:
            value (int | str): valeur à trouver

        Returns:
            int: index correspondant à la valeur cherchée si elle existe, sinon -1
        """
        # Parcourir la liste chaînée et vérifier si la valeur est contenue dans la liste chaînée
        current_node = self.head  # En affectant le noeud en cours au départ sur la 'tête' de la liste
        index = 0  # Et en partant de l'index 0
        while current_node:
            if current_node.value == value:
                return index  # Retourner l'index si la valeur est trouvée
            current_node = current_node.next_link  # Sinon on passe au noeud suivant
            index += 1  # Et à l'index suivant
        
        # Si après avoir parcouru toute la liste chaînée la valeur recherchée n'est pas retrouvée, alors retourner -1
        return -1

    # Définir la méthode insert() qui insère un élément à l'index donné
    def insert(self, index: int, value : int|str) -> None:
        """Permet d'insérer un élément à l'index donné.

        Args:
            index (int): index souhaité pour ajouter un élément dans la liste
            value (int | str): valeur à attribuer au nouvel élément inséré
        """
        # Cas où l'index est en dehors de la range de la liste, indiquer un message le précisant
        if index >= self.llist_length:
            print("List index out of range.")
        # Autres cas
        else:
            # Parcourir tous les noeuds jusqu'au noeud situé à l'index précédent l'index indiqué
            current_node = self.head  # En affectant le noeud en cours au départ sur la tête de la liste
            for _ in range(index-1):
                current_node = current_node.next_link  # On passe au noeud suivant

            # Une fois arrivé vérifier les différents cas possibles
            # Créer le nouveau noeud à insérer avec sa valeur à partir de la classe Node()
            new_node = Node(value)
            match index:
                # Cas où on est à l'index 0
                case 0:
                    new_node.next_link = self.head  # Le nouveau noeud inséré pointe vers l'ancien noeud qui était à l'index 0 (soit la 'tête')
                    self.head = new_node  # La 'tête' devient le nouveau noeud inséré
                # Autres cas
                case _:
                    new_node.next_link = current_node.next_link  # Le nouveau noeud inséré va pointer vers le noeud qui était à l'index donné
                    current_node.next_link = new_node  # Et le noeud qui était à l'index donné -1 va pointer vers le nouveau noeud inséré

            self.llist_length += 1  # On augmente la longueur de la liste chaînée de 1

    # Définir la méthode is_unique() qui vérifie que la liste ne contient pas de doublons
    def is_unique(self) -> bool:
        """Vérifie que la liste chaînée ne contient pas de doublons.

        Returns:
            bool: True s'il n'y a pas de doublons dans la liste, False sinon
        """
        # Initialiser une liste vide où stocker les valeurs des éléments de la liste chaînée tant qu'il n'y a pas de doublons
        elements = []
        current_node = self.head  # Partir de la 'tête' pour parcourir la liste chaînée
        # Parcourir la liste chaînée en vérifiant que l'élément n'est pas présent en doublon
        while current_node != self.tail and current_node.value not in elements:
            # Vérifier d'abord si l'élément n'est pas égal à la 'queue' pour ne pas avoir à parcourir toute la liste chaînée
            if current_node.value == self.tail.value:
                return False
            # Sinon stocker la valeur de l'élément dans la liste 'elements' et passer au suivant
            elements.append(current_node.value)
            current_node = current_node.next_link
        
        return current_node.value not in elements

    # Définir la méthode list_from_llist() qui permet de transformer la liste chaînée en liste standard
    def list_from_llist(self) -> list:
        """Permet de transformer la liste chaînée en liste standard.

        Returns:
            list: liste standard contenant les valeurs des noeuds de la liste chaînée
        """
        std_list = []
        # Parcourir tous les noeuds de la liste chaînée
        current_node = self.head  # En affectant le noeud en cours au départ sur la tête de la liste
        # Récupérer une par une les valeurs de chaque noeud dans une liste
        while current_node:  # Tant qu'on n'arrive pas à la fin de la liste
            std_list.append(current_node.value)
            current_node = current_node.next_link  # Passer au noeud suivant
        return std_list

    # Définir la méthode remove_at() qui retire un élément à l'index donné
    def remove_at(self, index: int) -> None:
        """Permer de retirer un élément de la liste chaînée à l'index donné.

        Args:
            index (int): index souhaité pour retirer un élément de la liste
        """
        # Cas où l'index est en dehors de la range de la liste, indiquer un message le précisant
        if index >= self.llist_length:
            print("List index out of range.")
        # Cas où il n'y a qu'un élément dans la liste
        elif self.head == self.tail:
            # La liste devient vide : la 'tête' et la 'queue' retrouvent leur valeur par défaut 'None'
            self.head = self.tail = None
            self.llist_length = 0  # la longueur de la liste chaînée retombe à 0
        # Autres cas
        else:
            # Parcourir tous les noeuds jusqu'au noeud situé à l'index précédent l'index indiqué
            current_node = self.head  # En affectant le noeud en cours au départ sur la tête de la liste
            for _ in range(index-1):
                current_node = current_node.next_link  # On passe au noeud suivant

            # Une fois arrivé vérifier les différents cas possibles
            # Cas où on est à l'index 0 et que la liste contient > 1 élément
            if index == 0:
                self.head = current_node.next_link  # La 'tête' devient désormais le noeud suivant le 1er noeud de la liste
            # Cas où l'index correspond au dernier élément de la liste
            elif index == self.llist_length-1:
                current_node.next_link = None  # Le noeud à l'index donné -1 ne pointe vers plus rien ('None')
                self.tail = current_node  # La 'queue' devient désormais le noeud à l'index donné -1
            # Autres cas
            else:
                # Le noeud à l'index donné -1 va pointer désormais vers le noeud correspondant au noeud qui était à l'index donné +1
                current_node.next_link = current_node.next_link.next_link

            self.llist_length -= 1  # On diminue de 1 la longueur de la liste chaînée

    # Définir la méthode reversed() qui inverse le sens de la liste chaînée
    def reversed(self) -> None:
        """Permet d'inverser le sens de la liste chaînée.

        """
        # Sauvegarder la 'queue' de la liste chaînée en tant que nouvelle 'tête' pour plus tard
        self.tail = self.head
        # Parcourir la liste chaînée afin de récupérer chaque noeud
        current_node = self.head.next_link  # En partant du 2eme noeud de la liste
        while current_node:
            # Créer un nouveau noeud contenant la valeur du noeud en cours que l'on va insérer en 'tête' de la liste chaînée
            new_node = Node(current_node.value)
            new_node.next_link = self.head  # Le nouveau noeud inséré pointe vers l'ancien noeud qui était à l'index 0 (soit la 'tête')
            self.head = new_node  # La 'tête' devient le nouveau noeud inséré
            current_node = current_node.next_link  # On passe au noeud suivant

        # On coupe la 'queue' du lien qui la reliait aux anciens noeuds pour ne garder que les noeuds de la liste dans l'ordre inverse
        self.tail.next_link = None

if __name__ == "__main__":
    # llist = Llist()
    # print(llist)
    # print(len(llist))
    
    # ---Test append()---
    # llist.append(10)
    # print(llist.head.value)
    # print(llist.tail.value)
    # print(len(llist))
    # llist.append(20)
    # print(llist.head.value)
    # print(llist.tail.value)
    # print(len(llist))
    # llist.append(30)
    # llist.append(40)
    # llist.append(50)
    # print(llist.head.value)
    # print(llist.tail.value)
    # print(llist)
    # print(len(llist))

    # ---Test remove()---
    # llist.remove_at(0)
    # print(llist)
    # print(llist.head)
    # print(llist.tail)
    # llist.remove_at(1)
    # print(llist.head.value)
    # print(llist.tail.value)
    # print(llist)
    # llist.remove_at(2)
    # print(llist)
    # print(llist.head.value)
    # print(llist.tail.value)
    # llist.remove_at(2)
    # print(llist)
    # print(len(llist))
    # print(len(llist))

    # ---Test insert()---
    # llist.insert(0, 50)
    # print(llist)
    # print(len(llist))
    # print(llist.head.value)
    # print(llist.tail.value)
    # llist.insert(1, 50)
    # print(llist)
    # print(llist.head.value)
    # print(llist.tail.value)
    # llist.insert(4, 100)
    # print(llist)
    # print(len(llist))
    # print(llist.head.value)
    # print(llist.tail.value)
    # llist.insert(3, 50)
    # print(len(llist))

    # ---Test at_index()---
    # print(llist.at_index(1))

    # ---Test contains()---
    # print(llist.contains(20))
    # print(llist.contains(50))
    # print(llist.contains(30))

    # --Test index_of()---
    # print(llist.index_of(20))

    # --Test is_unique()---
    # llist.append(50)
    # llist.append(50)
    # print(llist)
    # print(llist)
    # print(llist.tail.value)
    # print(llist.is_unique())

    # --Test reversed()---
    # llist.reversed()
    # print(llist)
    # print(len(llist))


    # --Test challenge example---
    llist = Llist()
    print(llist)

    llist.append(3)
    llist.append(10)
    llist.append(30)
    print(len(llist))
    print(llist)

    llist.insert(1, 50)
    print(llist)

    llist.remove_at(0)
    print(llist)

    print(llist.contains(10))
    print(llist.contains(87))

    print(llist.index_of(10))
    print(llist.index_of(87))

    print(llist.at_index(1))

    print(llist.is_unique())
    llist.append(50)
    print(llist)
    print(llist.is_unique())

    llist.append(20)
    llist.append(100)
    llist.append(80)
    print(llist)
    llist.reversed()
    print(llist)