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
        
class Hand(object):
    """ рука. набор игральных карт у игрока """
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)+" "
        else:
            rep = "<пусто>"
        return rep
        
    def cleaner(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
#main 

card1 = Card(rank="A", suit="c")
print("вывожу на экран обьект карту: ")
print(card1)
card2 = Card(rank="2", suit="c")
card3 = Card(rank="3", suit="c")
card4 = Card(rank="4", suit="c")
card5 = Card(rank="5", suit="c")
print("\nвывожу еще 4 карты:")
print(card2)
print(card3)
print(card4)
print(card5)


my_hand = Hand()
print("Печатаю карты, которые у меня на руках до раздачи:")
print(my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nПечатаю пять карт, которые у меня на руках:")
print(my_hand)

you_hand = Hand()
my_hand.give(card1, you_hand)
my_hand.give(card2, you_hand)
print("я передал две карты от себя к вам")
print("теперь у вас на руках")
print(you_hand)
print("и у меня")
print(my_hand)

my_hand.cleaner()
print("Я сбросил карты и теперь у меня на руках", my_hand)
