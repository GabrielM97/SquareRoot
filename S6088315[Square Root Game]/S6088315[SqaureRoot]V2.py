
#Square Root board game
#Gabriel Menezes 16/01/2017
                                                                                                                         #
#Rules:                                                                                                                  #
    #2 player                                                                                                            #
    #2 markers per player                                                                                                #
    #turns rolling dice                                                                                                  #
    #players start at the botton corners                                                                                 #
    #move to opposite diagonal corner to win                                                                             #
    #landing on an opponents marker rewars points and sends opponent back to start                                       #
    #Game ends when player gets boths markers on the opposite diagonal side                                              #
    #Winner is whoever achieves most points in the game                                                                  #
                                                                                                                         #
#Game mechanics:                                                                                                         #
    #Roll dice between 1 and 4                                                                                           #
    #Allow player to chose between their markers                                                                         #
    #Prompt player to select direction to move (up, left , right are the only available moves)                           #
    #if direction doesnt not allow counter to move at least one space move is invalid, player loses turn                 #
    #if number of moves greater the the available amount then player moves a valid number of spaces                      #
    #once a counter has arrived at the end space it can no longer be moved                                               #
                                                                                                                         #
#Scoring:                                                                                                                #
    #Landing on an opponent counter awards player with 1 point.                                                          #
    #Arriving first on the base awards 3 points next to arrive obtains 2 points, then 1                                  #
                                                                                                                         #
                                                                                                                         #
##########################################################################################################################
import random
import string

WIDTH = 7
player_one_marker =[57,58]
player_two_marker =[62,63]
players = []
char_player= []
star_char = []
player = 1       
game_on = True
player_score = [0,0]
BOARD = [ " " for x in range (0,64)]
goals = []


def print_rules ():

    print ("Game Rules:")

    print ("\n Take turns rolling a dice "
           "\n Players start at the bottom corners"
           "\n Move to opposite diagonal corner(base) to obtain points"
           "\n Arriving first on the base awards 4 points next to arrive obtains 3 points, then 2 ect "
           "\n Landing on an opponents marker rewadrs 1 point and sends them back to the start"
           "\n Collecting [x] will also award you points, the [x] in the middle of the board gives a bonus point"
           "\n Game ends when all players get boths markers on the opposite diagonal side (base)"
           "\n Winner is whoever achieves most points in the game")


def dice_roll ():

    #Creates a randomly generated dice roll.

    dice = random.randint(1,4)

    return dice


def board_walls():#Generates the walls that chnage the shape of the board.

    for x in range (1,64):

        if (x <= 5 and x >= 3) or (x <= 12 and x >= 10) or (x == 18):

            BOARD[x] = chr(9632)*3
              
        elif (x <= 61 and x >= 59) or (x <= 54  and x >= 52) or (x == 46):

            BOARD[x] = chr(9632)*3

        elif (x == 15 or x == 43) or (x <= 30 and x >= 29) or (x <= 23 and x >= 22)or (x <= 37 and x >= 36):
            
            BOARD[x] = chr(9632)*3

        elif (x == 21 or x == 49) or (x <= 28 and x >= 27) or (x <= 35 and x >= 34)or (x <= 42 and x >= 41):
      
            BOARD[x] = chr(9632)*3


def draw_BOARD():

    
    #Builds and displays board
    
    BOARD[player_one_marker[0]] = char_player [1]
    BOARD[player_one_marker[1]] = char_player [0]
    BOARD[player_two_marker[0]] = char_player [3]
    BOARD[player_two_marker[1]] = char_player [2]

    board_walls()

    print ("  ",char_player [2][:1],"  ",char_player [2][:1]," " * 23,char_player [0][:1],"  ",char_player [0][:1])

    print ("-"*43)
        
    for x in range (1,64):
                
        if x % WIDTH == 0:
            

            print (("|"),str(BOARD[x]).rjust(3," "),"|")

            print ("-"*43)
            
        else:
            print( "|",str(BOARD[x]).rjust(3," "),end =" ")


