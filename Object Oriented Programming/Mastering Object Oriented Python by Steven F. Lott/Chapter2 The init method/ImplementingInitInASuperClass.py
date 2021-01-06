# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:46:06 2020

@author: MRUTYUNJAY BISWAL
"""

from typing import Tuple
from enum import Enum


class Card:

    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)
        pass

    pass


class AceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 1, 11

    pass


class FaceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 10, 10

    pass


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"

    pass
