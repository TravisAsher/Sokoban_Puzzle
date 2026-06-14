#---------------------------------------------------------------------------------------------------------------
# Name:        Sokoban GUI Puzzle
# Purpose:     Plays a single iteration of Sokoban. I intend to edit this code in the future to allow for any
#              map iteration to be passed as input.
# Author:      Travis
#
# Created:     04/17/2018
#---------------------------------------------------------------------------------------------------------------

def printsep(number=92): print("-"*number)
def space(number=1): print("\n"*number)
def fill_out(title): return("_"*(92-len(title)))
from tkinter import *

vert=6
hor=10

grid=[
[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],
[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[2,12],[2,13],
[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],[3,13],
[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],[4,13],
[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[5,13],
[6,5],[6,6],[6,7],[6,8],[6,9],[6,10],[6,11],[6,12],[6,13],
[7,5],[7,6],[7,7],[7,8],[7,9],[7,10],[7,11],[7,12],[7,13],
[8,5],[8,6],[8,7],[8,8],[8,9],[8,10],[8,11],[8,12],[8,13],
[9,5],[9,6],[9,7],[9,8],[9,9],[9,10],[9,11],[9,12],[9,13]]

translate = [
'X','X','X','X','X',' ',' ',' ',' ',
'X',' ',' ',' ','X',' ',' ',' ',' ',
'X',' ','O',' ','X',' ','X','X','X',
'X',' ','O',' ','X',' ','X','E','X',
'X','X','X',' ','X','X','X','E','X',
' ','X','X',' ',' ','S',' ','E','X',
' ','X',' ','O',' ','X',' ',' ','X',
' ','X',' ',' ',' ','X','X','X','X',
' ','X','X','X','X','X',' ',' ',' ']

endgame_count = translate.count('E')


class Map(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.mainFont = ("Times New Roman", "12", "bold")
        self.title("Map of Maze")
        self.selection()

    def selection(self):
        Label(self, text = "Sokoban Board", font = self.mainFont).grid(row = 0,
            column = 5, columnspan =9)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=6,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=7,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=9,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=1,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=1,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=1,column=12,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=1,column=13,columnspan=1)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=2,column=5,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=6,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=2,column=9,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=12,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=13,columnspan=1)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=5,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=3,column=6,columnspan=1)
        Label(self,text="O",  font= self.mainFont).grid(row=3,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=3,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=9,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=3,column=10,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=11,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=13,columnspan=1)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=4,column=5,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=4,column=6,columnspan=1)
        Label(self,text="O",  font= self.mainFont).grid(row=4,column=7,columnspan=1)
        Label(self,text="",  font= self.mainFont).grid(row=4,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=4,column=9,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=4,column=10,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=4,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont, bg='green').grid(row=4,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=4,column=13,columnspan=1)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=6,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=5,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=9,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=10,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont, bg='green').grid(row=5,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=13,columnspan=1)

        Label(self,text=" ",  font= self.mainFont).grid(row=6,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=6,column=6,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=6,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=6,column=8,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=6,column=9,columnspan=1)
        Label(self,text="*",  font= self.mainFont).grid(row=6,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=6,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont, bg='green').grid(row=6,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=6,column=13,columnspan=1)

        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=7,column=6,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=7,columnspan=1)
        Label(self,text="O",  font= self.mainFont).grid(row=7,column=8,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=9,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=7,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=7,column=13,columnspan=1)

        Label(self,text=" ",  font= self.mainFont).grid(row=8,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=6,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=8,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=8,column=8,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=8,column=9,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=10,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=11,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=13,columnspan=1)

        Label(self,text=" ",  font= self.mainFont).grid(row=9,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=6,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=7,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=9,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=9,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=9,column=12,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=9,column=13,columnspan=1)



        self.button2 = Button(self, text= "left")
        self.button2.grid(row=2, column =0, columnspan = 2)
        self.button2["command"] = self.left

        self.button3 = Button(self, text= "right")
        self.button3.grid(row=2, column =2, columnspan = 2)
        self.button3["command"] = self.right

        self.button4 = Button(self, text= "up")
        self.button4.grid(row=1, column =1, columnspan = 2)
        self.button4["command"] = self.up

        self.button5 = Button(self, text= "down")
        self.button5.grid(row=3, column =1, columnspan = 2)
        self.button5["command"] = self.down
        
        self.button6 = Button(self, text= "What is Sokoban?")
        self.button6.grid(row=7, column =0, columnspan = 4)
        self.button6["command"] = self.what
        
        self.button7 = Button(self, text= "Reset Board")
        self.button7.grid(row=9, column=0, columnspan = 4)
        self.button7["command"] = self.reset


    def left(self):
        new_row=vert
        new_col=hor-1
        ext_row=vert
        ext_col=hor-2
        print("The coordinates to the left of your position are ({},{}).".format(new_row,new_col))
        lft_obj=retrieve_input(new_row,new_col)
        ext_lft_obj=retrieve_input(ext_row,ext_col)
        intct=det_intct(lft_obj,ext_lft_obj)
        if intct==1:
            self.moveblock(new_row,new_col,ext_row,ext_col)
            print("You move the block left by one space.")
            self.wincheck()
        elif intct==3:
            self.shift("left")
            print("You move to the left by one space.")
        elif intct==0 or intct==2:
            print("You cannot move this direction!")
        else:
            print("This is going to be a problem...")

    def right(self):
        new_row=vert
        new_col=hor+1
        ext_row=vert
        ext_col=hor+2
        print("The coordinates to the right of your position are ({},{}).".format(new_row,new_col))
        rgt_obj=retrieve_input(new_row,new_col)
        ext_rgt_obj=retrieve_input(ext_row,ext_col)
        intct=det_intct(rgt_obj,ext_rgt_obj)
        if intct==1:
            self.moveblock(new_row,new_col,ext_row,ext_col)
            print("You move the block right by one space.")
            self.wincheck()
        elif intct==3:
            self.shift("right")
            print("You move to the right by one space.")
        else:
            print("You cannot move this direction!")

    def up(self):
        new_row=vert-1
        new_col=hor
        ext_row=vert-2
        ext_col=hor
        print("The coordinates above your position are ({},{}).".format(new_row,new_col))
        up_obj=retrieve_input(new_row,new_col)
        ext_up_obj=retrieve_input(ext_row,ext_col)
        intct=det_intct(up_obj,ext_up_obj)
        if intct==1:
            self.moveblock(new_row,new_col,ext_row,ext_col)
            print("You move the block up by one space.")
            self.wincheck()
        elif intct==3:
            self.shift("up")
            print("You move up by one space.")
        else:
            print("You cannot move this direction!")

    def down(self):
        new_row=vert+1
        new_col=hor
        ext_row=vert+2
        ext_col=hor
        print("The coordinates below your position are ({},{}).".format(new_row,new_col))
        down_obj=retrieve_input(new_row,new_col)
        ext_down_obj=retrieve_input(ext_row,ext_col)
        intct=det_intct(down_obj,ext_down_obj)
        if intct==1:
            self.moveblock(new_row,new_col,ext_row,ext_col)
            print("You move the block down by one space.")
            self.wincheck()
        elif intct==3:
            self.shift("down")
            print("You move down by one space.")
        else:
            print("You cannot move this direction!")
            
    def what(self):
        welcome = "____/***WELCOME TO SOKOBAN!***\____"
        space()
        print(welcome,fill_out(welcome),sep="")
        print("Sokoban is a game played on a grid. Your goal is to move the various blocks into a specific\
 location on the grid. For this program, the blocks are implemented as circles, the walls are indicated by\
 black filled-in squares, and the location the blocks are intended to be moved to is indicated by green\
 filled-in squares. The player can freely move wherever there are no obstructions, into the green squares, or\
 into a single block. Movement into a block against a wall or up against another block is not permitted.")
        space()
        
        
    def reset(self):
        #We set "translate" back to the original state and update the maze display in the GUI
        global translate
        global vert
        global hor
        translate = [
        'X','X','X','X','X',' ',' ',' ',' ',
        'X',' ',' ',' ','X',' ',' ',' ',' ',
        'X',' ','O',' ','X',' ','X','X','X',
        'X',' ','O',' ','X',' ','X','E','X',
        'X','X','X',' ','X','X','X','E','X',
        ' ','X','X',' ',' ','S',' ','E','X',
        ' ','X',' ','O',' ','X',' ',' ','X',
        ' ','X',' ',' ',' ','X','X','X','X',
        ' ','X','X','X','X','X',' ',' ',' ']
        vert = 6
        hor = 10

        
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=6,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=7,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=1,column=9,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=1,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=1,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=1,column=12,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=1,column=13,columnspan=1)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=2,column=5,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=6,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=2,column=9,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=12,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=2,column=13,columnspan=1)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=5,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=3,column=6,columnspan=1)
        Label(self,text="O",  font= self.mainFont).grid(row=3,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=3,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=9,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=3,column=10,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=11,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=3,column=13,columnspan=1)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=4,column=5,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=4,column=6,columnspan=1)
        Label(self,text="O",  font= self.mainFont).grid(row=4,column=7,columnspan=1)
        Label(self,text="",  font= self.mainFont).grid(row=4,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=4,column=9,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=4,column=10,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=4,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont, bg='green').grid(row=4,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=4,column=13,columnspan=1)

        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=6,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=5,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=9,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=10,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont, bg='green').grid(row=5,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=5,column=13,columnspan=1)

        Label(self,text=" ",  font= self.mainFont).grid(row=6,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=6,column=6,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=6,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=6,column=8,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=6,column=9,columnspan=1)
        Label(self,text="*",  font= self.mainFont).grid(row=6,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=6,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont, bg='green').grid(row=6,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=6,column=13,columnspan=1)

        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=7,column=6,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=7,columnspan=1)
        Label(self,text="O",  font= self.mainFont).grid(row=7,column=8,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=9,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=7,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=7,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=7,column=13,columnspan=1)

        Label(self,text=" ",  font= self.mainFont).grid(row=8,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=6,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=8,column=7,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=8,column=8,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=8,column=9,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=10,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=11,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=12,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=8,column=13,columnspan=1)

        Label(self,text=" ",  font= self.mainFont).grid(row=9,column=5,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=6,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=7,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=8,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=9,columnspan=1)
        Label(self,text="X",  font= self.mainFont, bg='black').grid(row=9,column=10,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=9,column=11,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=9,column=12,columnspan=1)
        Label(self,text=" ",  font= self.mainFont).grid(row=9,column=13,columnspan=1)


    def moveblock(self,p,q,r,s):
        global translate
        down_place=retrieve_place(p,q)
        ext_down_place=retrieve_place(r,s)
        down_val=retrieve_input(p,q)
        ext_down_val=retrieve_input(r,s)
        if down_val=="&" and ext_down_val=="E":
            translate[down_place]="E"
            translate[ext_down_place]="&"
            Label(self,text=" ",  font= self.mainFont,bg='green').grid(row=p,column=q,columnspan=1)
            Label(self,text="O",  font= self.mainFont,bg='green').grid(row=r,column=s,columnspan=1)
        elif down_val=="&" and ext_down_val==" ":
            translate[down_place]="E"
            translate[ext_down_place]="O"
            Label(self,text=" ",  font= self.mainFont,bg='green').grid(row=p,column=q,columnspan=1)
            Label(self,text="O",  font= self.mainFont).grid(row=r,column=s,columnspan=1)
        elif down_val=="O" and ext_down_val=="E":
            translate[down_place]=" "
            translate[ext_down_place]="&"
            Label(self,text=" ",  font= self.mainFont).grid(row=p,column=q,columnspan=1)
            Label(self,text="O",  font= self.mainFont,bg='green').grid(row=r,column=s,columnspan=1)
        elif down_val=="O" and ext_down_val==" ":
            translate[down_place]=" "
            translate[ext_down_place]="O"
            Label(self,text=" ",  font= self.mainFont).grid(row=p,column=q,columnspan=1)
            Label(self,text="O",  font= self.mainFont).grid(row=r,column=s,columnspan=1)
        else:
            "This configuration seems to be problematic."

    def shift(self,dir):
        global translate
        global vert
        global hor
        if dir=="left":
            newvert=vert
            newhor=hor-1
        elif dir=="right":
            newvert=vert
            newhor=hor+1
        elif dir=="up":
            newvert=vert-1
            newhor=hor
        elif dir=="down":
            newvert=vert+1
            newhor=hor
        else:
            print("ER=ROR")
        current_loc=retrieve_input(vert,hor)
        current_place=retrieve_place(vert,hor)
        new_loc=retrieve_input(newvert,newhor)
        new_place=retrieve_place(newvert,newhor)
