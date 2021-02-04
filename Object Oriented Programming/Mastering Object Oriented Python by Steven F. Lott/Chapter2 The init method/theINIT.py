# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:48:50 2020

@author: MRUTYUNJAY BISWAL
"""

"""
__init__() works as a constructor in Python.

When an object is created, Python first creates an empty object and 
then calls the __init__() method to set the state of the new object
This method generally creates the object's instance variables and 
performs any other one-time processing.
"""
# let's play around the concept
from typing import Tuple


class Card:
    """
    There are 2 instance variables taken inside the class, those are
    suit and rank. And the other two variables are calculated using an method.
    """

    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = self.rank
        self.hard, self.soft = self._points()

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)


# let's inherit Ace card from our Card class
class AceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 1, 11


class FaceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 10, 10

# next start from page 68.
