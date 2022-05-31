#!/usr/bin/python
import time


class Print:
    def p_now_attacking( self, to_name ):
        print( f"Now {self.__str__()} is attacking to {to_name}" )
    

    def p_won(self):
        print( f"{self.__str__()} won!" )
    

    def p_has_life(self):
        print(f"{self.__str__()} has {self.life} life" )
    

    def p_no_death(self):
        print( "Nobody is death." )


class Fighter( Print ):
    def __init__(self, name, life, defense, damage) -> None:
        self.name = name
        self.life = life
        self.defense = defense
        self.damage = damage

    
    def attack( self, fighter ):
        fighter.life -= self.damage - fighter.defense
        pass


    def is_death(self):
        if self.life <= 0:
            return True

        self.p_no_death()
        return False


    def battle_with( self, fighter_2 ):
        self.p_now_attacking(fighter_2)
        time.sleep(2)
        self.attack( fighter_2 )

        if fighter_2.is_death():
            self.p_won()
            raise

        fighter_2.p_has_life()
        time.sleep(2)


    def __str__(self) -> str:
        return self.name


def main():
    fighter_1 = Fighter( 'fighter_1', 100, 20, 35 )
    fighter_2 = Fighter( 'fighter_2', 120, 5, 30 )

    while True:
        try:
            fighter_1.battle_with( fighter_2 )
            fighter_2.battle_with( fighter_1 )
        except:
            break


if __name__ == '__main__':
    main()
