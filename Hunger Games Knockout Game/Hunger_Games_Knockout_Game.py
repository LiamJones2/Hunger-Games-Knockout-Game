#necessary imports
from os import path

import time

import os

import sys

import random



#sets time to wait and follows time.sleep
timeToWait = 1

amountOfCharacters = 0

#clears the console
clearConsole = lambda: print('\n' * 150)

file_exists = os.path.exists('statsfile.txt')

clearConsole()

#checks if file exists, if it does then continue but if not then it makes the file needed to store stats and previous winners
if (file_exists):
    print("Your back!")
else:
    print("Welcome for the first time :)")
    time.sleep(timeToWait)
    with open('statsfile.txt','w+') as f:
        f.writelines("Total games completed: 0")
        f.writelines("\n")
        f.writelines("Coins = 200")
        f.writelines("\n")
        f.writelines("Stored winners:")
        f.writelines("\n")

with open('character stats.txt','w+') as f:
        pass

def getStartingCoins():
    with open('statsfile.txt','r') as f:
        content = f.readlines()
        coins = content[1]
        stringMinus = "Coins = "
        if stringMinus in coins:
            coinsTotal = int(coins.replace(stringMinus,''))
        print(coinsTotal)



def welcomeToGame():
    print("Welcome to the Hunger Knockout Game")
    time.sleep(timeToWait)
    print("Ultimate Hunger Knockout Game is unavailable")
    time.sleep(timeToWait)
    print("Type commands at any point to see the commands")
    time.sleep(timeToWait)
    clearConsole()


#menu for the application. Users can either start, get their stats or quit the application
def menu():
    clearConsole()
    print("Welcome to the menu")
    print("Type start to start")
    print("Type stats to get your stats")
    print("Type quit to quit your game")
    getStartingCoins()

    command = input()
    if command == "start":
         startNormalGame()
    elif command == "stats":
        getUsersStats()
    elif command == "quit":
        sys.exit()
    else:
         print("Sorry please try that again")
         time.sleep(2)
         menu()


#gets stats when requested from menu and prints out all stats from file called statsfile.txt that was made
def getUsersStats():
    clearConsole()
    a_file = open("statsfile.txt")
    lines = a_file.readlines()
    for line in lines:
        print(line)
    input("Press enter to go back to the Menu")

    menu()



#starts game, gets character names,character culture and character stats
def startNormalGame():
    print("Loading the sixteen characters...")
    countOfCharacters = 0
    while countOfCharacters < 16:
        newCharacter = creatingCharacters()
        print("New challenger appears: {}".format(newCharacter))
        with open('character stats.txt','a+',encoding="utf-8") as characterStatsFile:
            characterStatsFile.writelines(newCharacter)
            characterStatsFile.writelines('\n')
            characterStats = createCharacterStats()
            characterStrength = str(characterStats[0])
            characterAttack = str(characterStats[1])
            characterVitality = str(characterStats[2])
            characterSpeed = str(characterStats[3])

            characterStatsFile.writelines(characterStrength)
            characterStatsFile.writelines('\n')
            characterStatsFile.writelines(characterAttack)
            characterStatsFile.writelines('\n')
            characterStatsFile.writelines(characterVitality)
            characterStatsFile.writelines('\n')
            characterStatsFile.writelines(characterSpeed)
            characterStatsFile.writelines('\n')

                
        countOfCharacters += 1


def creatingCharacters():
    cultureOfCharacter = random.randint(1,6)
    if cultureOfCharacter == 1:
        character = createCaveman()
        return character
    elif cultureOfCharacter == 2:
        character = createEgyptian()
        return character
    elif cultureOfCharacter == 3:
        character = createSpartan()
        return character
    elif cultureOfCharacter == 4:
        character = createSamurai()
        return character
    elif cultureOfCharacter == 5:
        character = createRoman()
        return character
    elif cultureOfCharacter == 6:
        character = createBritish() 
        return character

def createCaveman():
    firstPartOfCavemanNameList = ['Tso','Stud','Od','Fed','U','Dra','Fey','Iz','Daa','Gho','Og','Cus','Dre','Dro','Dra']
    secondPartOfCavemanNameList = ['kos','col','rall','g','g','ia','uh','oe','lab','no','ic','ur','e','rua','ve']
    return firstPartOfCavemanNameList[random.randint(0,len(firstPartOfCavemanNameList)-1)] + secondPartOfCavemanNameList[random.randint(0,len(firstPartOfCavemanNameList)-1)] + " the caveman"

