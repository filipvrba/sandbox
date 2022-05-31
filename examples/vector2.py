#!/usr/bin/python

class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def __add__( self, value ):
        self.x += value.x
        self.y += value.y
        return self
    

    def __sub__( self, value ):
        self.x -= value.x
        self.y -= value.y
        return self


    def __name__(self):
        return type(self).__name__


    def __str__( self ):
        return f"{self.__name__()}( x: {self.x}, y: {self.y} )"


    def __len__( self ):
        return self.x + self.y


def main():
    def scenario():
        test = Vector2(1, 1)
        test_2 = Vector2()

        print(test_2)
        test_2 += test
        print(test_2, len(test_2))
        test_2 -= test
        print(test_2)
    
    scenario()


if __name__ == "__main__":
    main()
