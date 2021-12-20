import random
import time
import sqlite3

while True:
        conn=sqlite3.connect('player_database.db')
        C=conn.cursor()

        #print()
        #print("Please enter the name of the first team: ")
        #Team1name = input()
        #print()
        #print("Please enter the name of the second team: ")
        #Team2name = input()


          

        #Define dice_roll function that accepts one argument that is equal to number of sides on dice rolled

        def dice_roll(d):
                result = random.randint(1,d)
                return result

        #Define Statgen function that rolls 4d6, drops the lowest number, and sums the remaining 3

        # def Statgen():
        #         dice = [dice_roll(6),dice_roll(6),dice_roll(6),dice_roll(6)]
        #         stat = []
        #         dice.sort()
        #         stat.append(dice[1])
        #         stat.append(dice[2])
        #         stat.append(dice[3])
        #         stat = stat[0]+stat[1]+stat[2]
        #         return stat
                
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
                        self.inv = []
                        self.GK = C.fetchone()[0]
                        self.ini = dice_roll(20)+self.DEX
                        self.HP = 10

                def takedmg(self):
                        self.HP -= 5
                        if "cursed item" in self.inv:
                                print ("A curse haunts",self.name)
                                self.hp -=2
                        if self.HP <=0:
                                print (self.name, "is gravely injured!")
                        print()
                        if self.HP > 0:
                                print (self.name,"HP: ",self.HP)


        class Team1:
                name = "Chainlink Frogs"

        class Team2:
                name = "Compound Dragons"

        newlist=[]
        loopcount=0
        pos=[]
        silence = 0

        #Initialize scores
        ScoreA=0
        ScoreB=0

        #Initialize team pass counters
        TeamAPass=0
        TeamBPass=0

        #Initialize foul counter for both teams
        FoulA=0
        FoulB=0

        #Initialize run counter for both teams
        Aruncount=0
        Bruncount=0

        #How long the game lasts
        seconds = 1200

        #Make start time current time at beginning of game
        start_time = time.time()

        #Creates 10 named players

        P1 = Player("Tamara Edison",True,"olympus_omegas")
        P2 = Player("Borjo Blozok",False,"olympus_omegas")
        P3 = Player("Gauchinho",False,"olympus_omegas")
        P4 = Player("Sylvia Trask",False,"olympus_omegas")
        P5 = Player("Talia Jeffers",False,"olympus_omegas")
         
        P6 = Player("Daisuke Sato",True,"olympus_omegas")
        P7 = Player("Paro'blort",False,"olympus_omegas")
        P8 = Player("Tad Garbaj",False,"olympus_omegas")
        P9 = Player("Thankful Tenniford",False,"olympus_omegas")
        P10 = Player("Horus Shelp",False,"olympus_omegas")


        # BenchA =[Player("GhostA1",False,"TeamA"),
        #         Player("GhostA2", False, "TeamA")]
        # BenchB =[Player("GhostB1",False, "TeamB"),
        #         Player("GhostB2",False,"TeamB")]

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
                #Calls global scores and pass counters
                global ScoreA
                global ScoreB
                global TeamAPass
                global TeamBPass
                global FoulA
                global FoulB
                global Aruncount
                global Bruncount
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
                T1order=[]
                T2order=[]
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
                #print (Ordered)
                for player in Ordered: 
                        if player[1] in TeamA:
                                T1order.append(player[1])
                for player in Ordered: 
                        if player[1] in TeamB:
                                T2order.append(player[1])
                                        
                

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

                def getini():
                        

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
                        for player in Ordered: 
                                if player in TeamA:
                                        T1order.append(player[1])
                        for player in Ordered: 
                                if player in TeamB:
                                        T2order.append(player[1])


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

                def loot():
                        print(player1.name,"looks around for loot...")
                        print()
                        time.sleep(1)
                        lootroll = dice_roll(20)
                        if lootroll == 20:
                                P1.inv += "small item"
                                print ("...and found something.")
                                time.sleep(1)
                        elif lootroll == 1:
                                P1.inv += "cursed item"
                                time.sleep(1)
                                print ("...and didn't like what they found.")
                        else:
                                print("...but found nothing.")
                                time.sleep(1)
                                print()
                

                #defines a function that calls a penalty shot to occur
                def penalty():
                        global ScoreA
                        global ScoreB
                        if player1.name in TeamA and player2.name in TeamA:
                                while player1.name in TeamA and player2.name in TeamA:
                                        Ordered.pop(8)
                                        Ordered.insert(0,0,)
                                        return Ordered
                                
                        if player1.name in TeamB and player2.name in TeamB:
                                while player1.name in TeamB and player2.name in TeamB:
                                        Ordered.pop(8)
                                        Ordered.insert(0,0,)
                                        return Ordered
                                
                        #condition for player1 to score for TeamA
                        if player1.name in TeamA:
                                print()
                                print (player1.name,"approaches the center diamond for a penalty shot.")
                                time.sleep(4)
                                print()
                                print (KeeperB.name,"clears the",Team2.name,"Ring.")
                                time.sleep(4)
                                print()
                                print ("The sound of grinding metal fills the air.")
                                time.sleep(4)
                                print()
                                print ("The",Team2.name,"Ring tilts to a horizontal position.")
                                time.sleep(4)
                                print()
                                print (player1.name,"lines up their trajectory...")
                                time.sleep(5)
                                print()
                                print("...and launches the ball!")
                                time.sleep(4)
                                print()
                                print ("(The",Team2.name,"keeper braces as they watch helplessly)")
                                time.sleep(1)
                                roll = dice_roll(20)

                                if player1.MAG+roll >= 24:
                                        ScoreA+=4
                                        print()
                                        print(player1.name,"scores 4 for the",Team1.name,"!")
                                        time.sleep(3)
                                        print()
                                        print(Team1.name, ": ",ScoreA)
                                        print()
                                        print(Team2.name, ": ",ScoreB)
                                        
                                elif player1.MAG+roll >= 20:
                                        ScoreA+=3
                                        print()
                                        print(player1.name,"scores 3 for the",Team1.name,"!")
                                        time.sleep(3)
                                        print()
                                        print(Team1.name, ": ",ScoreA)
                                        print()
                                        print(Team2.name, ": ",ScoreB)
                                       
                                elif player1.MAG+roll >= 15:
                                        ScoreA+=2
                                        print()
                                        print(player1.name,"scores 2 for the",Team1.name,"!")
                                        time.sleep(3)
                                        print()
                                        print(Team1.name, ": ",ScoreA)
                                        print()
                                        print(Team2.name, ": ",ScoreB)
                                        
                                elif player1.MAG+roll >= 10:
                                        ScoreA+=1
                                        print()
                                        print(player1.name,"scores 1 for the",Team1.name,"!")
                                        time.sleep(3)
                                        print()
                                        print(Team1.name, ": ",ScoreA)
                                        print()
                                        print(Team2.name, ": ",ScoreB)
                                        
                                else:
                                        print()
                                        print("An unfortunate miss.")
                                        time.sleep(2)
                                        print()
                                        print("The",Team2.name,"keeper returns to their position.")
                                        time.sleep(1)
                                        print()
                                        print("Play resumes.")
                                        time.sleep(2)
                        #Condition for player1 to score for TeamB
                        else:
                                print()
                                print (player1.name,"approaches the center diamond for a penalty shot.")
                                time.sleep(4)
                                print()
                                print (KeeperA.name,"clears the",Team1.name,"Ring.")
                                time.sleep(4)
                                print()
                                print ("The crowd roars in anticipation.")
                                time.sleep(4)
                                print()
                                print ("The",Team1.name,"Ring tilts to a horizontal position.")
                                time.sleep(4)
                                print()
                                print (player1.name,"lines up their trajectory...")
                                time.sleep(5)
                                print()
                                print("...and launches the ball!")
                                time.sleep(4)
                                print()
                                print ("(The",Team1.name,"keeper braces as they watch helplessly)")
                                time.sleep(1)
                                roll = dice_roll(20)
                

                                if player1.MAG+roll >= 24:
                                        ScoreB+=4
                                        print()
                                        print(player1.name,"scores 4 for the",Team2.name,"!")
                                        time.sleep(3)
                                        print()
                                        print(Team1.name, ": ",ScoreA)
                                        print()
                                        print(Team2.name, ": ",ScoreB)
                                        
                                elif player1.MAG+roll >= 20:
                                        ScoreB+=3
                                        print()
                                        print(player1.name,"scores 3 for the",Team2.name,"!")
                                        time.sleep(3)
                                        print()
                                        print(Team1.name, ": ",ScoreA)
                                        print()
                                        print(Team2.name, ": ",ScoreB)
                                        
                                elif player1.MAG+roll >= 15:
                                        ScoreB+=2
                                        print()
                                        print(player1.name,"scores 2 for the",Team2.name,"!")
                                        time.sleep(3)
                                        print()
                                        print(Team1.name, ": ",ScoreA)
                                        print()
                                        print(Team2.name, ": ",ScoreB)
                                        
                                elif player1.MAG+roll >= 10:
                                        ScoreB+=1
                                        print()
                                        print(player1.name,"scores 1 for the",Team2.name,"!")
                                        time.sleep(3)
                                        print()
                                        print(Team1.name, ": ",ScoreA)
                                        print()
                                        print(Team2.name, ": ",ScoreB)
                                        
                                else:
                                        print()
                                        print("An unfortunate miss.")
                                        time.sleep(2)
                                        print()
                                        print("The",Team1.name,"keeper returns to their position.")
                                        time.sleep(1)
                                        print()
                                        print("Play resumes.")
                                        time.sleep(2)
                
                #Series of checks for game loop
                
                def checks():
                        global FoulA
                        global FoulB
                        global TeamAPass
                        global TeamBPass
                        global ScoreB
                        global ScoreA
                        global Aruncount
                        global Bruncount
                        global newlist
                        global loopcount
                        global pos
                        global previous
                        global silence
                        global Player
                        
                        #Checks length of newlist. If all players have appeared in text and have been added to newlist, starts a new round.
                        #Additionally, Players now look for loot at the beginning of each new round.

                        if len(newlist)>=10:
                                newlist=[]
                                getini()
                                print()
                                #New round console check
                                #print("IT'S A NEW ROUND!")
                                time.sleep(2)
                                loot()

                        for player in PTeamA:
                                if Player.HP <= 0:
                                        player.DEX = -99
                                                
                                                

                        for player in PTeamB:
                                if Player.HP <= 0:
                                        player.DEX = -99

                        #Checks for team possession

                        if pos == ['TeamA']:
                                while player1.name not in TeamA:
                                                Ordered.pop(9)
                                                Ordered.insert(0,0,)
                                                return Ordered
                                pos = []
                        if pos == ['TeamB']:
                                while player1.name not in TeamB:
                                                Ordered.pop(9)
                                                Ordered.insert(0,0,)
                                                return Ordered
                                pos = []

                        #Checks for keeper to "make sure they stay in their ring" (don't appear in text making plays)
                                
                        if player1.keeper == True or player2.keeper==True:
                                if player1.name not in newlist:
                                        newlist.append(player1.name)
                                Ordered.pop()
                                return Ordered

                        #Conditions for tackles and fouls to occur

                        if player2.DMAG + dice_roll(20) > player1.WIS+dice_roll(20):
                                print()
                                print(player1.name,"gets tackled by",player2.name,"and loses the ball!")
                                time.sleep(1)
                                player1.takedmg()
                                print()
                                print("Hard to believe the referee let them get away with that one...")
                                time.sleep(1.5)
                                if player2.name in TeamA:
                                        print()
                                        print(Team1.name,"have the ball!")
                                        time.sleep(2)
                                        pos=[]
                                        pos.append("TeamA")
                                        
                                
                                elif player2.name in TeamB:
                                        print()
                                        print(Team2.name,"have the ball!")
                                        time.sleep(2)
                                        pos=[]
                                        pos.append("TeamB")

                                elif player10.name in TeamA:
                                        print()
                                        print(Team1.name,"have the ball!")
                                        time.sleep(2)
                                        pos=[]
                                        pos.append("TeamA")
                                        
                                else:
                                        print()
                                        print(Team2.name,"have the ball!")
                                        time.sleep(2)
                                        pos=[]
                                        pos.append("TeamB")
                                        
                                if player2.STR+dice_roll(20) > player1.WIS+dice_roll(20): 
                                        print()
                                        print("* S M A S H *")
                                        time.sleep(2)
                                        print()
                                        print("Some obvious roughing from",player2.name,"results in a foul.")
                                        player1.takedmg()
                                        time.sleep(2)
                                        if player2.name in TeamA:
                                                FoulA+=1
                                                print()
                                                #Foul console check
                                                #print(Team1.name,"Fouls: ",FoulA)
                                                time.sleep(1)
                                        else:
                                                FoulB+=1
                                                print()
                                                #Foul console check
                                                #print(Team2.name,"Fouls: ",FoulB)
                                                time.sleep(1)
                                        if FoulA==3:
                                                penalty()
                                                FoulA=0
                                        if FoulB==3:
                                                penalty()
                                                FoulB=0

                        #Huge set of conditions for different passing outcomes
                        #This first set is a successful pass to a teammate.
                        #It's followed by a bunch of code that checks the team's pass counter, and if the team makes four 
                        #successful passes, the receiving Player of the fourth pass takes a shot.
                        #I should have made all of that into a function because I call it a lot, but I didn't and here we are.

                        if player1.STR+dice_roll(20) >= player2.STR+dice_roll(20): 
                                print()
                                print(player1.name,"gets the ball and launches it.")
                                time.sleep(2)
                                if player3.DEX+dice_roll(20)>=10:
                                        print()
                                        print(thirdname+" receives!")
                                        time.sleep(1)
                                        if player1.name in TeamA and player3.name in TeamA:
                                                TeamAPass+=1
                                                print()
                                                #Pass Count console check
                                                #print(Team1.name, "pass count = ",TeamAPass)
                                                time.sleep(2)
                                                if TeamAPass == 4:
                                                        print()
                                                        print (player3.name,"makes a quick play!")
                                                        time.sleep(2)
                                                        print()
                                                        print ("The",Team2.name,"keeper braces.")
                                                        time.sleep(5)
                                                        roll = dice_roll(20)
                                                        kroll = dice_roll(20)
                                                        if KeeperB.GK+kroll > player3.DEX+roll:
                                                                print()
                                                                print(KeeperB.name,"saves!")
                                                                TeamAPass=0
                                                                time.sleep(2)
                                                        elif player3.DEX+roll >= 20:
                                                                ScoreA+=4
                                                                print()
                                                                print(player3.name,"scores 4 for the",Team1.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 15:
                                                                ScoreA+=3
                                                                print()
                                                                print(player3.name,"scores 3 for the",Team1.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 12:
                                                                ScoreA+=2
                                                                print()
                                                                print(player3.name,"scores 2 for the",Team1.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 10:
                                                                ScoreA+=1
                                                                print()
                                                                print(player3.name,"scores 1 for the",Team1.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamAPass=0
                                                        else:
                                                                print()
                                                                print("The ",Team2.name,"keeper blocks the shot!")
                                                                TeamAPass=0
                                                                time.sleep(2)
                                                        
                                        elif player1.name in TeamB and player3.name in TeamB:
                                                
                                                TeamBPass+=1
                                                print()
                                                #Pass Count console check
                                                #print(Team2.name,"pass count = ",TeamBPass)
                                                time.sleep(2)
                                                if TeamBPass == 4:
                                                        print()
                                                        print (player3.name,"sends it!")
                                                        time.sleep(2)
                                                        print()
                                                        print("The",Team1.name,"keeper braces.")
                                                        time.sleep(5)
                                                        roll = dice_roll(20)
                                                        kroll = dice_roll(20)
                                                        if KeeperA.GK+kroll > player3.DEX+roll:
                                                                print()
                                                                print(KeeperA.name,"saves!")
                                                                TeamBPass=0
                                                                time.sleep(2)        
                                                        elif player3.DEX+roll >= 20:
                                                                ScoreB+=4
                                                                print()
                                                                print(player3.name,"scores 4 for the",Team2.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 15:
                                                                ScoreB+=3
                                                                print()
                                                                print(player3.name,"scores 3 for the",Team2.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 12:
                                                                ScoreB+=2
                                                                print()
                                                                print(player3.name,"scores 2 for the",Team2.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 10:
                                                                ScoreB+=1
                                                                print()
                                                                print(player3.name,"scores 1 for the",Team2.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamBPass=0
                                                        else:
                                                                print()
                                                                print("The ",Team1.name,"keeper blocks the shot!")
                                                                TeamBPass=0
                                                                time.sleep(2)

                                        #Interceptions occur when a pass happens and a player from the opposing team is in the receiving position
                                                        
                                        elif player1.name in TeamA and player3.name in TeamB:
                                                TeamBPass+=1
                                                print()
                                                print("A nice interception for the",Team2.name,"!")
                                                time.sleep(2)
                                                print()
                                                #Pass Count console check
                                                #print(Team2.name," pass count = ",TeamBPass)
                                                time.sleep(2)
                                                if TeamBPass == 4:
                                                        print()
                                                        print (player3.name,"takes a shot!")
                                                        time.sleep(2)
                                                        print()
                                                        print("The",Team1.name,"keeper braces.")
                                                        time.sleep(5)
                                                        roll = dice_roll(20)
                                                        kroll = dice_roll(20)
                                                        if KeeperA.GK+kroll > player3.DEX+roll:
                                                                print()
                                                                print(KeeperA.name,"saves!")
                                                                TeamBPass=0
                                                                time.sleep(2)
                                                        elif player3.DEX+roll >= 20:
                                                                ScoreB+=4
                                                                print()
                                                                print(player3.name,"scores 4 for the",Team2.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 15:
                                                                ScoreB+=3
                                                                print()
                                                                print(player3.name,"scores 3 for the",Team2.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 12:
                                                                ScoreB+=2
                                                                print()
                                                                print(player3.name,"scores 2 for the",Team2.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 10:
                                                                ScoreB+=1
                                                                print()
                                                                print(player3.name,"scores 1 for the",Team2.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamBPass=0
                                                        else:
                                                                print()
                                                                print("The ",Team1.name,"keeper blocks the shot!")
                                                                TeamBPass=0
                                                                time.sleep(2)
                                        else:
                                                TeamAPass+=1
                                                print()
                                                print("A nice interception for the",Team1.name,"!")
                                                time.sleep(2)
                                                print()
                                                #Pass count console check
                                                #print(Team1.name,"pass count = ",TeamAPass)
                                                time.sleep(2)
                                                if TeamAPass == 4:
                                                        print()
                                                        print (player3.name,"takes a shot!")
                                                        time.sleep(2)
                                                        print()
                                                        print("The",Team2.name,"keeper braces.")
                                                        time.sleep(5)
                                                        roll = dice_roll(20)
                                                        kroll = dice_roll(20)
                                                        if KeeperB.GK+kroll > player3.DEX+roll:
                                                                print()
                                                                print(KeeperB.name,"saves!")
                                                                TeamAPass=0
                                                                time.sleep(2)
                                                        elif player3.DEX+roll >= 20:
                                                                ScoreA+=4
                                                                print()
                                                                print(player3.name,"scores 4 for the",Team1.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 15:
                                                                ScoreA+=3
                                                                print()
                                                                print(player3.name,"scores 3 for the",Team1.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 12:
                                                                ScoreA+=2
                                                                print()
                                                                print(player3.name,"scores 2 for the",Team1.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 10:
                                                                ScoreA+=1
                                                                print()
                                                                print(player3.name,"scores 1 for the",Team1.name,"!")
                                                                time.sleep(3)
                                                                print()
                                                                print(Team1.name, ": ",ScoreA)
                                                                print()
                                                                print(Team2.name, ": ",ScoreB)
                                                                TeamAPass=0
                                                        else:
                                                                print()
                                                                print("The ",Team2.name,"keeper blocks the shot!")
                                                                TeamAPass=0
                                                                time.sleep(2)                              
                                
                                #If neither a successful pass or an interception occur, the ball is fumbled.

                                else:
                                        print()
                                        print(thirdname,"attempts a catch but fumbles the ball!")
                                        time.sleep(1)
                                        if (player4.name and player1.name in TeamA) or (player4.name and player1.name in TeamB):
                                                print()
                                                print(player4.name,"recovers the ball!")
                                                time.sleep(2)
                                                pos = []
                                                if player4.name in TeamA:
                                                        pos.append('TeamA')
                                                else:
                                                        pos.append('TeamB')

                                        else:
                                                print()
                                                print(player4.name,"grabs the live ball!")
                                                time.sleep(2)
                                                pos = []
                                                if player4.name in TeamA:
                                                        pos.append('TeamA')
                                                else:
                                                        pos.append('TeamB')

                                if player1.name not in newlist:
                                        newlist.append(player1.name)
                                if player2.name not in newlist:
                                        newlist.append(player2.name)
                                if player3.name not in newlist:
                                        newlist.append(player3.name)

                        #This condition occurs when Player 1 fails the strength test against Player 2
                        
                        else: 
                                print()
                                time.sleep(1)
                                if silence <= 7:
                                        silence +=1
                                if silence == 8:
                                        print("A peculiar silence falls over the crowd.")
                                        print()
                                        silence +=1
                                if silence == 9:
                                        print("The silence is palpable.")
                                        print()
                                        silence +=1
                                        
                                if silence == 10:
                                        print("It appears our captains are dispensing Wisdom to their teams.")
                                        print()
                                        time.sleep(2)
                                        silence = 0
                                        die1=dice_roll(4)
                                        die2=dice_roll(4)
                                        Gifted = [PTeamA[die1],PTeamB[die2]]

                                        #Implementation of Captains. Could do more here if Captain attribute was actually assigned to a specific player on each team.

                                        for Player in Gifted:
                                                wheel = ["X",Player.STR,Player.DEX,Player.WIS,Player.CHA,Player.MAG,Player.DMAG]
                                                spin = dice_roll(6)
                                                if spin == 1:
                                                        Player.STR += 1
                                                        print (Player.name,"feels a boost of energy!") 
                                                        print()
                                                        time.sleep(2)
                                                if spin == 2:
                                                        Player.DEX += 1
                                                        print (Player.name,"gets an idea!")
                                                        print()
                                                        time.sleep(2)
                                                if spin == 3:
                                                        Player.WIS += 1
                                                        print (Player.name, "understands.")
                                                        print()
                                                        time.sleep(2)
                                                if spin == 4:
                                                        Player.CHA += 1
                                                        print (Player.name, "keeps spirit!")
                                                        print()
                                                        time.sleep(2)
                                                if spin == 5:
                                                        Player.MAG += 1
                                                        print (Player.name, "learned a spell.")
                                                        print()
                                                        time.sleep(2)
                                                if spin == 6:
                                                        Player.DMAG += 1
                                                        print (Player.name,"has a sly look about them.")
                                                        print()
                                                        time.sleep(2)

                                        print("The Players take to the field!")
                                        print()
                                        time.sleep(2)
                                        silence = 0
                                
                                gameloop()

                        #Sets up conditions for surprise shots on the opponent's ring
                        #When a team has a player in the first and second initiative position, they get a point
                        #When a team has three of these points, the player in the second position takes a surprise shot of opportunity

                        if player1.name in TeamA and player2.name in TeamA:
                                        if Aruncount==0:
                                                print()
                                                print(player1.name, "positions themselves for a shot on the",Team2.name,"Ring!")
                                                time.sleep(2)
                                                Aruncount+=1
                                        elif Aruncount==1:
                                                print()
                                                print("The",Team2.name,"look worried.")
                                                time.sleep(2)
                                                Aruncount+=1
                                        elif Aruncount==2:
                                                print()
                                                print(Team2.name,"need to make a play to stop",player1.name,"!")
                                                time.sleep(2)
                                                Aruncount+=1
                                        else:
                                                time.sleep(2)
                                                # print()
                                                # print ("!A RUN TO THE MAX!")
                                                print()
                                                print(player2.name,"goes for the goal!")
                                                print ("The",Team2.name,"keeper braces.")
                                                time.sleep(3)
                                                roll = dice_roll(20)
                                                kroll = dice_roll(20)
                                                if KeeperB.GK+kroll > player2.DEX+roll:
                                                        print()
                                                        print(KeeperB.name,"saves!")
                                                        TeamAPass=0
                                                        time.sleep(2)
                                                elif player2.DEX+roll >= 20:
                                                        ScoreA+=4
                                                        print()
                                                        print(player2.name,"scores 4 for the",Team1.name,"!")
                                                        time.sleep(3)
                                                        print()
                                                        print(Team1.name, ": ",ScoreA)
                                                        print()
                                                        print(Team2.name, ": ",ScoreB)
                                                        TeamAPass=0
                                                elif player2.DEX+roll >= 15:
                                                        ScoreA+=3
                                                        print()
                                                        print(player2.name,"scores 3 for the",Team1.name,"!")
                                                        time.sleep(3)
                                                        print()
                                                        print(Team1.name, ": ",ScoreA)
                                                        print()
                                                        print(Team2.name, ": ",ScoreB)
                                                        TeamAPass=0
                                                elif player2.DEX+roll >= 12:
                                                        ScoreA+=2
                                                        print()
                                                        print(player2.name,"scores 2 for the",Team1.name,"!")
                                                        time.sleep(3)
                                                        print()
                                                        print(Team1.name, ": ",ScoreA)
                                                        print()
                                                        print(Team2.name, ": ",ScoreB)
                                                        TeamAPass=0
                                                elif player2.DEX+roll >= 10:
                                                        ScoreA+=1
                                                        print()
                                                        print(player2.name,"scores 1 for the",Team1.name,"!")
                                                        time.sleep(3)
                                                        print()
                                                        print(Team1.name, ": ",ScoreA)
                                                        print()
                                                        print(Team2.name, ": ",ScoreB)
                                                        TeamAPass=0
                                                else:
                                                        print()
                                                        print("The",Team2.name,"keeper blocks the shot!")
                                                        TeamAPass=0
                                                        time.sleep(2)
                                                Aruncount=0
                        
                        
                        #Same code but for Team B        

                        elif player1.name in TeamB and player2.name in TeamB:
                                        if Bruncount==0:
                                                print()
                                                print(player1.name, "positions themselves for a shot on the",Team1.name,"Ring!")
                                                time.sleep(2)
                                                Bruncount+=1
                                        elif Bruncount==1:
                                                print()
                                                print("The",Team1.name,"look worried.")
                                                Bruncount+=1
                                        elif Bruncount==2:
                                                print()
                                                print(Team1.name,"need to make a play to stop",player1.name,"!")
                                                Bruncount+=1
                                        else:   
                                                time.sleep(2)
                                                # print()
                                                # print("!B RUN TO THE MAX!")
                                                print()
                                                print(player2.name,"goes for the goal!")
                                                print()
                                                print("The",Team1.name,"keeper braces.")
                                                time.sleep(3)
                                                roll = dice_roll(20)
                                                kroll = dice_roll(20)
                                                if KeeperA.GK+kroll > player2.DEX+roll:
                                                        print()
                                                        print(KeeperA.name,"saves!")
                                                        TeamBPass=0
                                                        time.sleep(2)        
                                                elif player2.DEX+roll >= 20:
                                                        ScoreB+=4
                                                        print()
                                                        print(player2.name,"scores 4 for the",Team2.name,"!")
                                                        time.sleep(3)
                                                        print()
                                                        print(Team1.name, ": ",ScoreA)
                                                        print()
                                                        print(Team2.name, ": ",ScoreB)
                                                        TeamBPass=0
                                                elif player2.DEX+roll >= 15:
                                                        ScoreB+=3
                                                        print()
                                                        print(player2.name,"scores 3 for the",Team2.name,"!")
                                                        time.sleep(3)
                                                        print()
                                                        print(Team1.name, ": ",ScoreA)
                                                        print()
                                                        print(Team2.name, ": ",ScoreB)
                                                        TeamBPass=0
                                                elif player2.DEX+roll >= 12:
                                                        ScoreB+=2
                                                        print()
                                                        print(player2.name,"scores 2 for the",Team2.name,"!")
                                                        time.sleep(3)
                                                        print()
                                                        print(Team1.name, ": ",ScoreA)
                                                        print()
                                                        print(Team2.name, ": ",ScoreB)
                                                        TeamBPass=0
                                                elif player2.DEX+roll >= 10:
                                                        ScoreB+=1
                                                        print()
                                                        print(player2.name,"scores 1 for the",Team2.name,"!")
                                                        time.sleep(3)
                                                        print()
                                                        print(Team1.name, ": ",ScoreA)
                                                        print()
                                                        print(Team2.name, ": ",ScoreB)
                                                        TeamBPass=0
                                                else:
                                                        print()
                                                        print("The",Team1.name,"keeper blocks the shot!")
                                                        TeamBPass=0
                                                        time.sleep(2)
                                                Bruncount=0

                        if player1.name not in newlist:
                                newlist.append(player1.name)
                        if player2.name not in newlist:
                                newlist.append(player2.name)
                        if player3.name not in newlist:
                                newlist.append(player3.name)
                                        
                        
                        #Ensures that players don't tackle other players on their team   

                        while player1.name in TeamA and player2.name in TeamA:
                                Ordered.pop(8)
                                Ordered.insert(0,0,)
                                return Ordered
                        #print()
                        
                        while player1.name in TeamB and player2.name in TeamB:
                                Ordered.pop(8)
                                Ordered.insert(0,0,)
                                return Ordered
                

                        #Ensures players that appeared in this text loop are counted as having taken a turn (moved to newlist)

                        if player1.name not in newlist:
                                newlist.append(player1.name)
                        if player2.name not in newlist:
                                newlist.append(player2.name)
                        if player3.name not in newlist:
                                newlist.append(player3.name) 
                
                checks()

                #Sets scores to current scores before looping again        
                ScoreA=ScoreA
                ScoreB=ScoreB         

        #Creates loop that calls gameloop() for x amount of seconds and prints the final score when game time runs out
        game = True
        this=False
        half=True
        while game == True:
                half=False
                current_time = time.time()
                elapsed_time = current_time - start_time

                if seconds-elapsed_time >= 0:
                        if elapsed_time < seconds-elapsed_time:
                                last = round(seconds-elapsed_time)
                                if round(seconds-elapsed_time) != round(last):
                                        print()
                                        print(round(seconds-elapsed_time))

                # HALF TIME! HALF TIME! HALF TIME! (This makes Half Time work)

                if elapsed_time >= 585 and elapsed_time <= 615:
                        half=True

                while half==True:
                        
                        print()
                        print ("IT'S HALFTIME!")
                        time.sleep(2)
                        count=15
                        while half == True:
                                
                                time.sleep(1)
                                print()
                                print(count)
                                count-=1
                                time.sleep(1)
                                print()
                                print("HALF!")
                                time.sleep(1)
                                print()
                                print(count)
                                time.sleep(1)
                                count-=1
                                print()
                                print("TIME!")
                                time.sleep(1)

                                if count <= 0:
                                        half=False
                                        gameloop()      
                                                        

                gameloop()
                
                #Prints score and winning team at the end of the game time. Counts 30 seconds and then starts a new game.

                if elapsed_time>seconds:
                        print()
                        print("The Game has ended.")
                        print()
                        print(Team1.name,": ",ScoreA)
                        print()
                        print(Team2.name,": ",ScoreB)
                        if ScoreA>ScoreB:
                                print()
                                print(Team1.name,"win the Game.")
                        elif ScoreA<ScoreB:
                                print()
                                print(Team2.name,"win the Game.")
                        else:
                                print()
                                print("The Game ends in a tie.")
                        game = False
                        count = 30
                        this=True                
                while this == True:
                        time.sleep(1)
                        count = count-1
                        print()
                        print(count)
                        if count <= 0:
                                print()
                                print ('Well, I guess that''s tipoff')
                                time.sleep(2)
                                this =False
                                seconds = 1200
                                game = False



