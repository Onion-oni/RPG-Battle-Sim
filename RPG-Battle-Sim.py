#at least 1 pc and 1 npc
#need hp, hit, attack, damage, ac, level, modifier
    #user inptus can determine these
#turn order
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
