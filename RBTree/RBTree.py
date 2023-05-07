class Node: 
    
    def __init__(self, data, tree):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1
        self.tree = tree

    def getGrandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent
    
    def getUncle(self):
        if self.parent is None:
            return None

        grandpa = self.getGrandparent()

        if grandpa is None:
            return None

        if grandpa.right == self.parent:
            return grandpa.left
        else:
            return grandpa.right
     
    def recolor(self): 
        if self.color == 0:
            self.color = 1
        else:
            self.color = 0
    

    def is_leftChild(self):
        Par = self.parent
        if Par is not None and Par.left == self:
            return 1
        return 0

    def is_rightChild(self):
        Par = self.parent
        if Par is not None and Par.right == self:
            return 1
        return 0
   
    def getRoot(self):
       return self.getRoot_()

    def insert(self, data):
       if data < self.data:
           if self.left is None:
               self.left = Node(data, self.tree)
               self.left.parent = self
               self.left.tree = self.tree
           else:
               self.left.insert(data)
           if self.left is not None:
               self.left.checks()

       elif data > self.data:
            if self.right is None:
                self.right = Node(data, self.tree)
                self.right.parent = self
                self.right.tree = self.tree
            else:
                self.right.insert(data)
            if self.right is not None:
                    self.right.checks()

    def getMin(self):
        if self.left is None:
            return self.data 
        else:
            return self.left.getMin()

    def getMax(self):
        if self.right is None:
            return self.data
        else:
            return self.right.getMax()

    def search(self, data):

        if self is None or data == self.data:
            print(f" {self.data}.")
            return 1 
        if data < self.data:
            if self.left is not None:
                print(self.data, end = " -> ")
                return self.left.search(data)
        else:
            if self.right is not None:
                print(self.data, end = " -> ")
                return self.right.search(data)
            else: 
                return 0


    def rotateR(self):
        Parent = self.parent
        L = self.left
        self.left = L.right

        if L.right is not None:
            L.right.parent = self
        L.parent = self.parent

        if self.parent is None:
            self.tree.setRoot(L)
        elif self.is_rightChild():
            self.parent.right = L
        else:
            self.parent.left = L
        L.right = self
        self.parent = L

    def rotateL(self):
        R = self.right
        self.right = R.left
        if R.left is not None:
            R.left.parent = self
        R.parent = self.parent
        if self.parent == None:
            self.tree.setRoot(R)
        elif self.is_leftChild():
            self.parent.left = R
        else:
            self.parent.right = R
        R.left = self
        self.parent = R

    def checkC1(node):
        if node.parent is None:
            node.color = 0
            return 1
        return 0


    def checkC2(self):
        if self.parent is None:
            return 0
        uncle = self.getUncle()
        if uncle is None:
            return 0
        if uncle.color == 1:
            uncle = self.getUncle()
            uncle.recolor()

            grandpa = self.getGrandparent()
            grandpa.recolor()
        
            self.parent.recolor()
        
            return 1
        return 0

    def checkC3(self):
        if self.parent is None:
            return 0
        Uncle = self.getUncle()
        if Uncle is None:
            return 0
        if Uncle.color == 0:
            Parent = self.parent
            if self.is_rightChild() and Parent.is_leftChild():
                Parent.rotateL()

            if self.is_leftChild() and Parent.is_rightChild():
                Parent.rotateR()
                return 1
        return 0
    
   
    def checkC4(self):
        if self.parent is None:
            return 0
        Uncle = self.getUncle()
        if Uncle is None:
            return 0
        if Uncle.color == 0:
            Parent = self.parent
            Grandpa = self.getGrandparent()
            if self.is_rightChild() and Parent.is_rightChild():
                Grandpa.rotateL()

            if self.is_leftChild() and Parent.is_leftChild():
                Grandpa.rotateR()

            Parent.recolor()
            Grandpa.recolor()

            return 1
        return 0

    def checks(self):
        if self.checkC1() == 0:
            if self.checkC2() == 1:
                self.parent.checks()
            elif self.checkC3() == 1:
                self.parent.checks()
            elif self.checkC4() == 1:
                self.parent.checks()
        elif self.parent is not None:
            self.parent.checks()

    def Parc_Preorder(self):
        print(self.data, end = " ; ")
        if self.left is not None:
            self.left.Parc_Preorder()
        if self.right is not None:
            self.right.Parc_Preorder()

    def Parc_Postorder(self):
        if self.left is not None:
            self.left.Parc_Postorder()
        if self.right is not None:
            self.right.Parc_Postorder()
        print(self.data, end = " ; ")

    def Parc_Inorder(self):
        if self.left is not None:
            self.left.Parc_Inorder()
        print(self.data, end = " ; ")
        if self.right is not None:
            self.right.Parc_Inorder()


