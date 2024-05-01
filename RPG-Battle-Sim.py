#at least 1 pc and 1 npc
#need hp, hit, attack, damage, ac, level, modifier
    #user inputs can determine these
class Player(name):

    def __init__(self):
#Eventually will have capability to validate user inputs as being integers
        level = input ("What level is this character? (1-20): ")
        hitpoints = input("How many hitpoints does this character have?: ")
        armor = input("What is this character's armor class?: ")

        self.level = int(level)
        self.hitpoints = int(hitpoints)
        self.armor = int(armor)
        self.attack = 0
        
#turn order
    #rolling a d20 determines initiative but I will decide this while testing
#game logic is to have the two players fight until hp is <= 0
#need dice for hit and damage (d20, d12, d8, d6, d4)
    #d(x) = dice_maker()
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d8 = [1,2,3,4,5,6,7,8]
d6 = [1,2,3,4,5,6]
d4 = [1,2,3,4]
def dice_maker():
    max = input('Please enter the number of sides: ' )
    x = int(max) + 1
    d = []
    for n in range(1,x):
        d.append(n)
