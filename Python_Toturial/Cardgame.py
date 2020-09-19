class Card:
    def __init__(self, faceNum, suitNum):
        self.faceNum = faceNum if faceNum < 5 and faceNum > 0 else 1
        self.suitNum = suitNum if suitNum < 14 and suitNum > 0 else 1
        self.nameFace = ['Hearts','Diamonds','Spades','Clubs']
        self.nameSuit = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        
 
    def print(self):
        print ("%s of %s" % (self.nameFace[self.faceNum-1], self.nameSuit[self.suitNum-1]))

    def getCard(self):
        return self.nameFace[self.faceNum-1], self.nameSuit[self.suitNum-1]
    
    def getNameSuit(self):
        return self.nameSuit[self.suitNum-1] if self.suitNum-1 != 0 else 1

    def collectable(self, groupOfcards):
        if (groupOfcards.getLen() == 0):
            collectable = False
            
        elif (self.getNameSuit() == "Jack"):
            collectable = True
            for i in range(groupOfcards.getLen()):
                if (groupOfcards.cards[i].getNameSuit() != "Jack"):
                    collectable = False
        elif (self.getNameSuit() == "Queen"):
            collectable = True
            for i in range(groupOfcards.getLen()):
                if (groupOfcards.cards[i].getNameSuit() != "Queen"):
                    collectable = False 
        elif (self.getNameSuit() == "King"):
            collectable = True
            for i in range(groupOfcards.getLen()):
                if (groupOfcards.cards[i].getNameSuit() != "King"):
                    collectable = False
        else:
            cardNum = int(self.getNameSuit())
            collectable = True
            for i in range(groupOfcards.getLen()):
                if (groupOfcards.cards[i].getNameSuit() == "Jack"):
                    collectable = False
                    break
                if (groupOfcards.cards[i].getNameSuit() == "Queen"):
                    collectable = False
                    break
                if (groupOfcards.cards[i].getNameSuit() == "King"):
                    collectable = False
                    break
                if (int(groupOfcards.cards[i].getNameSuit()) != cardNum):
                        collectable = False
            
            sum = 0
            for i in range(groupOfcards.getLen()):
                if (groupOfcards.cards[i].getNameSuit() == "Jack"):
                    collectable = False
                    break
                if (groupOfcards.cards[i].getNameSuit() == "Queen"):
                    collectable = False
                    break
                if (groupOfcards.cards[i].getNameSuit() == "King"):
                    collectable = False
                    break
                sum += int(groupOfcards.cards[i].getNameSuit())
                if (sum == cardNum):
                    collectable = True
                    
        return collectable


class groupOfcards:
    def __init__(self, listOfCards):
        self.cards = listOfCards    
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def print(self):
        for card in self.cards:
            card.print()
            
    def pull(self, indexes):
        indexes.sort()
        for i in range(len(indexes)):
            #indexes = [3,5,1]
            #cards = Diamonds of Ace, Spades of 3, Hearts of 3, Diamonds of 3, Hearts of King, Hearts of 4
            #after sort indexes = [1,3,5]
            #after pop(indexes[i=0]) cards = the same except Diamonds of Ace bc indexes[0] = 1
            #we want to pop out the card of index 3 now 
            #but pop(indexes[i=1]), same as pop(3) ,will result delete Diamonds of 3
            #cards = Spades of 3, Hearts of 3, Hearts of King, Hearts of 4
            #instead of Hearts of 3 or having cards = Spades of 3, Diamonds of 3, Hearts of King, Hearts of 4
            #so we need to pop out (indexes[1]-1-1) that is pop(indexes[i]-i-1)
            self.cards.pop(indexes[i]-i-1)
        
    def addCards(self, goc): 
        if (len(goc.cards) != 0):
            for i in range(len(goc.cards)):
                self.cards.append(goc.cards[i])

             
    def getLen(self):
        return len(self.cards)
        
    def getCardsByIndexs(self, indexes):
        lis = []
        indexes.sort()
        for i in range(len(indexes)):
            lis.append(self.cards[indexes[i]-1])
        return groupOfcards(lis)
    
    def indexExist (self,lis):
        exist = True
        for i in range(len(lis)):
            #indexes from the user perspective starts from 1
            if (lis[i]-1 > len(self.cards)):
                exist = False
        if (len(lis) == 0):
            exist = False
        return exist
    
    def getRondom(self):
        indexes = []
        NumberOfRandomCards = randrange(self.getLen())+1
        for i in range(NumberOfRandomCards):
            indexes.append(randrange(self.getLen()))

        return self.getCardsByIndexs(indexes)


class Deck:
    def __init__(self):
        self.deck = self.createDeck()
        
    def createDeck(self):
        deck = []
        for suitNum in range(1,14):
            for faceNum in range(1,5):
                #print(faceNum,suitNum)
                deck.append(Card(faceNum, suitNum))
        return deck        
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def print(self):
        for card in self.deck:
            card.print()
            
    #Returns object goc
    def pull(self, n):
        
        pullList = []
        for i in range(n):
            if (len(self.deck) != 0):
                pullList.append(self.deck.pop())
        goc = groupOfcards(pullList)
        return goc


