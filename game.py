from player import Player
from orc import Orc
from goblin import Goblin
import random
from random import randint

random_weapon=random.choices(["Knife", "axe", "sword"])
weapon=random_weapon[0]
p_power=random.randint(5,10)
p_speed=random.randint(5,10)
p_armor_rating=random.randint(5,15)
profession=random.choice(["Warrior", "healer"])
type_0f_monster=random.choice(["orc","goblin"])
orc_armor_rating=random.randint(2,8)
orc_speed=random.randint(0,5)
orc_power=random.randint(10,15)
random_monster=random.choice([Orc("Bill","orc",50,orc_speed,orc_power,orc_armor_rating,weapon),Goblin("Johnny","goblin",20,p_speed,p_power,1,weapon)])
class Game:
    def __init__(self):
        pass
    
    
    @staticmethod
    def show_menu():
        while True:
            players_choice=input("battle or exit")
            if players_choice=="battle":
                return True
            elif players_choice=="exit":
                return False
            else:
                print("not valed")
                continue
            
    def create_player(self):
        name=input("enter your name")
        player=Player(name,50,p_speed,p_power,p_armor_rating,profession)
        player.add_hp()
        player.add_power()
        print( player)
        
    def choose_random_monster(self):
        monster=random_monster
        print(monster)
        return monster
    
    def start(self):
        self.menu=self.show_menu()
        if self.menu==True:
            self.player=self.create_player()
            self.monster=self.choose_random_monster()
            return self.player,self.monster
        else:
            print("god bey")





a=Game()
a.start()
# a.show_menu(a)

# monster=type_0f_monster
# print(a.choose_random_monster(a))
# print(a.create_player(a))    
    
        
    
    
    

