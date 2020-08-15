from card import Card
class User:
    def __init__(self,connectionSock,nick):
        self.connectionSock = connectionSock
        self.nick = nick
        self.isTurn = False
        self.isAlive = True
        self.isProtect = False
        self.prossessionCard = []

    def takeCard(self,card):
        self.prossessionCard.append(card)

    def useCard(self,n):
        card = self.prossessionCard[n]
        self.prossessionCard.remove(card)
        return card

    def execute(self, other, card):
        if card.type == 1:
            #상대 카드의 랭크와 이름을 모두 맞춰야 한다.
            num1 = input()
            if other.prossessionCard[0].type == num1:
                other.isAlive = False
        elif card.type == 2:
            #상대 카드를 본다.
            print(other.prossessionCard[0].type)
        elif card.type == 3:
            #상대 카드와 내 카드의 랭크를 비교하여 작은 사람이 패배한다.
            if self.prossessionCard[0].type > self.prossessionCard[0].type:
                other.isAlive = False
            elif self.prossessionCard[0].type < self.prossessionCard[0].type:
                self.isAlive= False
        elif card.type == 4:
            #다음 턴까지 방어상태가 된다.
            self.isProtect = True
        elif card.type == 5:
            #대상이 카드를 버리고 새로 뽑습니다.
            if card.type == self.prossessionCard[0].type:
                self.isAlive = False
            else: 
                other.isAlive = False
        elif self.type == 6:
            #대상의 카드와 나의 카드를 바꿉니다.
            pass
        elif self.type == 7:
            #5번이나 6번카드를 들고 있을 경우 반드시 내야합니다.
            pass
        elif self.type == 8:
            #패에서 낼경우 패배한다.
            pass
