class Node:
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode

# Os dados aqui serão um par chave, valor:
class Data:
    def __init__(self,key,value):
        self.key = key
        self.value = value

class HashTable:
    # definimod o tamanho para que o método que cria o hash não exceda o index da lista que passarmos
    def __init__(self,table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self,key):
        hash_value = 0
        for i in key:
            hash_value += ord(i) # me retorna o valor decimal do caractere
            hash_value = (hash_value*ord(i)) %self.table_size # garantimos que o hash não terá valores maior que o comprimento da lista
        return hash_value
    
    # adiciona valores na hashTable
    def add_key_value(self,key,value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key,value),None) 
        else: # caso haja colisões implementamos uma linkedList:
            node = self.hash_table[hashed_key]
            while node.nextNode:
                node = node.nextNode
            node.nextNode = Node(Data(key,value),None)
    
    # procuramos o valor de determinada chave, em O(1)
    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.nextNode is None:
                return node.data.value
            while node.nextNode:
                if key == node.data.key:
                    return node.data.value
                node = node.nextNode

            if key == node.data.key:
                return node.data.value
            
        return None
    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.nextNode:
                    while node.nextNode:
                        llist_string += ( str(node.data.key) + ":" + str(node.data.value) + "-->")
                        node = node.nextNode
                    llist_string += ( str(node.data.key) + ":" + str(node.data.value) + "--> None")
                    print(f"[{i}] {llist_string}")
                else:
                    print(f"[{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"[{i}] {val}")
        print("}")







