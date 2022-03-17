from card_pac import deck as _deck

deck = _deck.Deck(True)
deck_list = deck.get_deck_list()

for i in deck_list :
    print(f'Card: {i.get_type()}')

print(f'from the top! We have a... {deck.top().get_type()}!')

for i in range(2) :
    top_card = deck.pull()
    print(f'next we draw... {top_card.get_type()}!')

for i in deck.get_played_cards() :
    print(f'an F for all the cards we lost along the way... {i.get_type()}')