#        print(current_loc)
#        print(new_loc)
        if current_loc=="e" and new_loc=="E":
            translate[current_place]="E"
            translate[new_place]="e"
            Label(self,text=" ",  font= self.mainFont,bg='green').grid(row=vert,column=hor,columnspan=1)
            Label(self,text="*",  font= self.mainFont,bg='green').grid(row=newvert,column=newhor,columnspan=1)
            vert=newvert
            hor=newhor
            print("Your current location is ({},{}).".format(vert,hor))
        elif current_loc=="e" and new_loc==" ":
            translate[current_place]="E"
            translate[new_place]="L"
            Label(self,text=" ",  font= self.mainFont,bg='green').grid(row=vert,column=hor,columnspan=1)
            Label(self,text="*",  font= self.mainFont).grid(row=newvert,column=newhor,columnspan=1)
            vert=newvert
            hor=newhor
            print("Your current location is ({},{}).".format(vert,hor))
        elif current_loc=="L" and new_loc=="E":
            translate[current_place]=" "
            translate[new_place]="e"
            Label(self,text=" ",  font= self.mainFont).grid(row=vert,column=hor,columnspan=1)
            Label(self,text="*",  font= self.mainFont, bg='green').grid(row=newvert,column=newhor,columnspan=1)
            vert=newvert
            hor=newhor
            print("Your current location is ({},{}).".format(vert,hor))
        elif current_loc=="L" and new_loc==" ":
            translate[current_place]=" "
            translate[new_place]="L"
            Label(self,text=" ",  font= self.mainFont).grid(row=vert,column=hor,columnspan=1)
            Label(self,text="*",  font= self.mainFont).grid(row=newvert,column=newhor,columnspan=1)
            vert=newvert
            hor=newhor
            print("Your current location is ({},{}).".format(vert,hor))
        elif current_loc=="S" and new_loc=="E":
            translate[current_place]=" "
            translate[new_place]="e"
            Label(self,text=" ",  font= self.mainFont).grid(row=vert,column=hor,columnspan=1)
            Label(self,text="*",  font= self.mainFont, bg='green').grid(row=newvert,column=newhor,columnspan=1)
            vert=newvert
            hor=newhor
            print("Your current location is ({},{}).".format(vert,hor))
        elif current_loc=="S" and new_loc==" ":
            translate[current_place]=" "
            translate[new_place]="L"
            Label(self,text=" ",  font= self.mainFont).grid(row=vert,column=hor,columnspan=1)
            Label(self,text="*",  font= self.mainFont).grid(row=newvert,column=newhor,columnspan=1)
            vert=newvert
            hor=newhor
            print("Your current location is ({},{}).".format(vert,hor))
        else:
            print("Something is not right here...")



    def wincheck(self):
    #wincheck() analyzes each square in the grid, looking for '&' symbols, which indicate a block in a
    #win-square. Since there are three win-squares in this translate iteration, if three '&'s are detected in
    #grid, the level has been completed.
        wincount = translate.count('&')
        if wincount==endgame_count:
            space()
            print("You have completed the level!!")
            proceed = False
            while proceed == False:
                repeat = input("Would you like to repeat the level or quit? Type 'Repeat' or 'Quit':")
                if repeat == 'Repeat':
                    proceed = True
                    self.reset()
                elif repeat == 'Quit':
                    proceed = True
                    self.destroy()
                else:
                    print("Invalid input. You must indicate 'Repeat' to restart the level or 'Quit' to quit.")




