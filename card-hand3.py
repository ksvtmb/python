class Card(object):
    """ Одна игральная карта """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank+self.suit
        return rep

class Unprintable_Card(Card):
    """ Карты которые нельзя показывать """
    def __str__(self):
        """ нельзя выводить на печать """
        return "<нельзя напечатать>"


# j = Unprintable_Card(rank="A", suit="h")
# print (j)

class Positioable_Card(Card):
    """ карта, которую можно положить лицом или рубашкой вверх """
    def __init__(self, rank, suit, face_up=True):
        super(Positioable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positioable_Card, self).__str__()
        else:
            rep = "XX"
        return rep


    def flip(self):
        self.is_face_up = not self.is_face_up

#main code

card1 = Card("A", "c")
card2 = Unprintable_Card ("A", "d")
card3 = Positioable_Card ("A", "h")

print("выведем экземпляр класса Card")
print(card1)

print("выведем экземпляр класса  Unprintable_Card")
print(card2)

print("выводим экземпляр Positioable_Card")
print(card3)

card3.flip()

print("выводим экземпляр Positioable_Card еще раз после переворота карт")
print(card3)
