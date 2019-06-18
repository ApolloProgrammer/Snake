from tkinter import *
import random
import time

class Grid:
    def __init__(self,master,rows,cols,size,space):
        for i in range(rows):
            for j in range(cols):
                master.create_rectangle(i*size+space, j*size+space, i*size+size+space, j*size+size+space, fill="black", outline="white")

class Node:
    def __init__(self,master,size):
        self.canvas=master
        self.size=size
        self.x,self.y=random.randint(1, 15), random.randint(1, 15)  #random selection
        self.space=3
        self.x_dir,self.y_dir=0,0
        self.x_coordinate1, self.y_coordinate1 = self.x * self.size + self.space - self.size, self.y * self.size + self.space - self.size
        self.x_coordinate2, self.y_coordinate2 = (self.x + 1) * self.size + self.space - self.size, (self.y + 1) * self.size + self.space - self.size
        self.coordinates_history=[]
    def move(self):
        self.x_previous,self.y_previous=self.x,self.y
        if self.x_dir==1 and self.x==15:
            self.x=0
        if self.x_dir==-1 and self.x==0:
            self.x=16
        if self.y_dir==1 and self.y==15:
            self.y=0
        if self.y_dir==-1 and self.y==0:
            self.y=16

        if self.x_dir==1:
            self.x+=1
        elif self.x_dir==-1:
            self.x-=1

        if self.y_dir==1:
            self.y+=1
        elif self.y_dir==-1:
            self.y-=1

        self.coordinates_history.append([self.x_previous,self.y_previous])


    def draw(self):
        self.canvas.create_rectangle(self.x_coordinate1, self.y_coordinate1, self.x_coordinate2, self.y_coordinate2,fill="black", outline="white")
        self.x_coordinate1,self.y_coordinate1=self.x*self.size+self.space-self.size,self.y*self.size+self.space-self.size
        self.x_coordinate2,self.y_coordinate2=(self.x+1)*self.size+self.space-self.size,(self.y+1)*self.size+self.space-self.size
        self.canvas.create_rectangle(self.x_coordinate1+1,self.y_coordinate1+1,self.x_coordinate2-1,self.y_coordinate2-1,fill="red", outline="black")

    def draw1(self,x,y):
        self.canvas.create_rectangle(self.x_coordinate1, self.y_coordinate1, self.x_coordinate2, self.y_coordinate2,fill="black", outline="white")
        self.x_coordinate1,self.y_coordinate1=x*self.size+self.space-self.size,y*self.size+self.space-self.size
        self.x_coordinate2,self.y_coordinate2=(x+1)*self.size+self.space-self.size,(y+1)*self.size+self.space-self.size
        self.canvas.create_rectangle(self.x_coordinate1+1,self.y_coordinate1+1,self.x_coordinate2-1,self.y_coordinate2-1,fill="red", outline="black")

class Snake:
    def __init__(self,canvas,size):
        self.head=Node(canvas,size)
        self.body=[]

    def add(self,canvas,size):
        newNode=Node(canvas,size)
        self.body.append(newNode)

    def giveCoordinates(self,n):
        coordinates = self.head.__getattribute__('coordinates_history')[-n]
        return coordinates

class Food:
    def __init__(self, master, size):
        self.canvas = master
        self.size = size
        self.x, self.y = random.randint(1, 15), random.randint(1, 15)  #random selection
        self.space = 3

    def draw(self):
        self.x, self.y = random.randint(1,15), random.randint(1,15)  #random selection
        self.x_coordinate1, self.y_coordinate1 = self.x * self.size + self.space - self.size, self.y * self.size + self.space - self.size
        self.x_coordinate2, self.y_coordinate2 = (self.x + 1) * self.size + self.space - self.size, (self.y + 1) * self.size + self.space - self.size
        self.canvas.create_rectangle(self.x_coordinate1 + 1, self.y_coordinate1 + 1, self.x_coordinate2 - 1,self.y_coordinate2 - 1, fill="white")

def main():
    game=True
    rows,cols=15,15
    size=20
    space=3
    previous_coordinates=[]
    root = Tk()
    root.title('Snake')
    canvas = Canvas(width=303, height=303)
    canvas.pack()
    Grid(canvas,rows,cols,size,space)
    snake=Snake(canvas,size)
    head = snake.__getattribute__('head')
    food=Food(canvas, size)
    food.draw()
    while game==True:
        body = snake.__getattribute__('body')
        def up(event):
            head.__setattr__('y_dir', -1)  # UP ARROW
            head.__setattr__('x_dir', 0)
        def down(event):
            head.__setattr__('y_dir', 1)  # DOWN ARROW
            head.__setattr__('x_dir', 0)
        def left(event):
            head.__setattr__('x_dir', -1)  # LEFT ARROW
            head.__setattr__('y_dir', 0)
        def right(event):
            head.__setattr__('x_dir', 1)  # RIGHT ARROW
            head.__setattr__('y_dir', 0)

        root.bind('<Up>', up)
        root.bind('<Down>',down)
        root.bind('<Left>', left)
        root.bind('<Right>',right)


        if head.__getattribute__('x')==food.__getattribute__('x') and head.__getattribute__('y')==food.__getattribute__('y'):
            food.draw()
            snake.add(canvas,size)

        head.move()
        head.draw()
        if len(body)>=1:
            body=snake.__getattribute__('body')
            n=1
            for rect in body:
                x,y = snake.giveCoordinates(n)
                rect.draw1(x,y)
                if head.__getattribute__('x') == x and head.__getattribute__( 'y') == y:
                    game = False
                n+=1

        time.sleep(0.15)
        root.update()
    w = Label(root, text="GAME OVER!").pack()
    root.mainloop()

if __name__== "__main__":
  main()