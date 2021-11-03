import random




def dice_roll(d):
        result = random.randint(1,d)
        return result

#Define Statgen function that rolls 4d6, drops the lowest number, and sums the remaining 3

def Statgen():
        dice = [dice_roll(6),dice_roll(6),dice_roll(6),dice_roll(6)]
        stat = []
        dice.sort()
        stat.append(dice[1])
        stat.append(dice[2])
        stat.append(dice[3])
        stat = stat[0]+stat[1]+stat[2]
        return stat
        
#Create superclass Player
class Player:
        def __init__(self):
                self.STR = Statgen()
                self.DEX = Statgen()
                self.WIS = Statgen()
                self.CHA = Statgen()
                self.MAG = Statgen()
                self.DMAG = Statgen()
                self.GK = Statgen()
                self.keeper = False
                self.ini = dice_roll(20)+self.DEX
                self.X = 0
                self.Y = 0
P1 = Player()
print(P1.STR,P1.DEX,P1.WIS,P1.CHA,P1.MAG,P1.DMAG,P1.GK)
                
