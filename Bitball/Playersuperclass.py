import random
import time
import sqlite3
conn=sqlite3.connect('player_database.db')
C=conn.cursor()

#Define dice_roll function that accepts one argument that is equal to number of sides on dice rolled

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
        def __init__(self, name, keeper):
                self.name = name
                self.ini = dice_roll(20)
                self.STR = Statgen()
                self.DEX = Statgen()
                self.WIS = Statgen()
                self.CHA = Statgen()
                self.MAG = Statgen()
                self.DMAG = Statgen()
                self.keeper = False
                self.X = 0
                self.Y = 0
class Team1:
        name = "Aave Ghosts"
class Team2:
        name = "Olympus Omegas"

        #define passing behavior

        #define tackling behavior

        #define movement behavior

#Create subclass Ranger
        #define target behavior
                        
#Create subclass Shuttle
        #define openpass behavior
                        
#Create subclass Keeper
        #define keep behavior
                        
#Create subclass Striker
        #define shoot behavior

start_time = time.time()
seconds = 10
ScoreA=0
ScoreB=0
TeamAPass=0
TeamBPass=0



#Creates 10 named players

#P1 = Player("Gobro Gons",True)
#P2 = Player("Basilio Milano",False)
#P3 = Player("Cora Twill",False)
#P4 = Player("Nadezda York",False)
#P5 = Player("Vasanti Cruz",False)
#P6 = Player("Helias King",True)
#P7 = Player("Lyman Hollencrantz",False)
#P8 = Player("Pradip Santana",False)
#P9 = Player("Amelia Lacroix",False)
#P10 = Player("Khil Metarot",False)

P1 = Player("Gobro Gons",True)
P2 = Player("Basilio Milano",False)
P3 = Player("Cora Twill",False)
P4 = Player("Nadezda York",False)
P5 = Player("Vasanti Cruz",False)
P6 = Player("Helias King",True)
P7 = Player("Lyman Hollencrantz",False)
P8 = Player("Pradip Santana",False)
P9 = Player("Amelia Lacroix",False)
P10 = Player("Khil Metarot",False)


def gameloop():
        P1.ini = dice_roll(20)
        P2.ini = dice_roll(20)
        P3.ini = dice_roll(20)
        P4.ini = dice_roll(20)
        P5.ini = dice_roll(20)
        P6.ini = dice_roll(20)
        P7.ini = dice_roll(20)
        P8.ini = dice_roll(20)
        P9.ini = dice_roll(20)
        P10.ini = dice_roll(20)


#Puts them onto TeamA

        TeamA = [P1.name,P2.name,P3.name,P4.name,P5.name]
        PTeamA = [P1,P2,P3,P4,P5]

#Or TeamB

        TeamB = [P6.name,P7.name,P8.name,P9.name,P10.name]
        PTeamB = [P6,P7,P8,P9,P10]

#Orders players by their initiatives

        Order = [
                (P1,P1.name,P1.ini),
                (P2,P2.name,P2.ini),
                (P3,P3.name,P3.ini),
                (P4,P4.name,P4.ini),
                (P5,P5.name,P5.ini),
                (P6,P6.name,P6.ini),
                (P7,P7.name,P7.ini),
                (P8,P8.name,P8.ini),
                (P9,P9.name,P9.ini),
                (P10,P10.name,P10.ini),]
        Ordered = sorted(Order, key=lambda player: player[2])

#Unpacks first and last tuple in "Ordered" list

        (player1,firstname,firstini)=Ordered[0]
        (player2,secondname,secondini)=Ordered[1]
        (player3,thirdname,thirdini)=Ordered[2]
        (player10,lastname, lastini)=Ordered[9]

#Flavor text displays the first and last player in initiative order
        #print(player10.name+" takes first initiative with " +str(lastini) + " plus a DEX score of "+str((player10.DEX))+" for a total of "+str((player10.DEX+player10.ini)))
        #time.sleep(2)
        #print(player1.name+" will end the round with " +str(firstini)+ " plus a DEX score of " +str((player1.DEX))+" for a total of "+str((player1.DEX+player1.ini)))
        #time.sleep(2)