def createEgyptian():
    EgyptianNameList = ['Satemi','Jabari','Kaa','Hanif','Neith','Tefnut','Edfu','Pesahi','Rekh-mara','Ubaid','Khet-ui','Ra-to','Sensaos','Pthah-se','Akil','Huni','Uta-hor',
                        'Ra-pioses','Ra-tmeto','Amenheratf','Mehi','Bubastis','Nub-na','Sa-khons','Echidna']
    return EgyptianNameList[random.randint(0,len(EgyptianNameList)-1)] + " the Egyptian"

def createSpartan():
    firstPartOfSpartanNameList = ['Valentinos','Aggelos','Aris','Sergios','Marinos','Epameinondas','Neofytos','Andreas','Andrianos','Emmanouil','Cybele','Eva','Melina','Yeorgia','Ifigenia']
    secondPartOfSpartanNameList = [' Vlahotis',' Barakos',' Zerveas',' Mellotis',' Georgotis',' Apostolas',' Pagonallis',' Calloulis',' Maras',' Stathoulis',' Kaneli',' Kallouli',' Zorbide',' Dimou',' Boosalidi']
    return firstPartOfSpartanNameList[random.randint(0,len(firstPartOfSpartanNameList)-1)] + secondPartOfSpartanNameList[random.randint(0,len(firstPartOfSpartanNameList)-1)] + " the Spartan"

def createSamurai():
    firstPartOfSamuraiNameList = ['Shigeru','Taiho','Hisame','Hayato','Kikai','Hayato','Hatori','Sota','Hikari','Daichi','Kossori','Ketsueki','Hideki','Raion','Takeo']
    secondPartOfSamuraiNameList = [' Sairentojetto',' Honzo',' Fukuro',' Burakkuraitoningu',' Aisuhanma',' Faiyajetto',' Kuroitanken',' Nosuri',' Shizukanaiki',' Mayonaka',' Sandahaundo',' Bakuhatsu',' Faiamonsuta',' Sandajetto',' Sairentobomu']
    return firstPartOfSamuraiNameList[random.randint(0,len(firstPartOfSamuraiNameList)-1)] + secondPartOfSamuraiNameList[random.randint(0,len(firstPartOfSamuraiNameList)-1)] + " the Samurai"

def createRoman():
    firstPartOfRomanNameList = ['Alaricus','Horatio','Ferox','Callias','Flavian','Hersilia','Nigellus','Gemini','Idetta','Severus','Meleager','Ursinus','Herodotus','Cronus','Iphigenia']
    secondPartOfRomanNameList = [' Balbus',' Publicola',' Augur',' Laevinus',' Mucanius',' Hispaniensis',' Acidinus',' Barbatus',' Orca',' Cunctator',' Messala',' Arquetius',' Niger',' Sergianus',' Atticus']
    return firstPartOfRomanNameList[random.randint(0,len(firstPartOfRomanNameList)-1)] + secondPartOfRomanNameList[random.randint(0,len(firstPartOfRomanNameList)-1)] + " the Roman"

def createBritish():
    firstPartOfBritishNameList = ['Clive','Fern','Marley','Cedrica','Candace','Frideswide','Haiden','Eardwulf','Erline','Gleda','Wynnstan','Chaney','Braeden','Melric','Allura']
    secondPartOfBritishNameList = [' Beverlye',' Harlowe',' Kimberlye',' Hayleye',' Wolfee',' Wright',' Pressleye',' Airaldii',' Stonee',' Hayes',' Wintere',' Wellse',' Easome',' Turnbulle',' Harrisone']
    return firstPartOfBritishNameList[random.randint(0,len(firstPartOfBritishNameList)-1)] + secondPartOfBritishNameList[random.randint(0,len(firstPartOfBritishNameList)-1)] + " from the British Empire"

#caveman
#egyptian
#greek/spartan
#samurai
#roman
#british


def createCharacterStats():
    characterStats = ['0','0','0','0']
    #strength stat
    characterStats[0] = str(random.randint(1,20))+' '
    #attack stat
    characterStats[1] = str(random.randint(1,20))+' '
    #vitality stat
    characterStats[2] = str(random.randint(10,30))+' '
    #speed stat
    characterStats[3] = str(random.randint(1,20))+' '
    return characterStats


def getCharacterName(numberCharacter):
    with open('character stats.txt','r') as gettingCharacterName:
        content = gettingCharacterName.readlines()
        characterName = content[numberCharacter]
        return characterName


