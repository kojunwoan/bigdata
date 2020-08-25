from card import Card
from random import choice
class User:
    def __init__(self,connectionSock,nick):
        self.connectionSock = connectionSock
        self.nick = nick
        self.isTurn = False
        self.isAlive = True
        self.protected = False
        self.selectedCard = None
        self.favorability = 0
        self.prossessionCard = []
        
    def init(self):
        self.isTurn = False
        self.isAlive = True
        self.protected = False
        self.selectedCard = None
        self.prossessionCard = []

    def takeCard(self,card):
        self.prossessionCard.append(card)

    def useCard(self,n):
        if self.prossessionCard[n].type in [5,6] and self.prossessionCard[(n+1)%2].type == 7 or self.prossessionCard[n].type == 8:
            return False
        else:
            self.selectedCard = self.prossessionCard[n]
            self.prossessionCard.remove(self.selectedCard)
            return True

    def execute(self, other=None, grave=None, ext=None):
        note = ""
        if self.selectedCard.type == 1:
            #상대 카드의 랭크와 이름을 모두 맞춰야 한다.
            # note1 = self.nick+"이 "+other.nick+"의 카드를 "+ext+"로 추측하였습니다."#모두
            # note.append(note1)
            if other != None:
                if other.prossessionCard[0].type == ext:
                    other.isAlive = False
                    grave.append([other.prossessionCard[0],-1])
                    other.prossessionCard.remove(other.prossessionCard[0])
                    note = self.nick+"의 공격이 성공하여 "+other.nick+"님이 운명하셨습니다."#모두
                else:
                    note = "{}의 공격({}번 카드)이 {}님에게 실패하였습니다.".format(self.nick,ext,other.nick)#모두
            # note.append(note2)
            # print(self.selectedCard.type, other.prossessionCard[0].type, ext, grave)
            return grave, note
        elif self.selectedCard.type == 2:
            #상대 카드를 본다.
            if other != None:
                note = self.nick+"님이 "+other.nick+"님의 카드를 확인 하였습니다."#모두
            # note.append(note1)
            # note2 = other.nick+"의 카드는 "+other.prossessionCard[0].type+"번 입니다."#본인
            # note.append(note2)
            # print(self.selectedCard.type, other.prossessionCard[0].type)
            return note
        elif self.selectedCard.type == 3:
            #상대 카드와 내 카드의 랭크를 비교하여 작은 사람이 패배한다.
            # note1 = self.nick+"님이 "+other.nick+"님을 대결 상대로 선택하였습니다."#모두
            # note.append(note1)
            if other != None:
                if other.prossessionCard[0].type > self.prossessionCard[0].type:
                    self.isAlive = False
                    grave.append([self.prossessionCard[0],-1])
                    self.prossessionCard.remove(self.prossessionCard[0])
                    note = other.nick+"님이 대결에서 승리하여 "+self.nick+"님이 운명하셨습니다. "#모두
                elif other.prossessionCard[0].type < self.prossessionCard[0].type:
                    other.isAlive = False
                    grave.append([other.prossessionCard[0],-1])
                    other.prossessionCard.remove(other.prossessionCard[0])
                    note = self.nick+"님이 대결에서 승리하여 "+other.nick+"님이 운명하셨습니다. "#모두
            # note.append(note2)
            # print(self.prossessionCard[0].type, other.prossessionCard[0].type, grave)
            return grave, note
        elif self.selectedCard.type == 4:
            #다음 턴까지 방어상태가 된다.
            # note1 = self.nick+"님이 4번 카드를 선택하였습니다"#모두
            # note.append(note1)
            self.protected = True
            note = self.nick+"님은 다음 턴까지 방어상태입니다./다른 플레리어님들은 "+self.nick+"님을 공격할 수 없습니다."#모두
            # note.append(note2)
            # print(self.selectedCard.type, self.protected)
            return note
        elif self.selectedCard.type == 5:
            #대상이 카드를 버리고 새로 뽑습니다.
            # note1 = self.nick+"님 대상을 선택 하십시오."#본인
            # note.append(note1)
            # note2 = self.nick+"님이 5번카드 대상으로 "+other.nick+"님을 지정하였습니다. 현재의 카드를 버리고 새로운 카드를 한장 뽑으세요."#대상
            # note.append(note2)
            if other != None:
                if other.prossessionCard[0].type == 8:
                    other.isAlive= False
                    grave.append([other.prossessionCard[0],-1])
                    other.prossessionCard.remove(other.prossessionCard[0])
                    note = self.nick+"님이 5번카드 대상으로 "+other.nick+"님을 지정하였습니다./"+other.nick+"님의 8번 카드가 공개되며 운명하셨습니다."
                else:
                    grave.append([other.prossessionCard[0],-1])
                    other.prossessionCard.remove(other.prossessionCard[0])
                    if len(ext) != 0:
                        other.prossessionCard.append(choice(ext))
                    else:
                        other.prossessionCard.append(grave[0][0])
                        del grave[0]
                    ext.remove(other.prossessionCard[0])
                    note = self.nick+"님이 5번카드 대상으로 "+other.nick+"님을 지정하였습니다./"+other.nick+"님이 새 카드를 뽑으셨습니다."
            # note.append(note3)
            # print(self.selectedCard.type, other.prossessionCard[0].type, grave)
            return grave, ext, note
        elif self.selectedCard.type == 6:
            #대상의 카드와 나의 카드를 바꿉니다.
            # note1 = self.nick+"님 대상을 선택하십시오."
            # note.append(note1)
            if other != None:
                other.prossessionCard[0], self.prossessionCard[0] = self.prossessionCard[0], other.prossessionCard[0]
                note = self.nick+"님이 6번카드 대상으로 "+other.nick+"님을 지정하였습니다."
            # note.append(note2)
            # print(self.selectedCard.type, other.prossessionCard[0].type, grave)
            return note
        elif self.selectedCard.type == 7:
            # note1 = self.nick+"님이 7번 카드를 선택하셨습니다."
            # note.append(note1)
            # print (self.selectedCard.type)
            return note