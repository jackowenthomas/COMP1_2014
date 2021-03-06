# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014


import random
import datetime

NO_OF_RECENT_SCORES = 10

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ''

Deck = [None]
RecentScores = [None]
Choice = ''
RankOfAce = False


def GetRank(RankNo):
  Rank = ''
  if RankNo == 1 or RankNo == 14:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print('6. Save high scores')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def DisplayOptions():
  print()
  print('OPTIONS MENU')
  print()
  print('1. Set Ace to be HIGH or LOW')
  print()
  

def GetOptionsChoice():
  OptionChoice = input('Select an option from the menu (or enter q to quit): ')
  print()
  return OptionChoice

def SetOptionsChoice(OptionChoice):
  if OptionChoice == '1':
    SetAceHighOrLow()
 
def SetAceHighOrLow():
  global RankOfAce
  HighOrLow = input('Do you want Ace to be (h)igh or (l)ow: ')
  HighOrLow = HighOrLow.lower()[0]
  if HighOrLow == 'h':
    RankOfAce = True
    DisplayMenu()
  elif HighOrLow == 'l':
    RankOfAce = False
    DisplayMenu()
    
def GetMenuChoice():
  Choice = input()
  
  print()
  return Choice.lower()

def LoadDeck(Deck):
  global RankOfAce
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if RankOfAce == True and Deck[Count].Rank == 1:
      Deck[Count].Rank = 14
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('You got the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  ValidName = False
  while not ValidName:
    NameCheck = input("Do you want to save your score to the high score table? (enter y or n)? ")
    if NameCheck == "n":
      DisplayMenu()
    elif NameCheck == "y":
      PlayerName = input("Please enter your name: ")
      if len(PlayerName) > 0:
        ValidName = True
        DisplayMenu()
        return PlayerName
      
      
    print()
    
    

    

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  while len(Choice) == 0:
    Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  Choice = Choice [0]
  return Choice.lower()


def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = ''
  

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("{0:<10} {1:<10} {2:<10}".format("Name","Score","Date"))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<10} {1:<10} {2:<10}".format(RecentScores[Count].Name,RecentScores[Count].Score,RecentScores[Count].Date))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  DisplayMenu()
  print()

def BubbleSortScores(RecentScores):
   unsorted = True
   while unsorted:
        unsorted = False
        for Count in range(1,len(RecentScores)-1):
          if RecentScores[Count].Score < RecentScores[Count + 1].Score:
            hold = RecentScores[Count + 1]
            RecentScores[Count + 1] = RecentScores[Count]
            RecentScores[Count] = hold
            unsorted = True
   return RecentScores          

def UpdateRecentScores(RecentScores, Score):
  PlayerName = GetPlayerName()
  FoundSpace = False
  TodaysDate = datetime.date.today()
  Date = datetime.date.strftime(TodaysDate,"%d/%m/%y")
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
      RecentScores[Count].Score = RecentScores[Count + 1].Date
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  RecentScores[Count].Date = Date

def SaveScores(RecentScores):
  with open ("save_scores.txt", mode="r", encoding="utf-8"):

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  DisplayMenu()
  while Choice != 'q':
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionsChoice()
      if OptionChoice == '1':
        SetAceHighOrLow()
    elif Choice == '6':
      SaveScores(RecentScores)
      
