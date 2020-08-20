from card import Card
from server import server
from random import choice
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


    def execute(self, other, grave, ext=None):
        if self.selectedCard.type == 1:
            #상대 카드의 랭크와 이름을 모두 맞춰야 한다.
            # note1 = self.nick+"이 "+other.nick+"의 카드를 "+card+"로 추측하였습니다."
            if other.prossessionCard[0].type == ext:
                other.isAlive = False
                grave.append([other.prossessionCard[0],-1])
                # note2 = self.nick+"의 공격이 성공하여 "+other.nick+"님이 운명하셨습니다."
            # else:
                # note2 = self.nick+"의 공격이 실패하였습니다."   
            # return note1,note2,1,2,3,4
        elif self.selectedCard.type == 2:
            #상대 카드를 본다.
            # note1 = self.nick+"님이 "+other.nick+"님의 카드를 선택하였습니다."
            print(other.prossessionCard[0].type)
            # note2 = other.nick+"의 카드는 "+other.prossessionCard[0].type+"번 입니다."
            # return note1, note2, self.nick??
        elif self.selectedCard.type == 3:
            #상대 카드와 내 카드의 랭크를 비교하여 작은 사람이 패배한다.
            # note1 = self.nick+"님이 "+other.nick+"님을 대결 상대로 선택하였습니다."
            if other.prossessionCard[0].type > self.prossessionCard[0].type:
                self.isAlive = False
                grave.append([self.prossessionCard[0],-1])
                # note2 = other.nick+"님이 대결에서 승리하여 "+self.nick+"님이 운명하셨습니다. "
            elif other.prossessionCard[0].type < self.prossessionCard[0].type:
                other.isAlive = False
                grave.append([other.prossessionCard[0],-1])
                # note2 = self.nick+"님이 대결에서 승리하여 "+other.nick+"님이 운명하셨습니다. "
            # return note1,note2,1,2,3,4
        elif self.selectedCard.type == 4:
            #다음 턴까지 방어상태가 된다.
            # note1 = self.nick+"님이 4번 카드를 선택하였습니다"
            self.isProtect = True
            # note2 = self.nick+"님은 다음 턴까지 방어상태입니다. 다른 플레리어님들은 "+self.nick+"님을 공격할 수 없습니다."
            # return note1, note2
        elif self.selectedCard.type == 5:
            #대상이 카드를 버리고 새로 뽑습니다.
            # note1 = self.nick+"님 대상을 선택 하십시오."
            # note2 = self.nick+"님이 5번카드 대상으로 "+other.nick+"님을 지정하였습니다. 현재의 카드를 버리고 새로운 카드를 한장 뽑으세요."
            if other.prossessionCard[0].type == 8:
                other.isAlive= False
                grave.append([other.prossessionCard[0],-1])
                # note3 = other.nick"님의 8번 카드가 공개되며 운명하셨습니다."
            else:
                grave.append([other.prossessionCard[0],-1])
                other.prossessionCard.append(choice(ext))
                ext.remove(other.prossessionCard[0])
                # note3 = other.nick+"님이 새 카드를 뽑으셨습니다."
            # return note1, note2, note3
        elif self.selectedCard.type == 6:
            #대상의 카드와 나의 카드를 바꿉니다.
            # note1 = self.nick+"님 대상을 선택하십시오."
            self.prossessionCard[0].type, other.prossessionCard[0].type = other.prossessionCard[0].type, self.prossessionCard[0].type
            # note2 = self.nick+"님이 6번카드 대상으로 "+other.nick+"님을 지정하였습니다."+self.nick+"님과 카드를 교환하세요."
            # return note1, note2


            

