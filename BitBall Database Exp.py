import random
import time
import sqlite3
import sys
import os

conn=sqlite3.connect('player_database.db')
C=conn.cursor()

#print("Please enter the name of the first team: ")
#Team1name = input()
#print("Please enter the name of the second team: ")
#Team2name = input()

class Team1:
        name = "Alchemix Conjurers"
class Team2:
        name = "Olympus Omegas" 

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
        def __init__(self, name, keeper, team):
                self.name = name
                self.team = team
                (C.execute("SELECT str_mod FROM players WHERE name =:name",{"name":self.name}))
                self.STR = C.fetchone()[0]
                (C.execute("SELECT dex_mod FROM players WHERE name =:name",{"name":self.name}))
                self.DEX = C.fetchone()[0]
                (C.execute("SELECT wis_mod FROM players WHERE name =:name",{"name":self.name}))
                self.WIS = C.fetchone()[0]
                (C.execute("SELECT cha_mod FROM players WHERE name =:name",{"name":self.name}))
                self.CHA = C.fetchone()[0]
                (C.execute("SELECT mag_mod FROM players WHERE name =:name",{"name":self.name}))
                self.MAG = C.fetchone()[0]
                (C.execute("SELECT dmag_mod FROM players WHERE name =:name",{"name":self.name}))
                self.DMAG = C.fetchone()[0]
                self.keeper = keeper
                (C.execute("SELECT gk_mod FROM players WHERE name =:name",{"name":self.name}))
                self.GK = C.fetchone()[0]
                self.ini = dice_roll(20)+self.DEX
                self.X = 0
                self.Y = 0



#Initialize scores
ScoreA=0
ScoreB=0

#Initialize team pass counters
TeamAPass=0
TeamBPass=0

#Make start time current time at beginning of game
start_time = time.time()


#How long the game lasts
seconds = 10



#Creates 10 named players

P1 = Player("Hashad Kuhn",True,"aave_ghosts")
P2 = Player("Jon-Paul Jericho",False,"aave_ghosts")
P3 = Player("Djimi Koundé",False,"aave_ghosts")
P4 = Player("Mandy Malakar",False,"aave_ghosts")
P5 = Player("Tel'blort",False,"aave_ghosts")

P6 = Player("Helias King",True,"olympus_omegas")
P7 = Player("Lyman Hollencrantz",False,"olympus_omegas")
P8 = Player("Pradip Santana",False,"olympus_omegas")
P9 = Player("Amelia Lacroix",False,"olympus_omegas")
P10 = Player("Khil Metarot",False,"olympus_omegas")
 

#Puts them onto TeamA

TeamA = [P1.name,P2.name,P3.name,P4.name,P5.name]
PTeamA = [P1,P2,P3,P4,P5]

for Player in PTeamA:
        if Player.keeper == True:
                KeeperA = Player
#Or TeamB

TeamB = [P6.name,P7.name,P8.name,P9.name,P10.name]
PTeamB = [P6,P7,P8,P9,P10]

for Player in PTeamB:
        if Player.keeper == True:
                KeeperB = Player

#start defining the game
def gameloop():
        P1.ini = dice_roll(20)+P1.DEX
        P2.ini = dice_roll(20)+P2.DEX
        P3.ini = dice_roll(20)+P3.DEX
        P4.ini = dice_roll(20)+P4.DEX
        P5.ini = dice_roll(20)+P5.DEX
        P6.ini = dice_roll(20)+P6.DEX
        P7.ini = dice_roll(20)+P7.DEX
        P8.ini = dice_roll(20)+P8.DEX
        P9.ini = dice_roll(20)+P9.DEX
        P10.ini = dice_roll(20)+P10.DEX




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

        (player1,firstname,firstini)=Ordered[9]
        (player2,secondname,secondini)=Ordered[8]
        (player3,thirdname,thirdini)=Ordered[7]
        (player4,fourthname,fourthini)=Ordered[6]
        (player5,fifthname,fifthini)=Ordered[5]
        (player6,sixthname,sixthini)=Ordered[4]
        (player7,seventhname,seventhini)=Ordered[3]
        (player8,eighthname,eightini)=Ordered[2]
        (player9,ninthame,ninthini)=Ordered[1]
        (player10,lastname, lastini)=Ordered[0]

