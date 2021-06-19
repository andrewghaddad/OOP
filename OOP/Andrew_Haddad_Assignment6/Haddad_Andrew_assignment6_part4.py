
cards=['10 of Hearts','9 of Hearts','8 of Hearts','7 of Hearts',
        '6 of Hearts','5 of Hearts','4 of Hearts',
        '3 of Hearts','2 of Hearts','Ace of Hearts','King of Hearts',
        'Queen of Hearts','Jack of Hearts',
        '10 of Diamonds','9 of Diamonds','8 of Diamonds','7 of Diamonds',
        '6 of Diamonds','5 of Diamonds',
        '4 of Diamonds','3 of Diamonds','2 of Diamonds','Ace of Diamonds','King of Diamonds',
        'Queen of Diamonds','Jack of Diamonds','10 of Clubs','9 of Clubs','8 of Clubs',
        '7 of Clubs','6 of Clubs','5 of Clubs','4 of Clubs',
        '3 of Clubs','2 of Clubs','Ace of Clubs','King of Clubs',
        'Queen of Clubs','Jack of Clubs','10 of Spades','9 of Spades','8 of Spades','7 of Spades',
        '6 of Spades','5 of Spades','4 of Spades',
        '3 of Spades','2 of Spades','Ace of Spades','King of Spades',
        'Queen of Spades','Jack of Spades']

values=[10,9,8,7,6,5,4,3,2,1,10,10,10,10,9,8,7,6,5,4,3,2,1,10,10,10,10,9,8,7,6,5,4,3,2,1,10,10,10,
        10,9,8,7,6,5,4,3,2,1,10,10,10]

player_cards=[]
player_score=0
n=random.randint(0,52)
player_cards.append(cards[n])
player_score+=values[n]
n=random.randint(0,52)
player_cards.append(cards[n])
player_score+=values[n]
computer_cards= []
c_score= 0
ch="h"

print(player_cards,"is worth ",player_score)

while(ch=='h'):
    player_score=player(cards,values,player_cards,player_score)
    if(player_score>21):
        print('computer wins!')
        sys.exit()
    elif(player_score==21):
        print("Player wins!!!")
        sys.exit()
    else:
        ch=input("(h)it or (s)tand? ")

n=random.randint(0,52)
computer_cards.append(cards[n])
c_score+=values[n]
n=random.randint(0,52)
computer_cards.append(cards[n])
c_score+=values[n]
print(computer_cards,"is worth ",c_score)

while(c_score<player_score and c_score<21):
    c_score+=computer(cards,values,player_cards,player_score)
    if(c_score>21 ):
        print("Player wins!!!")
        sys.exit()
    elif(c_score==21 or c_score>player_score):
        print("Computer Wins!!")
        sys.exit()


def player(cards,values,player_cards,player_score):
    n=random.randint(0,52)
    print('You drew a card of ',cards[n])
    player_cards.append(cards[n])
    player_score+=values[n]
    print(player_cards,"is worth ",player_score)
return player_score

def computer(cards,values,computer_cards,c_score):
    n=random.randint(0,52)
    print('Computer drew a card of ',cards[n])
    computer_cards.append(cards[n])
    c_score+=values[n]
    print(computer_cards,"is worth ",c_score)
return c_score
