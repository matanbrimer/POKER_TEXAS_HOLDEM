def Func(players_num,deck):
    players_hand=[]

    for i in range(players_num):
        players_hand.append([])
        for j in range(2):
            players_hand[i].append(deck[0])
            del deck[0]



    return [players_hand,deck]
