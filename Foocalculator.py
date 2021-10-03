import lab1 as c

class Foocalculator:
    

    #empty constructor
    def __init__(self):
         pass

    def sum(self,m,n):
        return c.sum(m,n)

    def divide(self, m, n):
        return c.divide(m,n)

cal = Foocalculator()
cal.sum(5,5)
cal.sum(3,2)
