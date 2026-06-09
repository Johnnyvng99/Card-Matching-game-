import random
import math
import os.path
def count_down(count):
    if count == 0:            
        print('Go!')                  
    else:                        
        print(count)             
        count_down(count-1)
def main():
    count_down(5)
    
if __name__ == "__main__":
    main()

# TURNS = [1,1]

# GUESSES = len(TURNS)/2
# def guess():
#     guess_count = len(TURNS)/2
#     return math.floor(guess_count)

# print(guess())
# list1 = []
# print(len(list1))

# list1 = ["2_of_clubs.gif", 
#          "2_of_diamonds.gif", 
#         "3_of_hearts.gif",
#         "ace_of_diamonds.gif",
#         "jack_of_spades.gif", 
#         "king_of_diamonds.gif",
#         "queen_of_hearts.gif"]

# print(list1[6])


# front_face1 = turtle.Turtle()
# front_face2 = turtle.Turtle()
# front_face3 = turtle.Turtle()
# front_face4 = turtle.Turtle()
# front_face5 = turtle.Turtle()
# front_face6 = turtle.Turtle()
# front_face7 = turtle.Turtle()

# front_face8 = turtle.Turtle()
# front_face9 = turtle.Turtle()
# front_face10 = turtle.Turtle()
# front_face11 = turtle.Turtle()


# front_face.shape("card_back.gif")
# front_face1.shape("card_back.gif")
# front_face2.shape("card_back.gif")
# front_face3.shape("card_back.gif")
# front_face4.shape("card_back.gif")
# front_face5.shape("card_back.gif")
# front_face6.shape("card_back.gif")
# front_face7.shape("card_back.gif")

# front_face8.shape("card_back.gif")
# front_face9.shape("card_back.gif")
# front_face10.shape("card_back.gif")
# front_face11.shape("card_back.gif")

# # front_face.penup()
# front_face1.penup()
# front_face2.penup()
# front_face3.penup()
# front_face4.penup()
# front_face5.penup()
# front_face6.penup()
# front_face7.penup()

# front_face8.penup()
# front_face9.penup()
# front_face10.penup()
# front_face11.penup()

# # x-axis seperate by 150
# # y axis seperate by 165
# # front_face.setpos(-350, 215)
# front_face1.setpos(-200, 215)
# front_face2.setpos(-50, 215)
# front_face3.setpos(100, 215)
# front_face4.setpos(-350, 50)
# front_face5.setpos(-200, 50)
# front_face6.setpos(-50, 50)
# front_face7.setpos(100, 50)

# front_face8.setpos(-50, -115)
# front_face9.setpos(-350, -115)
# front_face10.setpos(-200, -115)
# front_face11.setpos(100, -115)

 # turtle.listen()
# click function to get coord
# # turtle.onscreenclick(get_coord, 1)
# def click(x , y):
#     if 309 < x < 365 and -298 < y < -262:
#         turtle.bye()
#     elif -369 < x < -305 and 145 < y < 289:
#         print("hello") 
    