def move_direction(dice,player_move,marker_position,player,index_marker):

    count = 0
    
    if player == 0:
        # Takes players choice of direction, location, and dice and uses them to work out where the player will be places after moving. 

        if player_move == 3:
            
            BOARD[player_one_marker[index_marker - 1]] = " "

            new_pos = check_border (dice,marker_position,player_move)

            if  new_pos < marker_position :

                player_one_marker[index_marker - 1] = new_pos

            elif new_pos < 8:
                 player_one_marker[index_marker - 1] = new_pos

            else:
                player_one_marker [index_marker - 1] = marker_position - (dice*WIDTH)


        elif player_move == 2:
            BOARD[player_one_marker[index_marker - 1]] = " "

            new_pos = check_border (dice,marker_position,player_move)

            while count <= 63:

                # While loops are used to make sure if the player is on a boarder they will stay on the boarder

                if new_pos > marker_position or new_pos == (7+count):

                    player_one_marker[index_marker - 1] = new_pos

                    count = 70
                    
                count += 7
     
            if new_pos == marker_position +1:
                 player_one_marker[index_marker - 1] = marker_position + dice

        elif player_move == 1:
             BOARD[player_one_marker[index_marker - 1]] = " "

             new_pos = check_border (dice,marker_position,player_move)

             while count <= 57:

                if new_pos < marker_position or new_pos == (1+count) :

                    player_one_marker[index_marker - 1] = new_pos

                count += 7
                 
             if new_pos == marker_position +1:
                 player_one_marker[index_marker - 1] = marker_position - dice

        wall_collision(play_move,index_marker,dice)  
            
        if index_marker - 1 == 0:
            BOARD[player_one_marker[index_marker - 1]] = char_player [1]

        elif index_marker - 1 == 1:
            BOARD[player_one_marker[index_marker - 1]] = char_player [0]        
            
    if player == 1:

        # Takes players choice of direction, location, and dice and uses them to work out where the player will be places after moving. 
        
        if player_move == 3:
            BOARD[player_two_marker[index_marker - 1]] = " "
            new_pos = check_border (dice,marker_position,player_move)

            if  new_pos < marker_position:
                
                player_two_marker[index_marker - 1] = new_pos

            elif new_pos < 8:
                 player_two_marker[index_marker - 1] = new_pos

            else:
                player_two_marker [index_marker - 1] = marker_position - (dice*WIDTH)
            
        elif player_move == 2:
            BOARD[player_two_marker[index_marker - 1]] = " "

            new_pos = check_border (dice,marker_position,player_move)

            while count <= 70:#checks right boundries
               
                if new_pos > marker_position or new_pos == (7+count):

                    player_two_marker[index_marker - 1] = new_pos

                count += 7
                     
            if new_pos == marker_position +1:
            
                player_two_marker[index_marker - 1] = marker_position + dice
                               
        elif player_move == 1:#checks left boundries
             BOARD[player_two_marker[index_marker - 1]] = " "
             
             new_pos = check_border (dice,marker_position,player_move)

             while count <= 57:
           

                if new_pos < marker_position or new_pos == (1+count):

                    player_two_marker[index_marker - 1] = new_pos

                count += 7
                 
             if new_pos == marker_position +1:
                player_two_marker[index_marker - 1] = marker_position - dice


        wall_collisionP2 (play_move,index_marker,dice)
             
        if index_marker - 1 == 0:
            BOARD[player_two_marker[index_marker - 1]] = char_player [3]

        elif index_marker - 1 == 1:
             BOARD[player_two_marker[index_marker - 1]] = char_player [2]


def check_border (dice,marker_position,player_move):#checks if the player has hit the edge of the board

    count = 7
    new_marker_position = marker_position + 1
    left_border = 1

    if player_move == 1:

        left_border = 1    

    # checks if the player is going out of boarders on left 
        while left_border <= marker_position:

            if (marker_position - dice) <= left_border:
                new_marker_position = left_border
        
            left_border = left_border + count
        
    if player_move == 2:

        # checks if player is going out of boarders on right
        right_border = 70

        while right_border >= marker_position:
            
            if (marker_position + dice)>= right_border :
            
                new_marker_position = right_border

            right_border = right_border - count

