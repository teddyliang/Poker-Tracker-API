from __future__ import annotations

from abc import ABC, abstractclassmethod
from typing import List
from enum import Enum


class Card():
    '''
    This class represents the value of a card (rank and suit)
    '''

    '''
    Type representing the ranks of cards
    '''
    class Rank(Enum):
        ACE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13

    '''
    Type representing the suits of cards
    '''
    class Suit(Enum):
        SPADE = 1
        CLUB = 2
        DIAMOND = 3
        HEART = 4
    
    def __init__(self, rank: Rank, suit: Suit):
        pass

    
class HoleCards():
    '''
    This class is defined as the two cards a player is holding for a poker hand.
    '''
    def __init__(self, card1: Card, card2: Card):
        pass

class Action():
    '''
    This class represents the different actions that can occur in a hand. Player actions include betting, checking, calling, and folding. Non player actions include seeing the flop, turn, and river. 
    '''
    pass

class Parser(ABC):
    '''
    This is an abstract class for parsers that parse logs of poker hands. The client can define their own parser.
    '''
    @abstractclassmethod
    def parse(cls, log_text: str) -> List[List[Action]]:
        pass

class PokerNowParser(Parser):
    '''
    This class represents a parser for logs from PokerNow. This is the default parser. It must be used with PokerNow logs.
    '''
    def parse(cls):
        pass

class Player:
    '''
    This class keeps track of a player's winnings and hand history
    '''
    pass

class Tracker:
    def __init__(self):
        pass
    
    def parse(self, parser: Parser = PokerNowParser):
        '''
        Based on the parser provided with the default as our PokerNowParser
        '''
        pass

    def calculate_equity(self, hand_list: List[HoleCards], hand : HoleCards, board: List[Card]) -> float:
        '''
        Calculates a hand's equity against the list of the hands of everyone at the table and the board state.
        Args:
            hand_list: the list of all opponent hands
            hand: the hand to calculate the equity of
            board: the community cards, if they exist 
        Returns:
            the equity of 'hand' versus all other hands
        Throws:
            ValueError if 'board' does not contain either 0, 3, 4, or 5 cards or if duplicate cards exist between all hands and the board
        '''
        pass
        
    def get_hand_history(self, hand_id: int) -> List[Action]:
        '''
        Gets all the actions that happened during a hand in the order that they happened
        Args:
            hand_id: unique hand id
        Returns:
            all the actions that happened within a single hand
        Throws:
            ValueError if hand_id is negative or does not match any hand_id currently stored
        '''
        pass

    def get_player_history(self, user: Player) -> List[(int, List[Action])]:
        '''
        Returns every hand and the action for every hand that 'user' was involved in
        Args: 
            user: the player to get the entire history of
        Returns:
            a list of hand ids and the corresponding hand histories for the player, returns empty list if the player was not found      
        '''
        pass

    def get_player(self, username: str) -> Player:
        '''
        Gets a player based on a username
        Args:
            username of the player to get
        Returns:
            a player object with the specified username
        Throws:
            ValueError is username provided does not match any that is currently stored
        '''
        pass
         
    