class Tree:

    def __init__(self, data):
        self.root = Node(data, tree = self)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, self)
            self.root.color = 0
        else:
            self.root.insert(data)

    def setRoot(self, node):
        self.root = node

    def getMin(self):
        if self.root is None:
            return None
        else:
            return self.root.getMin()

    def getMax(self):
        if self.root is None:
            return None
        else:
            return self.root.getMax()

    def search(self, data):
        if self.root is None:
            return 100
        else:
            return self.root.search(data)

    def getRoot():
        return self.root

    def Parc_Preorder(self):
        if self.root is not None:
            self.root.Parc_Preorder()

    def Parc_Postorder(self):
        if self.root is not None:
            self.root.Parc_Postorder()

    def Parc_Inorder(self):
        if self.root is not None:
            self.root.Parc_Inorder()



print("Hello, welcome to command center!\n")
print("Please choose what you want to do:")
ok = 0
print("  1. Insert node   |  2. Preorder Traversal  |  3. Postorder Traversal   |  4. Inorder Traversal   |  5. Get Min Value   |  6. Get Max Value   |  7. Find Value   |  8. Exit\n")

term = int(input("Your choice: "))
root = None

while term != 8:
    match term:
        case 1:
            if ok == 0:
                root = Tree(int(input("Alegeti un numar: ")))
                print("Root Inserted!\n")
                ok = 1
            else:
                root.insert(int(input("Alegeti un numar: ")))
                print("Node Inserted!\n")

        case 2:
            if root is None:
                print("  --- Atentie! Nu ati introdus niciun nod! ---\n")
            else: 
                print(" Afisarea in Preordine a Arborelui: ", end = " ")
                root.Parc_Preorder()
                print("\n")

        case 3:
            if root is None:
                print("  --- Atentie! Nu ati introdus niciun nod! ---\n")
            else: 
                print(" Afisarea in Postordine a Arborelui: ", end = " ")
                root.Parc_Postorder()
                print("\n")

        case 4:
            if root is None:
                print("  --- Atentie! Nu ati introdus niciun nod! ---\n")
            else: 
                print(" Afisarea in Inordine a Arborelui: ", end = " ")
                root.Parc_Inorder()
                print("\n")
        case 5:
            print(f" Valoarea minima introdusa este:  {root.getMin()}\n")

        case 6:
            print(f" Valoarea maxima introdusa este: {root.getMax()}\n")

        case 7:
            value = int(input(" Introduceti valoarea pe care doriti sa o cautam: "))
            print(" Drumul :", end = " ")
            response = root.search(value)
            match response:
                case 100: 
                    print("  --- Atentie! Nu ati introdus niciun nod! ---\n")
                case None:
                    print(" Nodul nu exista! \n")
                case 0:
                    print(" Nodul nu a fost gasit! \n")
                case 1:
                    print(" Nodul a fost gasit! \n")
                

        case 8:
            break

        case _:
            print("  --- Optiune Invalida ---\n")

    print("  1. Insert node   |  2. Preorder Traversal  |  3. Postorder Traversal   |  4. Inorder Traversal   |  5. Get Min Value   |  6. Get Max Value   |  7. Find Value   |  8. Exit\n")
    term = int(input("Your choice: "))

print("\nProgram ended sucessfully! Have a good day!\n")