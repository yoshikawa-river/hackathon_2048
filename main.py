import tkinter as tk
import math
import random

canvas = None

SQUARE_LENGTH = 100
RADIUS = SQUARE_LENGTH / 2 - 5
POSITION = {"x": 8, "y": 8}
BORDER_WIDTH = 8
NUMBER = 4
LENGTH = SQUARE_LENGTH * NUMBER + BORDER_WIDTH * NUMBER
CELL_COLOR = '#cbbeb5'
BORDER_COLOR = '#b2a698'
CELL_MAX = 3

cells = []

def set_field():
  canvas.create_rectangle(POSITION["x"], POSITION["y"], LENGTH + POSITION["x"], LENGTH + POSITION["y"], fill='#cbbeb5', width=BORDER_WIDTH, outline=BORDER_COLOR)

  for i in range(NUMBER - 1):
    x = POSITION["x"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    y = POSITION["y"] + SQUARE_LENGTH * (i + 1) + BORDER_WIDTH * i + BORDER_WIDTH
    canvas.create_line(x, POSITION["y"], x, LENGTH + POSITION["y"], width=BORDER_WIDTH, fill=BORDER_COLOR)
    canvas.create_line(POSITION["x"], y, LENGTH + POSITION["x"], y, width=BORDER_WIDTH, fill=BORDER_COLOR)

def create_canvas():
  root = tk.Tk()
  root.geometry(f"""{LENGTH + POSITION["x"] * 2}x{LENGTH + POSITION["y"] * 2}""")
  root.title("2048")
  canvas = tk.Canvas(root, width=(LENGTH + POSITION["x"]), height=(LENGTH + POSITION["y"]))
  canvas.place(x=0, y=0)

  return root, canvas

def set_number(num, x, y):
    center_x = POSITION["x"] + BORDER_WIDTH * x + BORDER_WIDTH / 2 + SQUARE_LENGTH * x + SQUARE_LENGTH / 2
    center_y = POSITION["y"] + BORDER_WIDTH * y + BORDER_WIDTH / 2 + SQUARE_LENGTH * y + SQUARE_LENGTH / 2
    canvas.create_rectangle(center_x - SQUARE_LENGTH / 2, center_y - SQUARE_LENGTH / 2, center_x + SQUARE_LENGTH / 2, center_y + SQUARE_LENGTH / 2, fill=CELL_COLOR, width=0)
    if num != 0:
      canvas.create_text(center_x, center_y, text=num, justify="center", font=("", 70), tag="count_text")

def operate(event):
  if event.keysym == 'Up' or event.keysym == 'Down':#上下関数呼び出し
    move_vertical(event.keysym)
  else:#左右関数呼び出し
    move_side(event.keysym)
  new_field()

class Cell():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.count = 0

def change_number(x, y):
  number = y * NUMBER + x 
  return number

def move_vertical(key):#上下関数
  if key == 'Up':
    new_y = 0
  else:
    new_y = CELL_MAX
  for cell in cells:
    if cell.count != 0:
      if cell.y != new_y:
        new_num = change_number(cell.x, new_y)
        cells[new_num].count = cell.count
        cell.count = 0

def move_side(key):#左右関数
  if key == 'Left':
    new_x = 0
  else:
    new_x = CELL_MAX
  for cell in cells:
    if cell.count != 0:
      if cell.x != new_x:
        new_num = change_number(new_x, cell.y)
        cells[new_num].count = cell.count
        cell.count = 0

# def is_vertical(x, y):
#   number = change_number(x, y)
#   print(number)
#   if cells[number].count == 0:
#     return True
#   elif number > 15:
#     return False
#   else:
#     return False

# def vertical_bottom(x, y, old_num):
#   i = y
#   print(x, i)
#   while not is_vertical(x, i):
#     i += 1
#   new_num = change_number(x, i)
#   # print(new_num)
#   if cells[new_num].count == cells[old_num].count:
#     cells[new_num].count *= 2
#     cells[old_num].count = 0

# old_num = change_number(x, y)
  # deploy_count(new_count, old_count)
  
def new_field():#再描画
  for cell in cells:
    set_number(cell.count, cell.x, cell.y)

def create_cells():
  global cells
  for y in range(NUMBER):
    for x in range(NUMBER):
      cells.append(Cell(x, y))
      # print(x, y)

def test():
  cells[0].count = 2
  cells[10].count = 2
  set_number(cells[0].count, cells[0].x, cells[0].y)
  set_number(cells[10].count, cells[10].x, cells[10].y)

def play():
  global canvas
  root, canvas = create_canvas()
  set_field()
  create_cells()
  test()
  root.bind("<Key>", lambda event: operate(event))
  root.mainloop()

play()
