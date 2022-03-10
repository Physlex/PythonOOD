"""
# Eventual abstract base used for inheritance hierarchy of cards
# TODO: Finish design of Card inheritance tree
"""
class Card() :
    """
    # Card Base Class Constructor
    # TODO: Replace with an inheritance hierarchy
    """
    def __init__(self, rank:str, suit:str)->None :
        self._rank = rank
        self._suit = suit

    """
    # Inheritable Display Function
    # @details, Formats and displays card details
    #           Formated like: 'x of y'
    """
    def display_card(self)->str :
        return str(f'{self._rank} of {self._suit}s')
    
    """
    # Inheritable, abstract, type declaration
    # @details, used in testing, not meant to be used publicly
    """
    def display_card_type(self)->str :
        return str(type(self))

    """
    # Protected Members
    """
    _rank:str
    _suit:str

"""
# Kind of a mess, but not finished anyway
"""
