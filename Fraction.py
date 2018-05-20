import copy
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        
        top_copy = copy.copy(top)
        bottom_copy = copy.copy(bottom)

        if top > bottom:
            m = top_copy
            n = bottom_copy
        else:
            m = bottom_copy
            n = top_copy
        div = gcd(m,n)

        self.num = top / div
        self.den = bottom / div

    def show(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self,other_fraction):
        new_num = (self.num*other_fraction.den)+(self.den*other_fraction.num)
        new_den = self.den*other_fraction.den

        return Fraction(new_num,new_den)

inst = Fraction(3,5)

print(inst + inst)
#exec: python C:\Users\Mbwenga\Documents\ML\Python\Fraction.py