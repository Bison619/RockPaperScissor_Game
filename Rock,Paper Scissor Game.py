
import random
import pygame,sys

pygame.init()

# constansts
HEIGHT = 700
WIDTH = 700
COLOR = (255,255,255)
LINE_COLOR = (255,0,0)

screen = pygame.display.set_mode(( HEIGHT,WIDTH))
pygame.display.set_caption('Rock Paper Scissor Game')
screen.fill(COLOR)

def drawline():
    pygame.draw.line(screen,LINE_COLOR, (350,0), (350,700), 10 )

drawline()
#
# def game(comp, you):
#     valid = ["Rock","Paper","Scissor"]
#     if you not in valid :
#
#         return "Invalid"
#     if comp==you:
#         return "Tie"
#
#     if comp == "Rock":
#         if you == "Paper":
#             return True
#         elif you == "Scissor":
#             return False
#     if comp == "Paper":
#         if you == "Rock":
#             return False
#         elif you == "Scissor":
#             return True
#     if comp =="Scissor":
#         if you == "Rock":
#             return True
#         elif you == 'Paper':
#             return False
#
# # computer choosing random data
# print(" Computer will chose first ,")
# rando= random.randint(1,3)
# if rando ==1:
#     comp="Rock"
# elif rando ==2:
#     comp="Paper"
# else:
#     comp="Scissor"
#
# # User input
# you = input(" Choose from Rock(Rock) Paper(Paper) or Scissors(Scissor) : ")
# you.lower()
#
# # function call
# a = game(comp,you)
# if a=="Invalid":
#     print("That is not a valid word Or use Uppercase in word  ")
# elif a=="Tie":
#     print("It is a Tie Man :(")
# elif a:
#     print('You Winnnn ! ;)')
# else:
#     print('You Loose , Looserrr !! : | ')
#
# # Printing the choice user and comp take
# if a== "Invalid":
#     pass
# else:
#     print(f'You Choose {you} ')
#     print(f'Computer Choose {comp}')

# main loop of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()