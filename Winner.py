class Winner(object):



    def Get_Winner(self):

        players_score = []

        hands = self.players_hand_plus_river(self.hands,self.cards_on_table)

        for player_hand in range(len(hands)):

            strip_sort = self.strip_sort(hands[player_hand])

            if self.Royal_Flush(strip_sort)[0]:
                players_score.append(self.Royal_Flush(strip_sort))

            elif self.Straight_Flush(strip_sort)[0]:
                players_score.append(self.Straight_Flush(strip_sort))

            elif self.Four(strip_sort)[0]:
                players_score.append(self.Four(strip_sort))

            elif self.Full_House(strip_sort)[0]:
                players_score.append(self.Full_House(strip_sort))

            elif self.Flush(strip_sort)[0]:
                players_score.append(self.Flush(strip_sort))

            elif self.Straight(strip_sort)[0]:
                players_score.append(self.Straight(strip_sort))

            elif self.Three(strip_sort)[0]:
                players_score.append(self.Three(strip_sort))

            elif self.Two_Pairs(strip_sort)[0]:
                players_score.append(self.Two_Pairs(strip_sort))

            elif self.Pair(strip_sort)[0]:
                players_score.append(self.Pair(strip_sort))

            elif self.High_Card(strip_sort)[0]:
                players_score.append(self.High_Card(strip_sort))

            players_score[player_hand].append(player_hand)


        place_winner=[0]
        temp=-1
        for i in range(len(players_score)):
            if temp<players_score[i][1]:
                temp=players_score[i][1]
                place_winner=[i]
            elif temp==players_score[i][1]:
                if players_score[i][2]==players_score[place_winner[0]][2]:
                    place_winner.append(i)
                elif players_score[i][2]>players_score[place_winner[0]][2]:
                    temp=players_score[i][1]
                    place_winner=[i]
        for i in range(len(place_winner)):
            self.winners.append(players_score[place_winner[i]])

    #- margin players and table cards - #
    #players_hand = [['10C', '5D'], ['13C', '4S'], ['9H', '2C'], ['11C', '9S'], ['11H', '4C']]
    #river =  ['12D', '14C', '10S', '3D', '2d']
    # return example:  [['10C', '5D', '12D', '14C', '10S', '3D', '2d'], ['13C', '4S', '12D', '14C', '10S', '3D', '2d'], ['9H', '2C', '12D', '14C', '10S', '3D', '2d'], ['11C', '9S', '12D', '14C', '10S', '3D', '2d'], ['11H', '4C', '12D', '14C', '10S', '3D', '2d']]
    def players_hand_plus_river(self,players_hand,river):
        for i in range(len(players_hand)):
            for j in range(len(river)):
                players_hand[i].append(river[j])

        return players_hand


    # - seperate int and chars and arrenge min to max by numbers in arrey - #
    # player_hand = ['10C', '5D', '12D', '14C', '10S', '3D', '2d']
    # - return exmaple: strip_sort :  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def strip_sort(self,player_hand):
        strip_hand=[]
        for i in range(len(player_hand)):
            if len(player_hand[i]) == 2:
                strip_hand.append([int(player_hand[i][0]),player_hand[i][1]])
            elif len(player_hand[i]) == 3:
                strip_hand.append([int(player_hand[i][0]+player_hand[i][1]),player_hand[i][2]])

        strip_sort=[]
        for i in range(len(strip_hand)):
            min = strip_hand[0][0]
            place = 0
            for j in range(len(strip_hand)):
                if min > strip_hand[j][0]:
                    min = strip_hand[j][0]
                    place = j

            strip_sort.append(strip_hand[place])
            del strip_hand[place]

        return strip_sort



    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Royal_Flush(self,strip_sort):
        hand = []

        strip_sort=strip_sort[::]



        #strip_sort = [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']],[[4, 'C'], [3, 'C'], [10, 'D'], [11, 'D'], [12, 'D'], [13, 'D'], [14, 'D']]

        # print("symbole=",strip_sort[2][1],"value=",strip_sort[2][0] )
        symbole=strip_sort[2][1]

        if strip_sort[2][0]==10:
            if strip_sort[3][0]==11 and strip_sort[3][1]==symbole:
                if strip_sort[4][0]==12 and strip_sort[4][1]==symbole:
                    if strip_sort[5][0]==13 and strip_sort[5][1]==symbole:
                        if strip_sort[6][0]==14 and strip_sort[6][1]==symbole:
                                for i in range(5):
                                    hand.append([strip_sort[2+i][0],strip_sort[2+i][1]])
                                return [True,9,None,"Royal Flush",hand]



        return [False]





    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Straight_Flush(self,strip_sort):
        hand=[]
        sum=0
        a=strip_sort.copy()
        strip_sort = a
        for i in range(len(strip_sort)):
            if strip_sort[i][0]==14:

                strip_sort.insert(0,[1,strip_sort[i][1]])


        symbole_num=[[],[],[],[]]
        for i in range(len(strip_sort)):
            if strip_sort[i][1]=="D":
                symbole_num[0].append(strip_sort[i])
            if strip_sort[i][1]=="S":
                symbole_num[1].append(strip_sort[i])
            if strip_sort[i][1]=="H":
                symbole_num[2].append(strip_sort[i])
            if strip_sort[i][1]=="C":
                symbole_num[3].append(strip_sort[i])



        for i in range(len(symbole_num)):
            if len(symbole_num[i])==5:
                hand.append([symbole_num[i],"?"])
                for t in range(5):
                    sum=sum+symbole_num[i][t][0]
                for j in range(len(symbole_num[i])-1):

                    if symbole_num[i][j][0]== symbole_num[i][j+1][0]-1:
                        if j==3:
                            return [True,8,sum,"Straight Flush",hand]
                    else: break

        return [False]

    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Four(self,strip_sort):
        strip_sort=strip_sort[::]


        arrey = []
        for i in range(len(strip_sort)):
            arrey.append(strip_sort[i][0])



        for i in range(len(arrey)):
            if arrey.count(arrey[i]) == 4:
                four=arrey[i]
                for j in range(4):
                    arrey.remove(four)
                sum=(four*4)+max(arrey)
                return[True,7,sum,"Four"]
                break

        return [False]


    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Full_House(self,strip_sort):

        arrey = []
        strip_sort=strip_sort[::]
        hand=[]
        for i in range(len(strip_sort)):
            arrey.append(strip_sort[i][0])
        for t in range(len(arrey)):
            if arrey.count(arrey[t]) == 3:
                full_house=arrey[t]
                hand.append([arrey[t],"?"])
                hand.append([arrey[t],"?"])
                hand.append([arrey[t],"?"])
                
                arrey[i] = -1
                for j in range(len(arrey)):
                    if arrey[j] == full_house:
                        arrey[j] = -2
                        break
                for j in range(len(arrey)):
                    if arrey[j] == full_house:
                        arrey[j] = -3
                        break
                for b in range(len(arrey)):
                    if arrey.count(arrey[b]) == 2:

                        hand.append([arrey[b],"?"])
                        hand.append([arrey[b],"?"])
                        full_house=(full_house*3) + (arrey[b]*2)
                        return[True,6,full_house,"Full House",hand]


        return [False]


    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Flush(self,strip_sort):
        strip_sort=strip_sort[::]
        hand = []
        symbole_num=[[],[],[],[]]
        for i in range(len(strip_sort)):
            if strip_sort[i][1]=="D":
                symbole_num[0].append(strip_sort[i])
            if strip_sort[i][1]=="S":
                symbole_num[1].append(strip_sort[i])
            if strip_sort[i][1]=="H":
                symbole_num[2].append(strip_sort[i])
            if strip_sort[i][1]=="C":
                symbole_num[3].append(strip_sort[i])

        flush=0

        for i in range(len(symbole_num)):
            if len(symbole_num[i]) == 5 or len(symbole_num[i]) == 6 or len(symbole_num[i]) == 7:
                for j in range(1,6,1):
                    flush = flush + symbole_num[i][-j][0]
                    hand.append([symbole_num[i][-j][0],symbole_num[i][-j][1]])


                return[True,5,flush,"Flush",hand]

        return[False]


    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Straight(self,strip_sort):

        cards_arrey = []
        strip_sort=strip_sort[::]
        for i in range(len(strip_sort)):
            if strip_sort[i][0]==14:
                strip_sort.insert(0,[1,strip_sort[i][1]])
                break

        for i in range(len(strip_sort)):
            cards_arrey.append(strip_sort[i][0])

        cards_arrey = list(dict.fromkeys(cards_arrey))
        cards_arrey = cards_arrey[::-1]

        count=1
        straight=0
        hand = []

        for i in range(len(cards_arrey)-1):
            if cards_arrey[i] == cards_arrey[i+1]+1:
                count = count + 1
                straight = straight + cards_arrey[i]
                hand.append([cards_arrey[i],"?"])

                if count == 5:
                    straight = straight + cards_arrey[i+1]
                    hand.append([cards_arrey[i+1],"?"])

                    return [True,4,straight,"Straight",hand]
            else:
                count = 1
                straight = 0
                hand = []

        return [False]

    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Three(self,strip_sort):



        cards_arrey = []
        hand = []
        three_sum = 0
        three = None
        for i in range(len(strip_sort)):
            cards_arrey.append(strip_sort[i][0])

        cards_arrey = cards_arrey[::-1]


        for i in range(len(cards_arrey)):

            if cards_arrey.count(cards_arrey[i]) == 3:
                three = cards_arrey[i]
                three_sum = cards_arrey[i] * 3
                for j in range(3):
                    hand.append([cards_arrey[i],"?"])
                    cards_arrey.remove(cards_arrey[i])

                for j in range(2):
                    max_card = max(cards_arrey)

                    three_sum = three_sum + max_card
                    hand.append([max_card,"?"])
                    cards_arrey.remove(max_card)

                return  [True,3,three_sum,"Three",hand]

        return [False]

    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Two_Pairs(self,strip_sort):
        cards_arrey = []
        hand = []
        two_pairs_sum = 0
        two_pairs=None
        for i in range(len(strip_sort)):
            cards_arrey.append(strip_sort[i][0])

        cards_arrey = cards_arrey[::-1]


        for i in range(len(cards_arrey)):

            if cards_arrey.count(cards_arrey[i]) == 2:
                    two_pairs = cards_arrey[i]
                    two_pairs_sum = two_pairs * 2

                    for j in range(2):
                        hand.append([two_pairs,"?"])
                    delete = cards_arrey[i]
                    cards_arrey[i] = -1

                    for bb in range(len(cards_arrey)):
                        if cards_arrey[bb] == delete:
                            cards_arrey[bb] = -2
                            break


                    for g in range(len(cards_arrey)):

                        if cards_arrey.count(cards_arrey[g]) == 2:
                            two_pairs = cards_arrey[g]
                            two_pairs_sum = two_pairs_sum + two_pairs * 2

                            for j in range(2):
                                hand.append([two_pairs,"?"])
                                cards_arrey.remove(two_pairs)


                            max_card = max(cards_arrey)

                            two_pairs_sum = two_pairs_sum + max_card
                            hand.append([max_card,"?"])


                            return [True,2,two_pairs_sum,"Two_Pairs",hand]

        return [False]

    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def Pair(self,strip_sort):

        cards_arrey = []
        hand = []
        pair_sum = 0
        pair=None
        for i in range(len(strip_sort)):
            cards_arrey.append(strip_sort[i][0])

        cards_arrey = cards_arrey[::-1]


        for i in range(len(cards_arrey)):
                if cards_arrey.count(cards_arrey[i]) == 2:
                    pair = cards_arrey[i]
                    pair_sum = cards_arrey[i] * 2
                    for j in range(2):
                        hand.append([cards_arrey[i],"?"])
                    temp=cards_arrey[i]
                    cards_arrey[i]=-1
                    for j in range(len(cards_arrey)):
                        if cards_arrey[j]==temp:
                            cards_arrey[j]=-2
                            break
                    for j in range(3):
                        max_card = max(cards_arrey)

                        pair_sum = pair_sum + max_card
                        hand.append([max_card,"?"])
                        cards_arrey.remove(max_card)

                    return  [True,1,pair_sum,"Pair",hand]

        return [False]





    # strip_sort =  [[10, 'C'], [11, 'C'], [12, 'D'], [13, 'C'], [13, 'S'], [14, 'D'], [14, 'C']]
    def High_Card(self,strip_sort):

        cards_arrey = []
        hand = []
        high_sum = 0
        high=None
        for i in range(len(strip_sort)):
            cards_arrey.append(strip_sort[i][0])

        cards_arrey = cards_arrey[::-1]


        for i in range(5):
            max_card = max(cards_arrey)

            high_sum =high_sum + max_card
            hand.append([max_card,"?"])
            cards_arrey.remove(max_card)

        return [True,0,high_sum,"High Card",hand]