#Begins play as first player tries to pass the ball

        #Calls global scores and pass counters
        global ScoreA
        global ScoreB
        global TeamAPass
        global TeamBPass
        
        if player10.STR >= player2.STR: 
                print(player10.name+" launches the ball")
                if player3.DEX+dice_roll(20)>=20:
                        print(thirdname+" receives!")
                        time.sleep(2)
                        if player10.name in TeamA and player3.name in TeamA:
                                
                                TeamAPass+=1
                                print(Team1.name, " pass count = ",TeamAPass)
                                time.sleep(.5)
                                if TeamAPass == 4:
                                        print (player3.name," takes a shot!")
                                        time.sleep(.5)
                                        print("The ",Team2.name," keeper braces")
                                        time.sleep(2)
                                        if player3.DEX+dice_roll(6) >= 20:
                                                ScoreA+=4
                                                print(player3.name," scores 4 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+dice_roll(6) >= 19:
                                                ScoreA+=3
                                                print(player3.name," scores 3 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+dice_roll(6) >= 18:
                                                ScoreA+=2
                                                print(player3.name," scores 2 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+dice_roll(6) >= 17:
                                                ScoreA+=1
                                                print(player3.name," scores 1 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        else:
                                                TeamAPass=0
                                                for player in PTeamB:
                                                        if player.keeper == True:
                                                                print(player.name," blocks the shot!")
                                                                
                        elif player10.name in TeamB and player3.name in TeamB:
                                
                                TeamBPass+=1
                                print(Team2.name," pass count = ",TeamBPass)
                                time.sleep(.5)
                                if TeamBPass == 4:
                                        print (player3.name," takes a shot!")
                                        time.sleep(.5)
                                        print("The ",Team1.name," keeper braces")
                                        time.sleep(2)
                                        if player3.DEX+dice_roll(6) >= 20:
                                                ScoreB+=4
                                                print(player3.name," scores 4 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+dice_roll(6) >= 19:
                                                ScoreB+=3
                                                print(player3.name," scores 3 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+dice_roll(6) >= 18:
                                                ScoreB+=2
                                                print(player3.name," scores 2 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+dice_roll(6) >= 17:
                                                ScoreB+=1
                                                print(player3.name," scores 1 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        else:
                                                TeamBPass=0
                                                for player in PTeamA:
                                                        if player.keeper == True:
                                                                print(player.name," blocks the shot!")
                                                                
                                        
                        elif player10.name in TeamA and player3.name in TeamB:
                                TeamBPass+=1
                                print("A nice interception for ",Team2.name,"!")
                                print(Team2.name," pass count = ",TeamBPass)
                                time.sleep(.5)
                                if TeamBPass == 4:
                                        print (player3.name," takes a shot!")
                                        time.sleep(.5)
                                        print("The ",Team1.name," keeper braces")
                                        time.sleep(2)
                                        if player3.DEX+dice_roll(6) >= 20:
                                                ScoreB+=4
                                                print(player3.name," scores 4 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+dice_roll(6) >= 19:
                                                ScoreB+=3
                                                print(player3.name," scores 3 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+dice_roll(6) >= 18:
                                                ScoreB+=2
                                                print(player3.name," scores 2 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+dice_roll(6) >= 17:
                                                ScoreB+=1
                                                print(player3.name," scores 1 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        else:
                                                TeamBPass=0
                                                for player in PTeamA:
                                                        if player.keeper == True:
                                                                print(player.name," blocks the shot!")
                                                                
                        else:
                                TeamAPass+=1
                                print("A nice interception for ",Team1.name,"!")
                                print(Team1.name,"pass count = ",TeamAPass)
                                if TeamAPass == 4:
                                        print (player3.name," takes a shot!")
                                        time.sleep(.5)
                                        print("The ",Team2.name," keeper braces")
                                        time.sleep(2)
                                        if player3.DEX+dice_roll(6) >= 20:
                                                ScoreA+=4
                                                print(player3.name," scores 4 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+dice_roll(6) >= 19:
                                                ScoreA+=3
                                                print(player3.name," scores 3 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+dice_roll(6) >= 18:
                                                ScoreA+=2
                                                print(player3.name," scores 2 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+dice_roll(6) >= 17:
                                                ScoreA+=1
                                                print(player3.name," scores 1 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        else:
                                                TeamAPass=0
                                                for player in PTeamB:
                                                        if player.keeper == True:
                                                                print(player.name," blocks the shot!")
                        
                                
                else:
                        print(thirdname+" attempts a catch but fumbles the ball!")

        elif player10.name in TeamA and player2.name in TeamA:
                        print(player10.name, " starts running for the goal")
        elif player10.name in TeamB and player2.name in TeamB:
                        print(player10.name, " makes a break for it!")
        else:
                print(player10.name+" gets tackled by "+player2.name+" and loses the ball!")
                time.sleep(2)
                if player2.name in TeamA:
                        print(Team1.name," has the ball!")
                        
                        
                else:
                        print(Team2.name," has the ball!")
        
ScoreA=ScoreA
ScoreB=ScoreB
start_time = time.time()
seconds = 1800
while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        gameloop()
        time.sleep(0.5)
        if elapsed_time>seconds:
                print("The Game has ended")
                print(Team1.name,": ",ScoreA)
                print(Team2.name,": ",ScoreB)
                if ScoreA>ScoreB:
                        print(Team1.name," wins the Game")
                elif ScoreA<ScoreB:
                        print(Team2.name," wins the Game")
                else:
                        print("The Game ends in a tie")
                
                        
                break
conn.close()
        

