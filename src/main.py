from CardFactory import CardFactory

cf = CardFactory()

spade_cards:list = []
for i in range(13) :
    spade_cards.append(cf.create_card(i + 1, 'spade'))

for i, iVal in enumerate(spade_cards) :
    print(f'Card: ', iVal.display_card())
    print(f'Card Type: ', iVal.display_card_type(), end='\n\n')