# checks if player si going out the top border

    if player_move == 3:
        
        top_border = 1
        left_border = 1 

        for col in range (1, 10):

            pos_dif = ( marker_position - left_border)+1

            left_border = left_border + 7

            for top_border in range (1,8):

                if pos_dif == top_border:
                
                    if (marker_position - (dice*WIDTH))<= top_border :                        
                        
                        new_marker_position = top_border       

    return new_marker_position


def player_move (dice):

    # Allowes the player to pick which direction the want to move.
    # try catch used to stop game from breaking.

    print("{}'s turn".format(players[player]))
    
    while True:
    
        try:

            print ("You rolled a {}\n would you like to move \n 1)left \n 2)right \n 3)up ".format(dice))
            user_input = int(input())    

            while 1< user_input > 3 or user_input == 0:
                print ("Invalid input, please enter one of the valid inputs \n 1)left \n 2)right \n 3)up ")
                user_input = int(input())

            
            if user_input >= 1 and user_input <= 3:

                break 

        except ValueError:

             print ("Invalid input")
             print (" ")

    return user_input


def get_players ():#gets the player

    char_at_player = ""
    char = " "
    # gets the name of the player and stores it in an array.
    
    for count in range (0,2):
        print("What is the name of player {}".format (count+1))
        
        player_name = input()

        for char in player_name:
        
            while char not in string.ascii_letters:

                print("Invalid, please input a another name")

                player_name = input()

                for x in player_name:
                    char = x

            break
                    
        players.append(player_name)
        
        for count in range (0,2):

            #Using splicing to get the first letter of the players name which will be used as that players marker for the game.

            if count == 1:
                char_at_player = player_name[:1] +"1"
                char_player.append (char_at_player)

            else:
                char_at_player = player_name[:1] +"2"
                char_player.append (char_at_player)

                
def player_turn (player,marker): # assigns the player and the marker to be used on set turn
    
    if player == 0:
        
        if marker == 1:
            play_check = player_one_marker [0]
        elif marker == 2:
            play_check = player_one_marker [1]

    elif player == 1:
        
        if marker == 1:

            play_check = player_two_marker [0]
        elif marker == 2:
            play_check = player_two_marker [1]

    return play_check


def scoring (player, marker_position): # check which player arrives at the end point in which order and awards points accordingly.
  
        #check if a player has landed of one of the end sqaures.
        #gives points acordingly

    for count in range (0,2):
        
        if player == 0:
            
            if player_one_marker[count] == 6:
                
                if player_one_marker[count] not in goals:

                    player_score [0] += 4 - len(goals)

                    goals.append (player_one_marker[count])


            elif player_one_marker[count] == 7:

                if player_one_marker[count] not in goals:

                    player_score [0] += 4 - len(goals)

                    goals.append (player_one_marker[count])

        if player == 1:
            
              if player_two_marker[count] == 1:
                  
                    if player_two_marker[count] not in goals:

                        player_score [1] += 4 - len(goals)

                        goals.append (player_two_marker[count])


              elif player_two_marker[count] == 2:

                    if player_two_marker[count] not in goals:

                        player_score [1] += 4 - len(goals)

                        goals.append (player_two_marker[count])

                   
def check_win(BOARD):  # checks the move of the payer if there is a win condition

    global player

    game_is_on = True
# checks to see if the opposite corners of the board are populated.

    # Used to check if both the players markers have arrives at the end point, if so player is no longer allowed to move and thier turn is passed.        
    
    if (player_one_marker [0] == 6 or player_one_marker [0] == 7 ) and (player_one_marker [1] == 6 or player_one_marker [1] == 7) :   

         print ("{} has No moves remaining.". format (players[0]))

         player = 0


    if (player_two_marker [0] == 1 or player_two_marker [0] == 2)  and (player_two_marker [1] == 1 or player_two_marker [1] == 2 ):

         print (" {} has No moves remaining.". format (players[1]))

         player = 1

    while BOARD[1]is not " " and BOARD[2]is not " " and BOARD[6]is not " " and BOARD[7]is not " ":

