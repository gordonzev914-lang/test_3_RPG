class Goblin:
    def __init__(self,name,type,hp,speed,power,armor_rating,weapon):
        self.name=name
        self.type=type
        self.hp=hp
        self.speed=speed
        self.power=power
        self.armor_rating=armor_rating
        self.weapon=weapon
    def __str__(self):
        return f"name {self.name},type {self.type},hp {self.hp},speed {self.speed},power {self.power}, armor_rating{self.armor_rating},weapon {self.weapon}"
    def speak(self):
        return print(f"{self.name} I will eat you ")

    def attack(self):
        pass   