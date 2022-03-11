from abc import ABC, abstractmethod

"""
# @Class Card, "Card", 'Card'
# @details Abstract base used for inheritance hierarchy of card types
#          slightly arbitrary, but good for learning how to develop w/ python
#          polymorphism
"""
class Card(ABC) :
    """
    # Card Base Class Constructor
    # @param rank, a string representing the value [1, 13]
    # @param suit, a string representing the class of card [spade, heart, diamond, club]
    """
    def __init__(self, rank:str, suit:str)->None :
        self._rank = rank
        self._suit = suit

    """
    # Defines the name of the current class
    # @details internally declares card type for external use.
    """
    @abstractmethod
    def get_name(self) :
        pass

    """
    # Defines the full definition of the current card
    # @details returns the name, colour, rank and suit
    """
    @abstractmethod
    def get_type(self) :
        pass

    """
    # Returns the cards rank
    # @return self._rank
    """
    def get_rank(self)->str :
        return self._rank
    
    """
    # Returns the cards suit
    # @return self._suit
    """
    def get_suit(self)->str :
        return self._suit

    """
    # Inheritable Display Function for simpler cards
    # @details, Formats and displays card details
    #           Formated like: 'x of y'
    """
    def display_card(self)->str :
        return str(f'{self._rank} of {self._suit}s')
    
    """
    # gets the suit of the card based on the class
    """
    def display_card_suit(self)->str :
        return str(type(self))

    """
    # Protected Members
    """
    _rank:str
    _suit:str
    _name:str
    _colour:str
    _type:str

"""
# This next set of classes is mainly a contrived reason to use inheritance
# for learning how python does it, rather than a relevant reason.
# 
# Technically, I could use a hashmap to cross define subtypes in cardfactory class
"""

"""
# Spade defn of a card
"""
class Spade(Card) :
    """
    # Inherited constructor
    # @details the card is defined in the same way as a generic card.
    # It is black when a spade.
    """
    def __init__(self, rank: str, suit: str) -> None:
        super().__init__(rank, suit)
        self._colour = 'black'
        self._type = (f'a {self._colour} {self.get_name()}')

    """
    # Arbitrary name defn for sake of learning
    """
    def get_name(self) :
        self._name = super().display_card()
        return self._name

    """
    # Arbitraty type defn for sake of learning
    """
    def get_type(self):
        return self._type

"""
# Club defn of a card
"""
class Club(Card) :
    """
    # Inherited constructor
    # @details the card is defined in the same way as a generic card.
    # It is black when a club.
    """
    def __init__(self, rank: str, suit: str) -> None:
        super().__init__(rank, suit)
        self._colour = 'black'
        self._type = (f'a {self._colour} {self.get_name()}')

    """
    # Arbitrary name defn for sake of learning
    """
    def get_name(self):
        self._name = super().display_card()
        return self._name

    """
    # Arbitraty type defn for sake of learning
    """
    def get_type(self):
        return self._type

"""
# Heart defn of a card
"""
class Heart(Card) :
    """
    # Inherited constructor
    # @details the card is defined in the same way as a generic card.
    # It is red when a heart.
    """
    def __init__(self, rank: str, suit: str) -> None:
        super().__init__(rank, suit)
        self._colour = 'red'
        self._type = (f'a {self._colour} {self.get_name()}')

    """
    # Arbitrary name defn for sake of learning
    """
    def get_name(self):
        self._name = super().display_card()
        return self._name
    
    """
    # Arbitraty type defn for sake of learning
    """
    def get_type(self):
        return self._type

"""
# Diamond defn of a card
"""
class Diamond(Card) :
    """
    # Inherited constructor
    # @details the card is defined in the same way as a generic card.
    # It is red when a diamond.
    """
    def __init__(self, rank: str, suit: str) -> None:
        super().__init__(rank, suit)
        self._colour = 'red'
        self._type = (f'a {self._colour} {self.get_name()}')

    """
    # Arbitrary name defn for sake of learning
    """
    def get_name(self):
        self._name = super().display_card()
        return self._name

    """
    # Arbitraty type defn for sake of learning
    """
    def get_type(self):
        return self._type

