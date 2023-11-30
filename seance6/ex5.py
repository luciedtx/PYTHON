from math import*
class Forme :
    def __innit__(self, L, l, pi, R ) :
        self.L= L
        self.l= l
        self.pi= pi
        self.R= R
    def aire(cls, L, l, pi, R):
        cls.aire=L*l
        

class Cercle(Forme) :
    def __init__(self, L, l , pi , R):
        Forme.__init__(self, L, l, pi, R)

class Rectangle(Forme):
    def __init__(self, L, l, pi, R):
        Forme.__init__(self, L, l, pi, R)


rect= Rectangle()
rect.aire()