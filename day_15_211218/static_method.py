"""
static method

annotation
starting with @
"""


class OrderSystem:
    last_no = 1

    def getNextOrderNo(self):
        print("get next no")

    @staticmethod
    def getNextOrderNoStatic():
        print("get next no - static")


#
ordsys = OrderSystem()
ordsys.getNextOrderNo()


# static method
OrderSystem.getNextOrderNoStatic()
