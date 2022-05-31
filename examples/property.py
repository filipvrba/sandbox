#!/usr/bin/python

class Vector2():
    def __init__( self, x = 0, y = 0 ):
        """Class have property attribute"""

        self.x = x
        self.y = y
    

    @property  # Decorator
    def x(self):
        print('x get')
        return self._x


    @x.setter  # Decorator
    def x(self, value):
        print('x set')
        self._x = value


def main():
    vec2 = Vector2()
    print(f"x {vec2.x}")


if __name__ == '__main__':
    main()
