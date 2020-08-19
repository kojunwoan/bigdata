from card import Card
class User:
    def __init__(self,connectionSock,nick):
        self.connectionSock = connectionSock
        self.nick = nick
        self.isTurn = False
        self.isAlive = True
        self.isProtect = False
        self.selectedCard = None
        self.prossessionCard = []

    def takeCard(self,card):
        self.prossessionCard.append(card)
        Card.remove(card)

    def useCard(self,n):
        self.selectedCard = self.prossessionCard[n]
        self.prossessionCard.remove(self.selectedCard)


    def execute(self, other, card):
        if self.selectedCard.type == 1:
            #상대 카드의 랭크와 이름을 모두 맞춰야 한다.
            num1 = input()
            if other.prossessionCard[0].type == num1:
                other.isAlive = False
        elif self.selectedCard.type == 2:
            #상대 카드를 본다.
            print(other.prossessionCard[0].type)
        elif self.selectedCard.type == 3:
            #상대 카드와 내 카드의 랭크를 비교하여 작은 사람이 패배한다.
            if other.prossessionCard[0].type > self.prossessionCard[0].type:
                self.isAlive = False
            elif other.prossessionCard[0].type < self.prossessionCard[0].type:
                other.isAlive= False
        elif self.selectedCard.type == 4:
            #다음 턴까지 방어상태가 된다.
            self.isProtect = True
        elif self.selectedCard.type == 5:
            if self.prossessionCard[0].type == 7:
                self.selectedCard.type = self.prossessionCard[0].type
            #대상이 카드를 버리고 새로 뽑습니다.
            else:
                self.takeCard(card) 
        elif self.selectedCard.type == 6:
            if self.prossessionCard[0].type == 7:
                self.selectedCard.type = self.prossessionCard[0].type
            else:
            #대상의 카드와 나의 카드를 바꿉니다.
                self.prossessionCard[0].type, other.prossessionCard[0].type = other.prossessionCard[0].type, self.prossessionCard[0].type
        elif self.selectedCard.type == 8:
            #패에서 낼경우 패배한다.
            self.isAlive = False


            