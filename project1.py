"""Project"""

import turtle
import random
import math
import os

def draw_boxes():
    """draw the box and color-theme for the game"""
    a = turtle.Screen()
    a.setup(width = 1000, height = 700)
    a.bgcolor("gray")
    a.title("Memory Card Game")

    j = turtle.Turtle()
    j.hideturtle()

    j.color("pink","white")
    j.speed(10)
    # get to starting pos
    j.penup()
    j.goto(-440, 310)
    j.right(90)
    j.pendown()
    
    # main box
    j.begin_fill()
    j.width(5)
    # borders
    j.forward(530)
    j.left(90)
    j.forward(640)
    j.left(90)
    j.forward(530)
    j.left(90)
    j.forward(640)
    j.end_fill()
    
    # go to second pos
    j.penup()
    j.left(90)
    j.goto(-440, -245)
    j.pendown()

    # tries board
    j.begin_fill()
    j.forward(59)
    j.left(90)
    j.forward(640)
    j.left(90)
    j.forward(59)
    j.left(90)
    j.forward(640)
    j.end_fill()

    j.penup()
    j.goto(240, 310)
    j.left(90)
    j.pendown()

    # leaderboard
    j.begin_fill()
    j.forward(530)
    j.left(90)
    j.forward(200)
    j.left(90)
    j.forward(530)
    j.left(90)
    j.forward(200)
    j.end_fill()

    j.penup()
    j.left(90)
    j.goto(240, -249)
    j.pendown()

   
def get_coord(x, y):
    """needed this during the styling stage to get coordinate 
    to put turtles"""
    print(x, y)

def quit_button():
    """quit button"""
    a = turtle.Screen()
    a.register_shape("quitbutton.gif")
    quit_button = turtle.Turtle()
    quit_button.penup()
    quit_button.speed(0)
    quit_button.setpos(337, -282)
    quit_button.shape("quitbutton.gif")
    quit_button.onclick(lambda x, y: turtle.bye())
    

flip_card = []

def name_popup():
    name_input = turtle.textinput('Name window','Please enter your name')
    if name_input:
        player_name = turtle.Turtle()
        player_name.penup()
        player_name.hideturtle()
        player_name.setpos(-435, 320)
        player_name.color("pink")
        player_name.write(name_input, font=("Arial", 16, "bold"))
        return name_input
    # return player name
    else:
        name_input = "No name entered"
        player_name = turtle.Turtle()
        player_name.penup()
        player_name.hideturtle()
        player_name.setpos(-435, 320)
        player_name.color("pink")
        player_name.write(name_input, font=("Arial", 16, "bold"))
        print("No name entered")
NAME = name_popup()

POINTS = []
TURNS = []

def guess():
    """count the integer counter to use in amount of guesses of player"""
    guess_count = len(TURNS)/2
    return math.floor(guess_count)


draw_boxes()
quit_button()


def card_amount_popup():
    """card number popup"""
    x = False
    while x is False:
        card_input = turtle.textinput("Card selection", "Number of card to play? (8, 10, 12)")
        if card_input:
            if card_input in {'8', '10', '12'}:
                # game is limit to only 3 play mode
                # limit input to these 3
                card_input_amount = turtle.Turtle()
                card_input_amount.penup()
                card_input_amount.hideturtle()
                card_input_amount.setpos(432, 320)
                card_input_amount.color("pink")
                # styling
                card_input_amount.write(card_input, font=("Arial", 13, "bold"))
                x = True
                card_amount.append(card_input)
                # print(card_amount)
            else:
                print(f"Invalid input: {card_input}, only accept 8, 10, or 12")
                x = False
                # protective
        else:
            print("Please enter card to play")
            x = False
            # protective

def remove():
    """"remove turtle"""
    for each in flip_card:
        each.hideturtle()

def reset_card():
    """reset the card if wrong match"""
    for each in flip_card:
        each.shape("card_back.gif")

def card_click(face_turtle, x, y,):
    """default card back face"""
    face_turtle.shape("card_back.gif")
    face_turtle.penup()
    face_turtle.setpos(x, y)

score = turtle.Turtle()
attempts = turtle.Turtle()   
gues = turtle.Turtle()

score.speed(0)
attempts.speed(0)
gues.speed(0)

score.penup()
attempts.penup()
gues.penup()

score.setpos(-410, -285)
attempts.setpos(-250, -285)
gues.setpos(-90, -285)

score.hideturtle()
attempts.hideturtle()
gues.hideturtle()

msg1 = f"Score: {len(POINTS)}"
msg2 = f"Tries: {len(TURNS)}" 
msg3 = f"Guesses: {guess()}"

