
def s1():
    print("Simple s1")

def simple_fonction():
    for i in range(20):
        print(i)

class simple_c1:

    def __init__(self, a1=4, a2=9):
        self.a1 = a1
        self.a2 = a2

    def fonct1(self):
        for i in range(self.a1):
            print("Test d'une simple fonction")

def simple_c(a1=4, a2=9):
    s1 = simple_c1(a1=a1, a2=a2)
    return s1

