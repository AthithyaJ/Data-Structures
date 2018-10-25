class Node:
    def __init__(self, cargo):
        self.cargo = cargo
        self.left = None
        self.right = None


def check(n):
    if n is 'y':
        return True
    elif n is 'n':
        return False


def animal_tree():
    ans = input('Are you thinking of an animal?')
    if check(ans):
        tree = Node('animal')
        x = input('Can it fly?')
        if check(x):
            ba = Node('bird')
            tree.left = ba
        else:
            ma = Node('Land Animal')
            tree.right = ma

        pro = input('Can the animal bark?')
        if check(pro):
            do = Node('dog')
            ma.left = do
            n = input('Is it a dog?')
            check(n)
        else:
            ca = Node('cat')
            ma.right = ca


animal_tree()