score.write(msg1, font=("Arial", 12, "bold"))
attempts.write(msg2, font=("Arial", 12, "bold")) 
gues.write(msg3, font=("Arial", 12, "bold"))

WIN_BOOL = False

score_board_title = turtle.Turtle()
score_board_content = turtle.Turtle()
score_board_content.speed(0)
score_board_title.speed(0)
score_board_content.penup()
score_board_title.penup()
score_board_content.hideturtle()
score_board_title.hideturtle()

# styling for title 
score_board_title.setpos(250, 280)
msg4 = "Leaderboard:"
score_board_title.write(msg4, font=("Arial", 12, "bold"))

def load_n_write_leaderboard():
    if os.path.exists("Leaderboard.txt"):
        # first time you play make sure this doesnt throw error
        with open("Leaderboard.txt", mode='r+', encoding='utf-8') as file_loaded:
            file1 = file_loaded.readlines()
            empty_list = []

            for each in file1:
                each = each.strip()
                if each:
                    temp = each.split()
                    # making sure to get only the contents
                    # not the empty space
                    if len(temp) == 2:
                        name, score = temp
                        empty_list.append([name, score])

            # print(empty_list)
            top15entry = empty_list[:15] #limit to only top 15
            x = 250
            y = 255
            for i in top15entry:
                name, score = i
                score_board_content.setpos(x, y)
                score_board_content.write(f"{name}      {score}", font=("Arial", 12, "bold"))
                # each loop, lower the y axis
                y -= 30 
load_n_write_leaderboard()
      
def turn_card(turtle_obj, true_value, max_point):
    if len(flip_card) <= 2:
        # when clicked transform shape
        turtle_obj.shape(true_value)

        if len(flip_card) == 0:
            #add to working list
            flip_card.append(turtle_obj)

            # update score/tries
            score.clear()
            attempts.clear()
            gues.clear()
            TURNS.append(1)
            msg1 = f"Score: {len(POINTS)}"
            msg2 = f"Tries: {len(TURNS)}"
            msg3 = f"Guesses: {guess()}"

            score.write(msg1, font=("Arial", 12, "bold"))
            attempts.write(msg2, font=("Arial", 12, "bold"))
            gues.write(msg3, font=("Arial", 12, "bold"))

        elif len(flip_card) == 1: 
            # add the clicked card to working list
            if flip_card[0] != turtle_obj:
                flip_card.append(turtle_obj)

                # update score/tries
                score.clear()
                attempts.clear()
                gues.clear()
                TURNS.append(1)
                msg1 = f"Score: {len(POINTS)}"
                msg2 = f"Tries: {len(TURNS)}"
                msg3 = f"Guesses: {guess()}"

                score.write(msg1, font=("Arial", 12, "bold"))
                attempts.write(msg2, font=("Arial", 12, "bold"))
                gues.write(msg3, font=("Arial", 12, "bold"))
            else:
                print("Can't pick same card")
        # print(flip_card)
    
    if len(flip_card) == 2:
        # check the working llist
        if flip_card[0] != flip_card[1]:
            # make sure they dont get away w clicking on the same card
            if flip_card[0].shape() == flip_card[1].shape():
                # print("SAME")
                # checking to see if the value are same
                # updated moves/score
                score.clear()
                attempts.clear()
                gues.clear()
                POINTS.append(1)
                msg1 = f"Score: {len(POINTS)}"
                msg2 = f"Tries: {len(TURNS)}"
                msg3 = f"Guesses: {guess()}"

                score.write(msg1, font=("Arial", 12, "bold"))
                attempts.write(msg2, font=("Arial", 12, "bold"))
                gues.write(msg3, font=("Arial", 12, "bold"))

                remove()
                flip_card.clear()
               
                # winning msg
                if len(POINTS) == max_point:
                # if test == True: # this is for testing 
                    print("YOU WINNNN")
                    winmsg = turtle.Turtle()
                    winmsg.speed(0)
                    winmsg.penup()
                    winmsg.setpos(0, 0)
                    winmsg.shape("winner.gif")
                    WIN_BOOL = True
                    
                    player_sts = [NAME,guess()]  #blank out for testing 
                    # player_sts = ["Johnnytesting1", 14] #testing
                    player_sts = [player_sts[0], int(player_sts[1])]
                    
                    # open the leaderboard.txt file, if it doesn't exist
                    # it will be created
                    with open("Leaderboard.txt", mode='a+', encoding='utf-8') as file_loaded:
                        file_loaded.seek(0)
                        file1 = file_loaded.read()
                        
                        leaderboard = []
                        
                        # this add the txt content to list in python
                        # this also give them meaning
                        if file1:
                            for i in file1.splitlines():
                                temp_line = i.strip().split()
                                # print (temp_line)
                                leaderboard.append([temp_line[0], int(temp_line[1])])
                            # print(leaderboard)
                            # sorting
                            # if leaderboard is empty it add the point
                        if len(leaderboard) == 0:
                            leaderboard.append(player_sts)
                        else:
                            # add the current point n name
                            leaderboard.append(player_sts)

                            # this sort by points, lowest will be place first
                            leaderboard.sort(key=lambda x: x[1], reverse=False)
                            # print("sorting")
                            # print(leaderboard)
                            
                            # reset the file
                            file_loaded.seek(0)
                            file_loaded.truncate()  

                        # Write the updated leaderboard back to the file
                        for player in leaderboard:
                            # add each elements of the python list to txt file
                            file_loaded.write(f"{player[0]} {player[1]}\n")
                    
                    # refresh at the end and rewrite
                    score_board_content.clear()
                    load_n_write_leaderboard()
            else:
                # print("NOT SAME")
                # reset the card back to the back cover
                reset_card()
                flip_card.clear()