def getCharacterStrength(numberStrength):
    with open('character stats.txt','r') as gettingCharacterStrength:
        content = gettingCharacterStrength.readlines()
        characterStrength = content[numberStrength]
        return int(characterStrength)

def getCharacterAttack(numberAttack):
    with open('character stats.txt','r') as gettingCharacterAttack:
        content = gettingCharacterAttack.readlines()
        characterAttack = content[numberAttack]
        return int(characterAttack)

def getCharacterVitality(numberVitality):
    with open('character stats.txt','r') as gettingCharacterVitality:
        content = gettingCharacterVitality.readlines()
        characterVitality = content[numberVitality]
        return int(characterVitality)

def getCharacterSpeed(numberSpeed):
    with open('character stats.txt','r') as gettingCharacterSpeed:
        content = gettingCharacterSpeed.readlines()
        characterSpeed = content[numberSpeed]
        return int(characterSpeed)

def fightSetup(participantOneName,participantOneStrength,participantOneAttack,participantOneVitality,participantOneSpeed,participantTwoName,participantTwoStrength,participantTwoAttack,participantTwoVitality,participantTwoSpeed, idOne,idTwo,round):
    clearConsole()
    print(round)
    print("Please welcome " + participantOneName + "to the battle arena")
    time.sleep(timeToWait)
    print("Their strength is {}".format(participantOneStrength))
    time.sleep(timeToWait)
    print("Their attack is {}".format(participantOneAttack))
    time.sleep(timeToWait)
    print("Their vitality is {}".format(participantOneVitality))
    time.sleep(timeToWait)
    print("Their speed is {}".format(participantOneSpeed))
    time.sleep(timeToWait)
    print("VERSUS")
    time.sleep(timeToWait)
    print("Please welcome " + participantTwoName + "to the battle arena")
    time.sleep(timeToWait)
    print("Their strength is {}".format(participantTwoStrength))
    time.sleep(timeToWait)
    print("Their attack is {}".format(participantTwoAttack))
    time.sleep(timeToWait)
    print("Their vitality is {}".format(participantTwoVitality))
    time.sleep(timeToWait)
    print("Their speed is {}".format(participantTwoSpeed))
    time.sleep(timeToWait)
    print("Would you like to place any bets?")
    winner = startFight(participantOneName,int(participantOneStrength),int(participantOneAttack),int(participantOneVitality),int(participantOneSpeed),participantTwoName,int(participantTwoStrength),int(participantTwoAttack),int(participantTwoVitality),int(participantTwoSpeed),idOne,idTwo)
    return winner


def startFight(participantOneName,participantOneStrength,participantOneAttack,participantOneHealth,participantOneSpeed,participantTwoName,participantTwoStrength,participantTwoAttack,participantTwoHealth,participantTwoSpeed,idOne,idTwo):
    print("The fight has begun")
    with open('character stats.txt','r') as returningWinner:
        content = returningWinner.readlines()
        winnerCheck = content[idOne[0]]
    #if headsOrTails == 1 then participantOne goes first, else participantTwo goes first 
    if participantOneSpeed >= participantTwoSpeed:
        while (participantOneHealth > 0 and participantTwoHealth > 0):
            hitOrNot = hitOrNotCalled(participantOneAttack,participantOneStrength)
            if hitOrNot == "Hit":
                damage = howMuchDamage(participantOneStrength)
                participantTwoHealth -= damage
                print("{} hits {} by {}".format(participantOneName,participantTwoName,damage))
                time.sleep(timeToWait)
                if participantTwoHealth <= 0:
                    winner = participantOneName
                    winnerCheck = content[idOne[0]]
                    break
            else:
                print("Miss!")
                time.sleep(timeToWait)
            hitOrNot = hitOrNotCalled(participantTwoAttack,participantTwoStrength)
            if hitOrNot == "Hit":
                damage = howMuchDamage(participantTwoStrength)
                participantOneHealth -= damage
                print("{} hits {} by {}".format(participantTwoName,participantOneName,damage))
                time.sleep(timeToWait)
                if participantOneHealth <= 0:
                    winner = participantTwoName
                    winnerCheck = content[idTwo[0]]
                    break
            else:
                print("Miss!")
                time.sleep(timeToWait)
            
    else:
        while(participantOneHealth > 0 and participantTwoHealth > 0):
            hitOrNot = hitOrNotCalled(participantTwoAttack,participantTwoStrength)
            if hitOrNot == "Hit":
                damage = howMuchDamage(participantTwoStrength)
                participantOneHealth -= damage
                print("{} hits {} by {}".format(participantTwoName,participantOneName,damage))
                time.sleep(timeToWait)
                if participantOneHealth <= 0:
                    winner = participantTwoName
                    winnerCheck = content[idTwo[0]]
                    break
            else:
                print("Miss!")
                time.sleep(timeToWait)
            hitOrNot = hitOrNotCalled(participantOneAttack,participantOneStrength)
            if hitOrNot == "Hit":
                damage = howMuchDamage(participantOneStrength)
                participantTwoHealth -= damage
                print("{} hits {} by {}".format(participantOneName,participantTwoName,damage))
                time.sleep(timeToWait)
                if participantTwoHealth <= 0:
                    winner = participantOneName
                    winnerCheck = content[idOne[0]]
                    break
            else:
                print("Miss!")
                time.sleep(timeToWait)


    print("The winner is {}".format(winner))
    input("Press enter to continue")
    if winnerCheck in participantTwoName:
         return idTwo
    else:
         return idOne