# If right corner has the correct markers the left must also contain correct marker and the game ends.

        if (player_one_marker [0] == 6 or player_one_marker [0] == 7 ) and (player_one_marker [1] == 6 or player_one_marker [1] == 7 ):

            draw_BOARD()

            print("Game Over!")

            if player_score[0] > player_score[1]:

                print ("{} WINS !".format (players[0]))

            elif player_score[0] > player_score[1]:

                print ("It's a draw")

            else:
                print ("{} WINS !".format (players[1]))


            blank_input = input("press any key to close")

            game_is_on = False
            break

    return game_is_on


def Check_collision (player,index_marker,marker_pos,play_move):
    
    # checks if a player marker collides with another marker.
    # if the marker landed on belongs to the opposite player, that players marker is returned to the start.
    # otherwise if the players lands on another of his markers the marker will be places either left or right of the marker already in place
    
    if player == 0:

        # Cheack if player is colliding with opposite player

            if player_one_marker[0] == player_two_marker[0]:

                player_two_marker[0] = 62
                player_score[0] +=1

            elif player_one_marker[0] == player_two_marker[1]:

                player_two_marker[1] = 63
                player_score[0]+=1

            elif player_one_marker[1] == player_two_marker[0]:
  
                player_two_marker[0] = 62
                player_score[0] +=1

            elif  player_one_marker[1] == player_two_marker[1]:

                player_two_marker[1] = 63
                player_score[0] +=1

            #checks if player has collided with a star. so that they correct amount of points may be added

            count = 24

            while count < 41:

                if player_one_marker[index_marker - 1] == count:

                    if star_char[0] != "" and count == 24:
                        star_char[0] = ""
                        player_score[0] +=1
                        
                    if star_char[1] != "" and count == 26:
                        star_char[1] = ""
                        player_score[0] +=1
                        

                if count == 38:
                    if player_one_marker[index_marker - 1] == count:

                        if star_char[2] != "" and count == 38:
                            star_char[2] = ""
                            player_score[0] +=1
                        
                if player_one_marker[index_marker - 1] == 40:
                    
                    if star_char[3] != "" and count == 40:
                        
                        star_char[3] = ""
                        player_score[0] +=1
                        
                count +=2

            if player_one_marker[index_marker - 1] == 32:
                if star_char[4] != "":
                    player_score[0] +=2

            if play_move == 1:

            #checks collision against other player marker

                if index_marker -1 == 0:
                    
                    if player_one_marker[0] == player_one_marker [1]:

                        player_one_marker[0] = player_one_marker[1]+1

                elif index_marker -1 == 1:
                    
                
                    if player_one_marker[1] == player_one_marker [0]:

                        player_one_marker[1] = player_one_marker[1]+1   

            if play_move == 2:

                    if index_marker -1 == 0:

                        if player_one_marker[0] == player_one_marker [1]:

                            player_one_marker[0] = player_one_marker[1]-1                            

                    elif index_marker -1 == 1:

                        if player_one_marker[1] == player_one_marker [0]:

                            player_one_marker[1] = player_one_marker[1]-1

            if play_move == 3:

                if index_marker -1 == 0:

                    if player_one_marker[0] == player_one_marker [1]:

                        player_one_marker[0] = player_one_marker[1]+WIDTH
                        
                elif index_marker -1 == 1:

                        if player_one_marker[1] == player_one_marker [0]:

                            player_one_marker[1] = player_one_marker[0]+WIDTH
                            
    elif player == 1:

        if player_two_marker[0] == player_one_marker[0]:

             player_one_marker[0] = 57
             player_score[1] +=1

        elif player_two_marker[0] == player_one_marker[1]:

             player_one_marker[1] = 58
             player_score[1] +=1            

        elif player_two_marker[1] == player_one_marker[0] :

            player_one_marker[0] = 57
            player_score[1] +=1

        elif player_two_marker[1] == player_one_marker[1]:

            player_one_marker[1] = 58
            player_score[1] +=1

        count = 24

        while count < 41:

            if player_two_marker[index_marker - 1] == count:

                if star_char[0] != "" and count == 24:
                    star_char[0] = ""
                    player_score[1] +=1
                    
                if star_char[1] != "" and count == 26:
                    star_char[1] = ""
                    player_score[1] +=1                    

            if count == 38:

                if player_two_marker[index_marker - 1] == count:

                    if star_char[2] != "" and count == 38:
                        star_char[2] = ""
                        player_score[1] +=1
                    
            if player_one_marker[index_marker - 1] == 40:
                
                if star_char[3] != "" :
                    
                    star_char[3] = ""
                    player_score[0] +=1
            count +=2

        if player_two_marker[index_marker - 1] == 32:
            if star_char[4] != "":
                player_score[1] +=2

        if play_move == 1:

            #checks collision against other player marker

            if index_marker -1 == 0:
                
                if player_two_marker[0] == player_two_marker [1]:

                    player_two_marker[0] = player_two_marker[1]+1

            elif index_marker -1 == 1:
                
            
                if player_two_marker[1] == player_two_marker [0]:

                    player_two_marker[1] = player_two_marker[1]+1   

        if play_move == 2:

                
                if index_marker -1 == 0:

                    if player_two_marker[0] == player_two_marker [1]:

                        player_two_marker[0] = player_two_marker[1]-1
                        

                elif index_marker -1 == 1:


                    if player_two_marker[1] == player_two_marker [0]:

                        player_two_marker[1] = player_two_marker[1]-1

        if play_move == 3:

            if index_marker -1 == 0:

                if player_one_marker[0] == player_one_marker [1]:

                    player_one_marker[0] = player_one_marker[1]+WIDTH
                    

            elif index_marker -1 == 1:

                    if player_two_marker[1] == player_two_marker [0]:

                        player_two_marker[1] = player_two_marker[0]+WIDTH
                        

