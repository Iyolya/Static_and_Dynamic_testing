import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 4)
        self.card2 = Card("Clubs", 8)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame()
       

    def test_check_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card1))


    def test_highest_card(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    
    def test_cards_total(self):
        self.assertEqual("You have a total of 12", self.card_game.cards_total(self.cards))