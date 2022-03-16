import card_factory
import cards
"""
# @class Deck, "Deck", 'Deck'
# @details, Creates a deck upon request 
#           and returns it as a stack ADT
"""
class Deck() :
    """
    # Creates a generic deck type from list
    # @param list_to_convert, a list of Cards (Base). Must only hold Card type
    #                         and it's variants 
    """
    def __init__(self, list_to_convert:list) -> None:
        #Clears the list of non-Card types
        for i in list_to_convert :
            if (not issubclass(i, cards.Card)) :
                list_to_convert.remove(i)
        self.__deck = list_to_convert
        pass 
    
    """
    # Creates a default deck of cards
    """
    def __init__(self) -> None:
        self.__deck = self.__create_deck()
        pass

    """
    # Public Methods
    """

    """
    # Returns the 'Top' card in the deck
    # @details the top card in the deck follows the stack rules,
    #          meaning that the top card is the last added.
    # @throw_exception 'accessing null element' when len(deck) < 1        
    """
    def top(cls) :
        if (len(cls.__deck) < 1) : print('accessing null element')
        return cls.__deck[len(cls.__deck) - 1]

    """
    # Returns the 'Top' card in deck, then removes from deck
    # @details all lost cards are appended to lost_cards list
    #          on reshuffle, all lost_cards are joined to __deck again
    # @returns card, the top element of the deck
    """
    def pull(cls) :
        card = cls.top()
        cls.__deck.remove(card)
        cls.__lost_cards.append(card)
        return card

    """
    # Mutators/Extractors
    """

    """
    # Used for debugging purposes
    # @details returns the deck list, ONLY FOR TESTING
    """
    def get_deck(cls)->list :
        return cls.__deck

    """
    # Private Methods
    """

    """
    # Generates cards to put into a deck via a list
    # @param list_of_cards, the list that will hold all the cards
    # @return list_of_cards, returns list filled with cards
    """
    def __create_deck(self, list_of_cards:list)->list :
        self.__cf = card_factory.CardFactory()
        valid_suits = self.__cf.get_valid_suits()
        #Generates 4 x 13 cards
        for i in range(1, 14) :
            for j in range(1, 5) :
                list_of_cards.append(self.__cf.create_card(i, valid_suits[j]))
        return list_of_cards

    """
    # Private members
    """
    __deck:list
    __lost_cards:list
    __cf:card_factory