def select_marker (player):

    # Allowes the player to select which marker they would like to move

    while True:

        try: # try catch used to ensure game wont break should any errors occure.

            print ("Which marker do you wish to move ? 1 or 2")
            marker =  int(input())

            # Checks if the marker the player is trying to move is already at the end
            # If so the marker will not be available to move and the player is asked to choose again.
                 

            while 1 < marker >2 or marker == 0:

                print ("Invalid input, please select either 1 or 2")
                marker =  int(input())

            if marker == 1 or marker == 2:
                break

        except ValueError:#Throws exception so game does not break
            print("Invlid Marker ")

    for count in range (0,2):# checks to see if a player marker has reach the end, if so that marker can no longer move

        if player == 0:

            while player_one_marker[marker-1] == count + 6:

                print ("Marker no longer available, please select a different marker")
                marker =  int(input())
                    
        elif player == 1:

            while player_two_marker[marker-1] == count +1:

                print ("Marker no longer available, please select a different marker")
                marker =  int(input())   

    return marker


def wall_collisionP2 (play_move,index_marker,dice):#check collision against walls for player 2

    if play_move == 1: # left wall collision
        
        count = 15

        while count < 50:

            if player_two_marker[index_marker-1] == 15 :
                
                player_two_marker[index_marker-1] +=1

                break
                 
            if BOARD[player_two_marker[index_marker-1]] == chr(9632)*3 :
                
                player_two_marker[index_marker-1] +=1
            
            elif (player_two_marker[index_marker- 1] == 2) or (player_two_marker[index_marker- 1] == 9):
                
                player_two_marker[index_marker-1] += 1

            elif ((player_two_marker[index_marker -1] + dice) > 18) and player_two_marker[index_marker -1] < 18:

                player_two_marker[index_marker-1] = 18 +1
                
            elif (player_two_marker[index_marker -1] + dice) > 46 and player_two_marker[index_marker -1] < 46:

                player_two_marker[index_marker-1] = 46 +1

            count += 7
    
    if play_move == 2:# right wall check

        count = 21

        while count < 56:

            if BOARD[player_two_marker[index_marker-1]] == chr(9632)*3:

                player_two_marker[index_marker-1] = player_two_marker[index_marker-1] - 1

            elif (player_two_marker[index_marker- 1] == 6) or (player_two_marker[index_marker- 1] == 13):

                player_two_marker[index_marker-1] = player_two_marker[index_marker-1] - 1

            elif (player_two_marker[index_marker- 1] == 55) or (player_two_marker[index_marker- 1] == 62):

                player_two_marker[index_marker-1] = player_two_marker[index_marker-1] - 1

            elif (player_two_marker[index_marker -1] - dice) < 18 and player_two_marker[index_marker -1] > 18:

                player_two_marker[index_marker-1] = 18 +1

            count += 7

        if (player_two_marker[index_marker -1] - dice) < 14 and player_two_marker[index_marker -1] > 14:

            player_two_marker[index_marker-1] = 14

    if play_move == 3: # up check

        for count in range (0,21):

             if BOARD[player_two_marker[index_marker-1]] == chr(9632)*3 :

                    player_two_marker[index_marker-1] = player_two_marker[index_marker-1]+ WIDTH

             elif (player_two_marker[index_marker- 1] == 20):
            
                    player_two_marker[index_marker-1] = player_two_marker[index_marker-1]+ WIDTH


