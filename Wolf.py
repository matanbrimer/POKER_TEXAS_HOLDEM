import Get_Deck
import Card_Distribution
from Game import Game
from Winner import Winner
import sys
class Table(Game,Winner):

    def __init__ (self,players):
        self.deck=None
        self.players=players
        #self.players=[]
        self.hands=None
        self.cash=[]
        self.cards_on_table=None
        self.winners=[]
        self.small = None
        self.big = None

    def Shuffle_Deck(self):

        self.deck = Get_Deck.Func()

    def Card_Distribution(self):

        cards = Card_Distribution.Func(len(self.players),self.deck)

        self.hands = cards[0]
        self.deck = cards[1]



sys.stdout.flush()

if __name__ == "__main__":

    players = ["rom","don"]
    cash = ["100","50"]

    t1 = Table(players)

    t1.Shuffle_Deck()
    print("deck=",t1.deck)
    t1.Card_Distribution()
    print("hands=",t1.hands)

    t1.flop()
    t1.turn()
    t1.river()
    print("Cards on table : ",t1.cards_on_table)

    #t1.hands = [['3H', '3D'], ['11D', '2S']]
    #t1.cards_on_table = ['13C', '7D', '13H', '10H', '8H']

    t1.Get_Winner()
    print("winners=",t1.winners)