def hitOrNotCalled(participantAttack,participantStrength):
    hit = 50 + (participantAttack*2.5)
    hitChance = random.randint(1,100)
    if hitChance > hit:
        return "noHit"
    else:
        return "Hit"


def howMuchDamage(participantStrength):
    damageChanceHigh = participantStrength + 10
    if damageChanceHigh > 20:
        damageChanceHigh = 20
    damageChanceLow = participantStrength - 10
    if damageChanceLow < 1:
        damageChanceLow = 1
    damageDealt = random.randint(damageChanceLow,damageChanceHigh)
    return damageDealt

def bet():
    if (coins > 0):
        pass

    
    


'''
Calling the functions that start the application after all functions have been read
'''
welcomeToGame()

menu()

#Round of 16 starts here

winnerOfFirstRoundOfSixteen = fightSetup(getCharacterName(0),getCharacterStrength(1),getCharacterAttack(2),getCharacterVitality(3),getCharacterSpeed(4),getCharacterName(5),getCharacterStrength(6),getCharacterAttack(7),getCharacterVitality(8),getCharacterSpeed(9),(0,1,2,3,4),(5,6,7,8,9),"First round of 16")



winnerOfSecondRoundOfSixteen = fightSetup(getCharacterName(10),getCharacterStrength(11),getCharacterAttack(12),getCharacterVitality(13),getCharacterSpeed(14),getCharacterName(15),getCharacterStrength(16),getCharacterAttack(17),getCharacterVitality(18),getCharacterSpeed(19),(10,11,12,13,14),(15,16,17,18,19),"Second round of 16")


winnerOfThirdRoundOfSixteen = fightSetup(getCharacterName(20),getCharacterStrength(21),getCharacterAttack(22),getCharacterVitality(23),getCharacterSpeed(24),getCharacterName(25),getCharacterStrength(26),getCharacterAttack(27),getCharacterVitality(28),getCharacterSpeed(29),(20,21,22,23,24),(25,26,27,28,29),"Third round of 16")


winnerOfFourthRoundOfSixteen = fightSetup(getCharacterName(30),getCharacterStrength(31),getCharacterAttack(32),getCharacterVitality(33),getCharacterSpeed(34),getCharacterName(35),getCharacterStrength(36),getCharacterAttack(37),getCharacterVitality(38),getCharacterSpeed(39),(30,31,32,33,34),(35,36,37,38,39),"Fourth round of 16")


winnerOfFifthRoundOfSixteen = fightSetup(getCharacterName(40),getCharacterStrength(41),getCharacterAttack(42),getCharacterVitality(43),getCharacterSpeed(44),getCharacterName(45),getCharacterStrength(46),getCharacterAttack(47),getCharacterVitality(48),getCharacterSpeed(49),(40,41,42,43,44),(45,46,47,48,49),"Fifth round of 16")


winnerOfSixthRoundOfSixteen = fightSetup(getCharacterName(50),getCharacterStrength(51),getCharacterAttack(52),getCharacterVitality(53),getCharacterSpeed(54),getCharacterName(55),getCharacterStrength(56),getCharacterAttack(57),getCharacterVitality(58),getCharacterSpeed(59),(50,51,52,53,54),(55,56,57,58,59),"Sixth round of 16")