def wall_collision (play_move,index_marker,dice): #check collision against walls for player 1

    if play_move == 1: # left wall collision

        count = 15

        while count < 50:

            if BOARD[player_one_marker[index_marker-1]] == chr(9632)*3 :

                player_one_marker[index_marker-1] +=1

            elif (player_one_marker[index_marker- 1] == 2) or (player_one_marker[index_marker- 1] == 9):
                
                player_one_marker[index_marker-1] += 1

            elif (player_one_marker[index_marker -1] + dice) > 18 and player_one_marker[index_marker -1] < 18:

                player_one_marker[index_marker-1] = 18 +1

            count += 7
            
    if play_move == 2:# right wall check

        count = 21

        while count < 56:

            if BOARD[player_one_marker[index_marker-1]] == chr(9632)*3:

                player_one_marker[index_marker-1] = player_one_marker[index_marker-1] - 1

            elif (player_one_marker[index_marker- 1] == 6) or (player_one_marker[index_marker- 1] == 13):

                player_one_marker[index_marker-1] = player_one_marker[index_marker-1] - 1

            elif (player_one_marker[index_marker- 1] == 55) or (player_one_marker[index_marker- 1] == 62):

                player_one_marker[index_marker-1] = player_one_marker[index_marker-1] - 1

            elif (player_one_marker[index_marker -1] - dice) < 46 and player_one_marker[index_marker -1] > 46:

                player_one_marker[index_marker-1] = 46 -1

            count += 7

        if (player_one_marker[index_marker -1] - dice) < 14 and player_one_marker[index_marker -1] > 14:

            player_one_marker[index_marker-1] = 14

    if play_move == 3: #up check 

        for count in range (0,21):

             if BOARD[player_one_marker[index_marker-1]] == chr(9632)*3 :

                    player_one_marker[index_marker-1] = player_one_marker[index_marker-1]+ WIDTH

             elif (player_one_marker[index_marker- 1] == 16):
            
                    player_one_marker[index_marker-1] = player_one_marker[index_marker-1]+ WIDTH
                    

def stars (): # positions stars on the board.

    for count in range (0,5):
        star_char.append("x")

    BOARD[24]= "[x]"
    BOARD[26]= "[x]"
    BOARD[38]= "[x]"
    BOARD[40]= "[x]"
    BOARD[32]= "[x]"

    
print_rules()
print(" ")
get_players()
stars ()


# Main game loop
# Could be Main function passing in key variables.
while game_on:

    draw_BOARD()
    
    player = (player + 1) % 2
        
    dice_num = dice_roll()
    
    play_move = player_move(dice_num)

    which_marker = select_marker(player)

    play_check = player_turn (player,which_marker)
        
    move_direction(dice_num,play_move,play_check,player,which_marker)

    Check_collision (player,which_marker,play_check,play_move)
    
    scoring (player, play_check)
    
    game_on = check_win(BOARD)

    print (player_score)



    

        


    
   

        

    
   

    
    