def retrieve_input(x,y):
    #This function returns the type of object that is located at grid position (x,y)
    global translate
    max=len(translate)
    place=0
    for i in range (0,max):
        if grid[i]==[x,y]:
            place=i
    value=translate[place]
    return value


def retrieve_place(x,y):
    #This function takes 2-list coordinates of position on the grid and returns the location this value
    #occupies within "grid"
    global translate
    max=len(translate)
    place=0
    for i in range (0,max):
        if grid[i]==[x,y]:
            place=i
    return place

def det_intct(inpt,ext_inpt):
    global translate
    if inpt=="X":
        return 0
    elif inpt=="O" or inpt=="&":
        if ext_inpt=="X" or ext_inpt=="O" or ext_inpt=="&":
            return 2
        else:
            return 1
    else:
        return 3
    #The above definition will return a value from 0 to 3 where 0 means "can't move due to wall",
    #where 1 means "action moves block direction indicated", where 2 means "can't move due to
    #block against wall", and where 3 means "action moves player direction indicated".

def main():
    map=Map()
    print("Your location is indicated by '*'.\n")
    map.mainloop()


if __name__ == '__main__':
    #By default, '__name__' is set to equal '__main__', meaning that this statement is just to cause the
    #function main() to be executed, which sequentially then prompts the program to run.
    main()