winnerOfSeventhRoundOfSixteen = fightSetup(getCharacterName(60),getCharacterStrength(61),getCharacterAttack(62),getCharacterVitality(63),getCharacterSpeed(64),getCharacterName(65),getCharacterStrength(66),getCharacterAttack(67),getCharacterVitality(68),getCharacterSpeed(69),(60,61,62,63,64),(65,66,67,68,69),"Seventh round of 16")



winnerOfEighthRoundOfSixteen = fightSetup(getCharacterName(70),getCharacterStrength(71),getCharacterAttack(72),getCharacterVitality(73),getCharacterSpeed(74),getCharacterName(75),getCharacterStrength(76),getCharacterAttack(77),getCharacterVitality(78),getCharacterSpeed(79),(70,71,72,73,74),(75,76,77,78,79),"Eighth round of 16")



#Quarter finals start here

winnerOfFirstQuarterFinal = fightSetup(getCharacterName(winnerOfFirstRoundOfSixteen[0]),getCharacterStrength(winnerOfFirstRoundOfSixteen[1]),getCharacterAttack(winnerOfFirstRoundOfSixteen[2]),getCharacterVitality(winnerOfFirstRoundOfSixteen[3]),getCharacterSpeed(winnerOfFirstRoundOfSixteen[4])
                                       ,getCharacterName(winnerOfSecondRoundOfSixteen[0]),getCharacterStrength(winnerOfSecondRoundOfSixteen[1]),getCharacterAttack(winnerOfSecondRoundOfSixteen[2]),getCharacterVitality(winnerOfSecondRoundOfSixteen[3]),getCharacterSpeed(winnerOfSecondRoundOfSixteen[4])
                                       ,winnerOfFirstRoundOfSixteen,winnerOfSecondRoundOfSixteen,"First quarter final")


winnerOfSecondQuarterFinal = fightSetup(getCharacterName(winnerOfThirdRoundOfSixteen[0]),getCharacterStrength(winnerOfThirdRoundOfSixteen[1]),getCharacterAttack(winnerOfThirdRoundOfSixteen[2]),getCharacterVitality(winnerOfThirdRoundOfSixteen[3]),getCharacterSpeed(winnerOfThirdRoundOfSixteen[4])
                                       ,getCharacterName(winnerOfFourthRoundOfSixteen[0]),getCharacterStrength(winnerOfFourthRoundOfSixteen[1]),getCharacterAttack(winnerOfFourthRoundOfSixteen[2]),getCharacterVitality(winnerOfFourthRoundOfSixteen[3]),getCharacterSpeed(winnerOfFourthRoundOfSixteen[4])
                                       ,winnerOfThirdRoundOfSixteen,winnerOfFourthRoundOfSixteen,"Second quarter final")


winnerOfThirdQuarterFinal = fightSetup(getCharacterName(winnerOfFifthRoundOfSixteen[0]),getCharacterStrength(winnerOfFifthRoundOfSixteen[1]),getCharacterAttack(winnerOfFifthRoundOfSixteen[2]),getCharacterVitality(winnerOfFifthRoundOfSixteen[3]),getCharacterSpeed(winnerOfFifthRoundOfSixteen[4])
                                       ,getCharacterName(winnerOfSixthRoundOfSixteen[0]),getCharacterStrength(winnerOfSixthRoundOfSixteen[1]),getCharacterAttack(winnerOfSixthRoundOfSixteen[2]),getCharacterVitality(winnerOfSixthRoundOfSixteen[3]),getCharacterSpeed(winnerOfSixthRoundOfSixteen[4])
                                       ,winnerOfFifthRoundOfSixteen,winnerOfSixthRoundOfSixteen,"Third quarter final")


winnerOfFourthQuarterFinal = fightSetup(getCharacterName(winnerOfSeventhRoundOfSixteen[0]),getCharacterStrength(winnerOfSeventhRoundOfSixteen[1]),getCharacterAttack(winnerOfSeventhRoundOfSixteen[2]),getCharacterVitality(winnerOfSeventhRoundOfSixteen[3]),getCharacterSpeed(winnerOfSeventhRoundOfSixteen[4])
                                       ,getCharacterName(winnerOfEighthRoundOfSixteen[0]),getCharacterStrength(winnerOfEighthRoundOfSixteen[1]),getCharacterAttack(winnerOfEighthRoundOfSixteen[2]),getCharacterVitality(winnerOfEighthRoundOfSixteen[3]),getCharacterSpeed(winnerOfEighthRoundOfSixteen[4])
                                       ,winnerOfSeventhRoundOfSixteen,winnerOfEighthRoundOfSixteen,"Fourth quarter final")



