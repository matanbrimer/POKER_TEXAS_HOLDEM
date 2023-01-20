class Game(object):


    def flop(self):
        flop=[]

        del self.deck[0]

        for i in range(3):
            flop.append(self.deck[0])
            del self.deck[0]

        self.cards_on_table = flop

    def turn(self):

        del self.deck[0]
        self.cards_on_table.append(self.deck[0])
        del self.deck[0]

    def river(self):

        del self.deck[0]
        self.cards_on_table.append(self.deck[0])
        del self.deck[0]
      
