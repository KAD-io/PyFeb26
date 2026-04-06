"""hm13_job1"""


from random import shuffle


class Card:
    number_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    mast_list = ['♠️', '❤️', '♦️', '♣️']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f"{self.mast} {self.number}"


class CardsDeck:
    def __init__(self):
        self.card_list = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.card_list.append(Card(number, mast))
        self.card_list.append(Card("Joker", "Red"))
        self.card_list.append(Card("Joker", "Black and white"))

    def shuffle(self):
        shuffle(self.card_list)

    def get(self, card_number):
        if not 1 <= card_number <= 54:
            return "Error"
        return self.card_list[card_number - 1]


deck = CardsDeck()
deck.shuffle()


while True:
    print('Enter "55" or more to shuffle the deck or "0" to exit')
    choose = int(input('Choose a card from a deck of 54 cards: '))
    if choose == 0:
        print("exit")
        break
    if choose > 54:
        deck.shuffle()
        print("shuffle the deck")
    else:
        card = deck.get(choose)
        print(f'You card is: {card}')
