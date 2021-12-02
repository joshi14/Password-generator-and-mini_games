import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
score=0
def low():
    entry.delete(0, END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""  
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")
def generate():
    password1 = low()
    entry.insert(10, password1)
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)
    root.destroy()
root = Tk()
var = IntVar()
var1 = IntVar()
root.title("Random Password Generator")
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
c_label = Label(root, text="Length")
c_label.grid(row=1)
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)
root.mainloop()

root1=Tk()
root1.geometry('500x300')
root1.title("LOGIN FOR GAMES")
label0=Label(root1,text="Username",width=20,font=("bold",10))
label0.grid(row=1,column=1)
label1=Label(root1,text="Password",width=20)
label1.grid(row=3,column=1)
entry0=Entry(root1)
entry0.grid(row=1,column=2)
entry1=Entry(root1)
entry1.grid(row=3,column=2)
def paste():
    password = pyperclip.paste()
    entry1.insert(10, password)
def login():
    root1.destroy()
paste_button=Button(root1,text="Paste",command=paste)
paste_button.grid(row=3,column=3)
login=Button(root1,text="Login",command=login)
login.grid(row=6,column=2)
root1.mainloop()

menu=Tk()
menu.geometry('300x100')
menu.title("GAMES AVAILABLE")
def game():
    import turtle
    import time
    import random
    wn = turtle.Screen()
    wn.title("Block Game")
    wn.bgcolor("NavajoWhite2")
    wn.setup(width=600, height=800)
    wn.tracer(0)
    delay = 0.1
    class Shape():
        def __init__(self):
            self.x = 5
            self.y = 0
            self.color = random.randint(1, 7)
            square = [[1,1],[1,1]]
            horizontal_line = [[1,1,1,1]]
            vertical_line = [[1],[1],[1],[1]]
            left_l = [[1,0,0,0],[1,1,1,1]]
            right_l = [[0,0,0,1],[1,1,1,1]]
            left_s = [[1,1,0],[0,1,1]]
            right_s = [[0,1,1],[1,1,0]]
            t = [[0,1,0],[1,1,1]]
            shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]
            self.shape = random.choice(shapes)                      
            self.height = len(self.shape)
            self.width = len(self.shape[0])
        def move_left(self, grid):
            if self.x > 0:
                if grid[self.y][self.x - 1] == 0:
                    self.erase_shape(grid)
                    self.x -= 1
        def move_right(self, grid):
            if self.x < 12 - self.width:
                if grid[self.y][self.x + self.width] == 0:
                    self.erase_shape(grid)
                    self.x += 1
        def draw_shape(self, grid):
            for y in range(self.height):
                for x in range(self.width):
                    if(self.shape[y][x]==1):
                        grid[self.y + y][self.x + x] = self.color        
        def erase_shape(self, grid):
            for y in range(self.height):
                for x in range(self.width):
                    if(self.shape[y][x]==1):
                        grid[self.y + y][self.x + x] = 0            
        def can_move(self, grid):
            result = True
            for x in range(self.width):
                if(self.shape[self.height-1][x] == 1):
                    if(grid[self.y + self.height][self.x + x] != 0):
                        result = False
            return result
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    pen = turtle.Turtle()
    pen.penup()
    pen.speed(0)
    pen.shape("square")
    pen.setundobuffer(None)  
    def draw_grid(pen, grid):
        pen.clear()
        top = 230
        left = -110  
        colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]  
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                screen_x = left + (x * 20)
                screen_y = top - (y * 20)
                color_number = grid[y][x]
                color = colors[color_number]
                pen.color(color)
                pen.goto(screen_x, screen_y)
                pen.stamp()
    def check_grid(grid):
        y = 23
        while y > 0:
            is_full = True
            for x in range(0, 12):
                if grid[y][x] == 0:
                    is_full = False
                    y -= 1
                    break
            if is_full:
                global score
                score += 10
                draw_score(pen, score)
                for copy_y in range(y, 0, -1):
                    for copy_x in range(0, 12):
                        grid[copy_y][copy_x] = grid[copy_y-1][copy_x]
    def draw_score(pen, score):
        pen.color("blue")
        pen.hideturtle()
        pen.goto(-75, 350)
        pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))
    shape = Shape()
    grid[shape.y][shape.x] = shape.color
    wn.listen()
    wn.onkeypress(lambda: shape.move_left(grid), "a")
    wn.onkeypress(lambda: shape.move_right(grid), "d")
    draw_score(pen, score)
    while True:
        wn.update()
        if shape.y == 23 - shape.height + 1:      
            shape = Shape()
            check_grid(grid)
        elif shape.can_move(grid):
            shape.erase_shape(grid)
            shape.y +=1
            shape.draw_shape(grid)
        else:
            shape = Shape()
            check_grid(grid)
        draw_grid(pen, grid)
        draw_score(pen, score)
        time.sleep(delay)
    wn.mainloop()
def snake():
    import turtle
    import time
    import random
    delay = 0.1
    score = 0
    high_score = 0
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    wn.tracer(0)
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)
    segments = []
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
    def go_up():
        if head.direction != "down":
            head.direction = "up"
    def go_down():
            if head.direction != "up":
                head.direction = "down"
    def go_left():
        if head.direction != "right":
            head.direction = "left"
    def go_right():
        if head.direction != "left":
            head.direction = "right"
    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    while True:
        wn.update()
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        time.sleep(delay)
    wn.mainloop()
snake=Button(menu,text="Tetris game",command=game)
snake.grid(row=1,column=2)
turtle=Button(menu,text="Snake game",command=snake)
turtle.grid(row=1,column=1)
menu.mainloop()