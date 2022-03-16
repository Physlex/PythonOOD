import card_pac.card_factory as card_factory
import card_pac.cards as cards
import random

"""
# @class Deck, "Deck", 'Deck'
# @details, Creates a deck upon request 
#           and returns it as a stack ADT
"""
class Deck() :
    """
    # Constructors
    """    
    
    """
    # Creates a generic deck type from list
    # @param list_to_convert, a list of Cards (Base). Must only hold Card type
    #                         and it's variants 
    """
    def __init__(self, list_to_convert:list, shuffle = True) -> None:
        #Clears the list of non-Card types
        for i in list_to_convert :
            if (not issubclass(i, cards.Card)) :
                list_to_convert.remove(i)

        #Define attributes
        self.__deck = list_to_convert
        self.__lost_cards = []
        self.__cf = card_factory.CardFactory()

        #Shuffles deck (optionally)
        if shuffle == True :
            random.shuffle(self.__deck)
        pass 
    
    """
    # Creates a default deck of cards
    """
    def __init__(self, shuffle = True) -> None:
        #Define attributes
        self.__deck = []
        self.__lost_cards = []
        self.__cf = card_factory.CardFactory()
        self.__create_deck(self.__deck)

        #Shuffles deck (optionally)
        if shuffle == True :
            random.shuffle(self.__deck)
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
    # Shuffles the deck and puts all lost cards back into the deck
    # @details shuffles lost cards into the deck, randomizes the deck
    """
    def shuffle(cls)->None :
        #reimplement lost->deck
        for i in cls.__lost_cards :
            cls.__deck.append(i)
        
        #reshuffle deck
        random.shuffle(cls.__deck)
        pass

    """
    # Extractors
    """
    #Returns deck list
    def get_deck_list(cls)->list :
        return cls.__deck

    #Returns lost cards
    def get_played_cards(cls)->list :
        return cls.__lost_cards


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
        
        for i in range(1, 14) :
            for j in range(4) :
                list_of_cards.append(self.__cf.create_card(i, valid_suits[j]))
        return list_of_cards


    """
    # Private members
    """
    __deck:list
    __lost_cards:list
    __cf:card_factory