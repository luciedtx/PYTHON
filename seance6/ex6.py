#  Les test unitaires
class Calculatrice :
    @staticmethod
    def addition(x,y):
        return x+y
    def soustraction(x,y):
        return x-y
    def multiplication(x,y):
        return x*y
    def division(x,y):
        try :
            x/y
        except ValueError:
            print("impossible de diviser par 0")
        return x/y