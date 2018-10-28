import  collections
from random import choice

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamods clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __getitem__(self, item):
        return self._cards[item]


    def __len__(self):
        return len(self._cards);

suit_values = dict(spades=3, diamods=2, clubs=1, hearts=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value *len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    beer_card = Card('7','diamods')
    print(beer_card)

    print("#################################################")

    deck = FrenchDeck()
    print(deck.ranks)
    print(deck.suits)

    print("#################################################")

    print("deck len:",len(deck))

    print("#################################################")

    print("deck first:", deck[0])
    print("deck last:", deck[-1])

    print("#################################################")

    print("random choice 1:",choice(deck))
    print("random choice 2:", choice(deck))
    print("random choice 3:", choice(deck))

    print("#################################################")

    print("deck 0~2:", deck[:3])
    print("deck A:", deck[12::13])

    print("#################################################")

    for card in deck:
        print("card :",card)

    print("#################################################")

    for card in reversed(deck):
        print("card :", card)

    print("#################################################")

    print(Card('Q',"hearts") in deck)
    print(Card('Q', "beasts") in deck)

    print("#################################################")

    for card in sorted(deck,key=spades_high):
        print(card)