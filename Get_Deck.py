import random
import sys




def Func():

    deck=["2D","3D","4D","5D","6D","7D","8D","9D","10D","11D","12D","13D","14D","2H","3H","4H","5H","6H",
            "7H","8H","9H","10H","11H","12H","13H","14H","2S","3S","4S","5S","6S","7S","8S","9S","10S","11S",
            "12S","13S","14S","2C","3C","4C","5C","6C","7C","8C","9C","10C","11C","12C","13C","14C"]

    # - shuffle cards deck - #
    for i in range(random.randint(1,9)):
        random.shuffle(deck)

    # - cut the cards - #
    num_cut = random.randint(10,40)
    for i in range(num_cut):
        deck.append(deck[0])
        del deck[0]

    return deck



if __name__ == "__main__":
    sys.stdout.flush()
    print(Func())