#Semi finals start here
winnerOfFirstSemiFinal = fightSetup(getCharacterName(winnerOfFirstQuarterFinal[0]),getCharacterStrength(winnerOfFirstQuarterFinal[1]),getCharacterAttack(winnerOfFirstQuarterFinal[2]),getCharacterVitality(winnerOfFirstQuarterFinal[3]),getCharacterSpeed(winnerOfFirstQuarterFinal[4])
                                       ,getCharacterName(winnerOfSecondQuarterFinal[0]),getCharacterStrength(winnerOfSecondQuarterFinal[1]),getCharacterAttack(winnerOfSecondQuarterFinal[2]),getCharacterVitality(winnerOfSecondQuarterFinal[3]),getCharacterSpeed(winnerOfSecondQuarterFinal[4])
                                       ,winnerOfFirstQuarterFinal,winnerOfSecondQuarterFinal,"First semi final")


winnerOfSecondSemiFinal = fightSetup(getCharacterName(winnerOfThirdQuarterFinal[0]),getCharacterStrength(winnerOfThirdQuarterFinal[1]),getCharacterAttack(winnerOfThirdQuarterFinal[2]),getCharacterVitality(winnerOfThirdQuarterFinal[3]),getCharacterSpeed(winnerOfThirdQuarterFinal[4])
                                       ,getCharacterName(winnerOfFourthQuarterFinal[0]),getCharacterStrength(winnerOfFourthQuarterFinal[1]),getCharacterAttack(winnerOfFourthQuarterFinal[2]),getCharacterVitality(winnerOfFourthQuarterFinal[3]),getCharacterSpeed(winnerOfFourthQuarterFinal[4])
                                       ,winnerOfThirdQuarterFinal,winnerOfFourthQuarterFinal,"Second semi final")


#THE FINAL 

winnerOfFinal = fightSetup(getCharacterName(winnerOfFirstSemiFinal[0]),getCharacterStrength(winnerOfFirstSemiFinal[1]),getCharacterAttack(winnerOfFirstSemiFinal[2]),getCharacterVitality(winnerOfFirstSemiFinal[3]),getCharacterSpeed(winnerOfFirstSemiFinal[4])
                                       ,getCharacterName(winnerOfSecondSemiFinal[0]),getCharacterStrength(winnerOfSecondSemiFinal[1]),getCharacterAttack(winnerOfSecondSemiFinal[2]),getCharacterVitality(winnerOfSecondSemiFinal[3]),getCharacterSpeed(winnerOfSecondSemiFinal[4])
                                       ,winnerOfFirstSemiFinal,winnerOfSecondSemiFinal,"THE FINAL!")


with open('character stats.txt','r') as returningWinner:
    content = returningWinner.readlines()
    name = content[winnerOfFinal[0]]
    print("THE GRAND CHAMPION IS {}".format(name))
    winnerName = content[winnerOfFinal[0]]
    winnerStrength = content[winnerOfFinal[1]]
    print(winnerStrength)
    winnerAttack = content[winnerOfFinal[2]]
    winnerVitality = content[winnerOfFinal[3]]
    winnerSpeed = content[winnerOfFinal[4]]
    with open('statsfile.txt','a') as storingWinner:
        content = storingWinner
        print(winnerOfFinal)
        storingWinner.writelines(winnerName)
        storingWinner.writelines(winnerStrength)
        storingWinner.writelines(winnerAttack)
        storingWinner.writelines(winnerVitality)
        storingWinner.writelines(winnerSpeed)
        with open("statsfile.txt") as f:
            lines = f.readlines()

        numberOfGamesCompleted = lines[0]
        print(numberOfGamesCompleted)
        numberOfGames = numberOfGamesCompleted
        removeOldNumberOfGames = 'Total games completed: '
        if removeOldNumberOfGames in numberOfGames:
            numberOfGames = int(numberOfGames.replace(removeOldNumberOfGames,''))
        numberOfGames += 1
        print(numberOfGames)

        lines # ['This is the first line.\n', 'This is the second line.\n']

        lines[0] = "Total games completed: " + str(numberOfGames) + "\n"

        lines # ["This is the line that's replaced.\n", 'This is the second line.\n']

        with open("statsfile.txt", "w") as f:
            f.writelines(lines)



