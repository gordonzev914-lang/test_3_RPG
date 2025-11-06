class Player:
    def __init__(self,name,hp,speed,power,armor_rating,profession):
        self.name=name
        self.hp=hp
        self.speed=speed
        self.power=power
        self.armor_rating=armor_rating
        self.profession=profession
    def __str__(self):
        return f"name {self.name}, hp {self.hp}, speed {self.speed}, power {self.power}, armor_rating {self.armor_rating}, profession {self.profession} "
            
    
    
    
    def add_hp(self):
        if self.profession=="healer":
            self.hp+=10

    def add_power(self):
        if self.profession=="Warrior":
            self.power+=2        


    
    
    
    def speak(self):
        return f"{self.name} They will die "

    def attack(self):
        pass    
        