card_amount = []
total_card = []
activelist = []

def load_card():
    # 7 type of card
    list1 = ["2_of_clubs.gif", 
             "2_of_diamonds.gif", 
             "3_of_hearts.gif",
             "ace_of_diamonds.gif",
             "jack_of_spades.gif", 
             "king_of_diamonds.gif",
              "queen_of_hearts.gif"]
  
    if card_amount[0] == '8':
        # need 4 card
        list4card = random.sample(range(0, 7), 4)
        # print(list4card)

        for each in list4card:
            activelist.append(list1[each])
            activelist.append(list1[each])
        
        # active list contain all the name
        # of cards in a list, should be a list of dup
        # print(activelist)

        activelist_coord = random.sample(range(0, 8), 8)
        # coord is a random list of position
        # print(activelist_coord)

        # assigning card value
        card1 = turtle.Turtle()
        card_click(card1, -350, 215)
        card1.onclick(lambda x, y:turn_card(card1, activelist[activelist_coord[0]], 4))
        # turncard(turtle, true value randomize, max point to indicate when player win)
        card2 = turtle.Turtle()
        card_click(card2, -200, 215)
        card2.onclick(lambda x, y:turn_card(card2, activelist[activelist_coord[1]], 4))

        card3 = turtle.Turtle()
        card_click(card3, -50, 215)
        card3.onclick(lambda x, y:turn_card(card3, activelist[activelist_coord[2]], 4))
        
        card4 = turtle.Turtle()
        card_click(card4, 100, 215)
        card4.onclick(lambda x, y:turn_card(card4, activelist[activelist_coord[3]], 4))

        card5 = turtle.Turtle()
        card_click(card5, -350, 50)
        card5.onclick(lambda x, y:turn_card(card5, activelist[activelist_coord[4]], 4))

        card6 = turtle.Turtle()
        card_click(card6, -200, 50)
        card6.onclick(lambda x, y:turn_card(card6, activelist[activelist_coord[5]], 4))

        card7 = turtle.Turtle()
        card_click(card7, -50, 50)
        card7.onclick(lambda x, y:turn_card(card7, activelist[activelist_coord[6]], 4))
        
        card8 = turtle.Turtle()
        card_click(card8, 100, 50)
        card8.onclick(lambda x, y:turn_card(card8, activelist[activelist_coord[7]], 4))
        
    elif card_amount[0] == '10':
        # need 5 card
        list4card = random.sample(range(0, 7), 5)
        # print(list4card)

        for each in list4card:
            activelist.append(list1[each])
            activelist.append(list1[each])
        
        # active list contain all the name
        # of cards in a list, should be a list of dup
        # print(activelist)

        activelist_coord = random.sample(range(0, 10), 10)
        # coord is a random list of position
        # print(activelist_coord)

        card1 = turtle.Turtle()
        card_click(card1, -350, 215)
        card1.onclick(lambda x, y:turn_card(card1, activelist[activelist_coord[0]], 5))

        card2 = turtle.Turtle()
        card_click(card2, -200, 215)
        card2.onclick(lambda x, y:turn_card(card2, activelist[activelist_coord[1]], 5))

        card3 = turtle.Turtle()
        card_click(card3, -50, 215)
        card3.onclick(lambda x, y:turn_card(card3, activelist[activelist_coord[2]], 5))
        
        card4 = turtle.Turtle()
        card_click(card4, 100, 215)
        card4.onclick(lambda x, y:turn_card(card4, activelist[activelist_coord[3]], 5))

        card5 = turtle.Turtle()
        card_click(card5, -350, 50)
        card5.onclick(lambda x, y:turn_card(card5, activelist[activelist_coord[4]], 5))

        card6 = turtle.Turtle()
        card_click(card6, -200, 50)
        card6.onclick(lambda x, y:turn_card(card6, activelist[activelist_coord[5]], 5))

        card7 = turtle.Turtle()
        card_click(card7, -50, 50)
        card7.onclick(lambda x, y:turn_card(card7, activelist[activelist_coord[6]], 5))
        
        card8 = turtle.Turtle()
        card_click(card8, 100, 50)
        card8.onclick(lambda x, y:turn_card(card8, activelist[activelist_coord[7]], 5))

        card9 = turtle.Turtle()
        card_click(card9, -50, -115)
        card9.onclick(lambda x, y:turn_card(card9, activelist[activelist_coord[8]], 5))
        
        card10 = turtle.Turtle()
        card_click(card10, -350, -115)
        card10.onclick(lambda x, y:turn_card(card10, activelist[activelist_coord[9]], 5))

    elif card_amount[0] == '12':
        # need 6 card
        list4card = random.sample(range(0, 7), 6)

        # print(list4card)

        for each in list4card:
            activelist.append(list1[each])
            activelist.append(list1[each])
        
        # active list contain all the name
        # of cards in a list, should be a list of dup
        # print(activelist)

        activelist_coord = random.sample(range(0, 12), 12)
        # coord is a random list of position
        # print(activelist_coord)

        card1 = turtle.Turtle()
        card_click(card1, -350, 215)
        card1.onclick(lambda x, y:turn_card(card1, activelist[activelist_coord[0]], 6))

        card2 = turtle.Turtle()
        card_click(card2, -200, 215)
        card2.onclick(lambda x, y:turn_card(card2, activelist[activelist_coord[1]], 6))

        card3 = turtle.Turtle()
        card_click(card3, -50, 215)
        card3.onclick(lambda x, y:turn_card(card3, activelist[activelist_coord[2]], 6))
        
        card4 = turtle.Turtle()
        card_click(card4, 100, 215)
        card4.onclick(lambda x, y:turn_card(card4, activelist[activelist_coord[3]], 6))

        card5 = turtle.Turtle()
        card_click(card5, -350, 50)
        card5.onclick(lambda x, y:turn_card(card5, activelist[activelist_coord[4]], 6))

        card6 = turtle.Turtle()
        card_click(card6, -200, 50)
        card6.onclick(lambda x, y:turn_card(card6, activelist[activelist_coord[5]], 6))

        card7 = turtle.Turtle()
        card_click(card7, -50, 50)
        card7.onclick(lambda x, y:turn_card(card7, activelist[activelist_coord[6]], 6))
        
        card8 = turtle.Turtle()
        card_click(card8, 100, 50)
        card8.onclick(lambda x, y:turn_card(card8, activelist[activelist_coord[7]], 6))

        card9 = turtle.Turtle()
        card_click(card9, -50, -115)
        card9.onclick(lambda x, y:turn_card(card9, activelist[activelist_coord[8]], 6))
        
        card10 = turtle.Turtle()
        card_click(card10, -350, -115)
        card10.onclick(lambda x, y:turn_card(card10, activelist[activelist_coord[9]], 6))
    
        card11 = turtle.Turtle()
        card_click(card11, -200, -115)
        card11.onclick(lambda x, y:turn_card(card11, activelist[activelist_coord[10]], 6))
        
        card12 = turtle.Turtle()
        card_click(card12, 100, -115)
        card12.onclick(lambda x, y:turn_card(card12, activelist[activelist_coord[11]], 6))

def main():
    
    card_amount_popup()

    screen = turtle.Screen()
    screen.register_shape("card_back.gif")
    
    screen.register_shape("2_of_clubs.gif")
    screen.register_shape("2_of_diamonds.gif")
    screen.register_shape("3_of_hearts.gif")
    screen.register_shape("ace_of_diamonds.gif")
    screen.register_shape("jack_of_spades.gif")
    screen.register_shape("king_of_diamonds.gif")
    screen.register_shape("queen_of_hearts.gif")

    screen.register_shape("card_warning.gif")
    screen.register_shape("file_error.gif")
    screen.register_shape("leaderboard_error.gif")
    screen.register_shape("quitmsg.gif")
    screen.register_shape("winner.gif")

    load_card()

    turtle.done()

if __name__ == "__main__":
    main()