#Flavor text displays the first and last player in initiative order
        #print(player1.name+" takes first initiative with " +str(lastini) + " plus a DEX score of "+str((player1.DEX))+" for a total of "+str((player1.DEX+player1.ini)))
        #time.sleep(2)
        #print(player1.name+" will end the round with " +str(firstini)+ " plus a DEX score of " +str((player1.DEX))+" for a total of "+str((player1.DEX+player1.ini)))
        #time.sleep(2)
#Begins play as first player tries to pass the ball

        #Calls global scores and pass counters
        global ScoreA
        global ScoreB
        global TeamAPass
        global TeamBPass

        
        #Series of checks for game loop
        
        if player1.STR >= player2.STR: 
                print(player1.name+" launches the ball")
                time.sleep(.5)
                if player3.DEX+dice_roll(20)>=10:
                        print(thirdname+" receives!")
                        time.sleep(1)
                        if player1.name in TeamA and player3.name in TeamA:
                                TeamAPass+=1
                                print(Team1.name, " pass count = ",TeamAPass)
                                time.sleep(.5)
                                if TeamAPass == 4:
                                        print (player3.name," takes a shot!")
                                        time.sleep(.5)
                                        print ("The ",Team2.name," keeper braces")
                                        time.sleep(3)
                                        roll = dice_roll(20)
                                        kroll = dice_roll(20)
                                        if KeeperB.GK+kroll > player3.DEX+roll:
                                                print("The ",Team2.name," keeper saves!")
                                                TeamAPass=0
                                                time.sleep(.5)
                                        elif player3.DEX+roll >= 20:
                                                ScoreA+=4
                                                print(player3.name," scores 4 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+roll >= 15:
                                                ScoreA+=3
                                                print(player3.name," scores 3 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+roll >= 12:
                                                ScoreA+=2
                                                print(player3.name," scores 2 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+roll >= 10:
                                                ScoreA+=1
                                                print(player3.name," scores 1 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        else:
                                                print("The ",Team2.name," keeper blocks the shot!")
                                                TeamAPass=0
                                                time.sleep(.5)
                                        
                        elif player1.name in TeamB and player3.name in TeamB:
                                
                                TeamBPass+=1
                                print(Team2.name," pass count = ",TeamBPass)
                                time.sleep(.5)
                                if TeamBPass == 4:
                                        print (player3.name," takes a shot!")
                                        time.sleep(.5)
                                        print("The ",Team1.name," keeper braces")
                                        time.sleep(3)
                                        roll = dice_roll(20)
                                        kroll = dice_roll(20)
                                        if KeeperA.GK+kroll > player3.DEX+roll:
                                                print("The ",Team1.name," keeper saves!")
                                                TeamBPass=0
                                                time.sleep(.5)        
                                        elif player3.DEX+roll >= 20:
                                                ScoreB+=4
                                                print(player3.name," scores 4 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+roll >= 15:
                                                ScoreB+=3
                                                print(player3.name," scores 3 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+roll >= 12:
                                                ScoreB+=2
                                                print(player3.name," scores 2 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+roll >= 10:
                                                ScoreB+=1
                                                print(player3.name," scores 1 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        else:
                                                print("The ",Team1.name," keeper blocks the shot!")
                                                TeamBPass=0
                                                time.sleep(.5)
                                        
                        elif player1.name in TeamA and player3.name in TeamB:
                                TeamBPass+=1
                                print("A nice interception for ",Team2.name,"!")
                                time.sleep(.5)
                                print(Team2.name," pass count = ",TeamBPass)
                                time.sleep(.5)
                                if TeamBPass == 4:
                                        print (player3.name," takes a shot!")
                                        time.sleep(.5)
                                        print("The ",Team1.name," keeper braces")
                                        time.sleep(3)
                                        roll = dice_roll(20)
                                        kroll = dice_roll(20)
                                        if KeeperA.GK+kroll > player3.DEX+roll:
                                                print("The ",Team1.name," keeper saves!")
                                                TeamBPass=0
                                                time.sleep(.5)
                                        elif player3.DEX+roll >= 20:
                                                ScoreB+=4
                                                print(player3.name," scores 4 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+roll >= 15:
                                                ScoreB+=3
                                                print(player3.name," scores 3 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+roll >= 12:
                                                ScoreB+=2
                                                print(player3.name," scores 2 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        elif player3.DEX+roll >= 10:
                                                ScoreB+=1
                                                print(player3.name," scores 1 for the",Team2.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamBPass=0
                                        else:
                                                print("The ",Team1.name," keeper blocks the shot!")
                                                TeamBPass=0
                                                time.sleep(.5)
                        else:
                                TeamAPass+=1
                                print("A nice interception for ",Team1.name,"!")
                                time.sleep(.5)
                                print(Team1.name,"pass count = ",TeamAPass)
                                time.sleep(.5)
                                if TeamAPass == 4:
                                        print (player3.name," takes a shot!")
                                        time.sleep(.5)
                                        print("The ",Team2.name," keeper braces")
                                        time.sleep(3)
                                        roll = dice_roll(20)
                                        kroll = dice_roll(20)
                                        if KeeperA.GK+kroll > player3.DEX+roll:
                                                print("The ",Team2.name," keeper saves!")
                                                TeamAPass=0
                                                time.sleep(.5)
                                        elif player3.DEX+roll >= 20:
                                                ScoreA+=4
                                                print(player3.name," scores 4 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+roll >= 15:
                                                ScoreA+=3
                                                print(player3.name," scores 3 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+roll >= 12:
                                                ScoreA+=2
                                                print(player3.name," scores 2 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        elif player3.DEX+roll >= 10:
                                                ScoreA+=1
                                                print(player3.name," scores 1 for the",Team1.name,"!")
                                                time.sleep(3)
                                                print(Team1.name, ": ",ScoreA)
                                                print(Team2.name, ": ",ScoreB)
                                                TeamAPass=0
                                        else:
                                                print("The ",Team2.name," keeper blocks the shot!")
                                                TeamAPass=0
                                                time.sleep(.5)
                                
                else:
                        print(thirdname+" attempts a catch but fumbles the ball!")
                        time.sleep(.5)

        elif player1.name in TeamA and player2.name in TeamA:
                        print(player1.name, " starts running for the goal")
                        time.sleep(.5)
        elif player1.name in TeamB and player2.name in TeamB:
                        print(player1.name, " makes a break for it!")
                        time.sleep(.5)
        else:
                print(player1.name+" gets tackled by "+player2.name+" and loses the ball!")
                time.sleep(1)
                if player2.name in TeamA:
                        print(Team1.name," have the ball!")
                        time.sleep(.5)
                        
                else:
                        print(Team2.name," have the ball!")
                        time.sleep(.5)
        #Sets scores to current scores before looping again        
        ScoreA=ScoreA
        ScoreB=ScoreB


#Creates loop that calls gameloop() for x amount of seconds and prints the final score when game time runs out
while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        gameloop()
        if seconds-elapsed_time >= 0:
                print(round(seconds-elapsed_time))
        time.sleep(.5)
        if elapsed_time>seconds:
                print("The Game has ended")
                print(Team1.name,": ",ScoreA)
                print(Team2.name,": ",ScoreB)
                if ScoreA>ScoreB:
                        print(Team1.name," win the Game")
                elif ScoreA<ScoreB:
                        print(Team2.name," win the Game")
                else:
                        print("The Game ends in a tie")
                
                
                break
os.execv(sys.argv[0], sys.argv)
                
conn.close()
