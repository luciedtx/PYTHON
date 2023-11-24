
def addition(x,y):
    """somme de deux nombres

    Args:
        x (float): 1er nombre a additioner
        y (float): 2eme nombre a additioner

    Returns:
        float: resultat de l'addition
    """
    return x+y

# classes : contient attributs et methodes
class Rectangle :
    longueur= 10
    largeur= 5
    def aire(self,longueur,largeur):
        return self.longueur*self.largeur


# print(f"Mon rectangle a pour longueur {Rectangle.longueur} et pour largeur {Rectangle.largeur} et l'aire est {Rectangle.aire(Rectangle.longueur,Rectangle.largeur)}.")

premier_rectangle= Rectangle()
premier_rectangle.longueur= 20
premier_rectangle.largeur= 10
print(f"Mon rectangle a pour longueur {premier_rectangle.longueur} et pour largeur {premier_rectangle.largeur} et l'aire est {premier_rectangle.aire(premier_rectangle.longueur,premier_rectangle.largeur)}.")

deuxieme_rectangle= Rectangle()
deuxieme_rectangle.longueur= 40
deuxieme_rectangle.largeur= 20
print(f"Mon rectangle a pour longueur {deuxieme_rectangle.longueur} et pour largeur {deuxieme_rectangle.largeur} et l'aire est {deuxieme_rectangle.aire(deuxieme_rectangle.longueur,deuxieme_rectangle.largeur)}.")


