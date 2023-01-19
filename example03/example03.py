# Создайте программу для игры в 'Крестики-нолики'

from tkinter import*
import random, time

def stop_game():
   global game_left
   for item in game_left:
      buttons[item]. config(bg = 'white', state = 'disabled')
      
def win(w):
   global game
   if (game[0]== w and game[1] == w and game[2] == w) or (game[3]== w and game[4] == w and game[5] == w)\
        or (game[6]== w and game[7] == w and game[8] == w) or (game[0]== w and game[3] == w and game[6] == w)\
        or (game[1]== w and game[4] == w and game[7] == w) or (game[2]== w and game[5] == w and game[8] == w)\
        or (game[0]== w and game[4] == w and game[8] == w) or (game[2]== w and game[4] == w and game[6] == w):
      return True

def push(m):
   global game
   global game_left
   global step
   game[m] = 'X'
   buttons[m].config(text = 'X', bg = 'white', state = 'disabled')
   game_left.remove(m)

   if m == 4 and step == 0:
       n = random.choice(game_left)
   elif m != 4 and step == 0:
      n = 4
   if step > 0:
      n = 8 - m
   if n not in game_left:
      try:
         n = random.choice(game_left)
      except IndexError:
         label['text'] = 'ИГРА ОКОНЧЕНА!!'
         stop_game()

   game[n] = '0'
   buttons[n].config(text = '0', bg = 'white', state = 'disabled')
   if win('X'):
      label['text'] = 'ВЫ ПОБЕДИЛИ!!'
      stop_game()
   elif win('0'):
      label['text'] = 'ВЫ ПРОИГРАЛИ!!'
      stop_game()
   else:
      if (len(game_left) > 1):
          game_left.remove(n)
      else:
          label['text'] = 'ИГРА ОКОНЧЕНА!!'
          stop_game()
      step += 1

game = [None] * 9
game_left = list(range(9))
step = 0
root = Tk()
label = Label(width=20, text = 'КРЕСТИКИ-НОЛИКИ', font=('Arial', 20, 'bold'))

buttons = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg= 'pink', command = lambda x = i: push(x)) for i in range(9)]


label.grid(row=0, column=0, columnspan=3)

row = 1; col = 0
for i in range(9):
   buttons[i].grid(row=row, column=col)
   col += 1
   if col == 3:
      row += 1
      col = 0

root.mainloop()