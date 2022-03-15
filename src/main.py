import random
from card_pac import card_factory

def print_cards(suit_cards:list)->None :
    for iVal in suit_cards :
        print(f'Card:', iVal.get_type())
        print(f'Card Suit:', iVal.display_card_suit(), end = "\n\n")

cf = card_factory.CardFactory()

deck = [] 
for i in range(13) :
    rank = i + 1
    deck.append(cf.create_card(rank, 'spade'))
    deck.append(cf.create_card(rank, 'diamond'))
    deck.append(cf.create_card(rank, 'club'))
    deck.append(cf.create_card(rank, 'heart'))

print_cards(deck)
print("Shuffling cards...")
random.shuffle(deck)
print(f'Top card is a {deck[len(deck) - 1].get_type()}!')