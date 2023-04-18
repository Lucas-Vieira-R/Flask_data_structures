class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    # nessa lista, teremos atributos do primeiro e do ultimo Node da lista, para facilitar a inserção nas extremidades
    def __init__(self):
        self.head = None
        self.last_node = None

    # Representação visual da lista
    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            if node.next_node is None:
                ll_string += " None"
            node = node.next_node
        print(ll_string)

    # Criaremos metodos que nos permita adicionar Nodes no início e no final da lista:

    def insert_beginning(self,data):
        if self.head is None:
            self.head = Node(data,None)
            self.last_node = self.head
        new_node = Node(data,self.head)
        self.head = new_node
    
    def insert_end(self,data):
        if self.head is None:
            self.insert_beginning(data)

        self.last_node.next_node = Node(data,None)
        self.last_node = self.last_node.next_node


    # método para passar a lista linkada para um array, a fim de retornar um json na API:

    def to_array(self):
        arr = []
        if self.head is None:
            return arr
        node = self.head
        while node.next_node:
            arr.append(node.data)
            node = node.next_node
        return arr
    
    #metodo que returna um nó com id específico
    def get_user_by_id(self,user_id):
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        
