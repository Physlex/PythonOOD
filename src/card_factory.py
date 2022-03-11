import cards

"""
# @class CardFactory, "CardFactory", 'CardFactory'
# @details, Creates a card on demand and returns the created card
#           The card creation process is based on a ruleset defined
#           above create_card
"""
class CardFactory() :
    """
    # CardFactory constructor
    # @details creates a card factory for use to create cards
    """
    def __init__(self)-> None: 
        pass

    """
    # Creates a card based on the rank and suit requested
    # @param rank, the rank of the card. Must be a number between [1, 13] or an 
    #  alpha representation of the numerical represesentation.
    #  For example: rank = 1, then rank = 'ace'
    #               rank = '2', then rank = '2'
    #               rank = 12, then rank = 'Queen'
    #
    # @param suit, the suit of the card. Must be one of:
    #   - club, diamond, heart, or spade 
    #
    # @throw_exception_wrong_rank if rank is N/A to function preconditions
    #
    # @return None, if suit and rank do not match an appropriate card
    #   Else, the appropriate card is returned
    """
    def create_card(self, rank, suit:str) :
        if (type(rank) == type(1)) :
            if (rank < 1 or rank > 13) :
                print(f'\'{rank}\' is not a valid card rank')
                return None
            else :
                rank = self.__rankint_to_rankstr[rank]

        if (suit not in self.__suit_to_valid) :
            print(f'\'{suit}\' is not a valid card suit')
            return None
    
        self.__created_card = self.__suit_to_card[suit](rank, suit)
        return self.__created_card

    """
    # Private Members
    """
    __created_card:cards.Card    
    __rankint_to_rankstr = {
        1: 'ace', 2: '2', 3: '3', 4: '4', 5: '5', 
        6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
        11: 'jack', 12: 'queen', 13: 'king'
    }
    __suit_to_valid = {
        'club': True,
        'diamond': True,
        'heart': True,
        'spade': True,
    }
    __suit_to_card = {
        'club': cards.Club,
        'diamond': cards.Diamond,
        'heart': cards.Heart,
        'spade': cards.Spade,
    }