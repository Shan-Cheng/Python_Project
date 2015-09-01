# -----------------------------------------------------------------------------
# Name:        robot
# Purpose:    assignment 6
# class definition for a Robot in a maze class
#
# Author: Shan
# Date: May 15 2015
# -----------------------------------------------------------------------------

"""
Module to describe and control Robot objects in a given maze.
"""
import tkinter


class Robot(object):
    """
    A Robot moves around in a maze

    Argument:
     name(string): robot's name
     color: robot's color
     row (int) : position in the x axis of maze
     column(int) :position in the x axis of maze

    Attributes:
     name(string): robot's name
     color: robot's color
     row (int) : position in the x axis of maze
     column(int) :position in the x axis of maze
     maze (array) : maze array
     unit_size (int) :class variable used by the show method
     maze_size (int) : show the maze size
     full(int) : initialize the battery levers

    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full battery
    # A robot with a fully charged battery can take up to 20 steps
    full = 20

    def __init__(self, name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.battery = self.full


    def __str__(self):
        return self.name + " is " + self.color + " robot who get lost in maze"

    def __gt__(self, other):
        if self.battery > other.battery:
            return True
        else:
            return False

    def recharge(self, gas):
        """
        recharge robot's battery

        :parameter : gas => how much gas we refill
        :return : recharged battery

        """
        self.battery = self.battery + gas
        return self

    def one_step_forward(self):
        """
        move robot one step forward
        :return : new position of robot
        """
        if self.row >= self.maze_size:
            self.row
        elif self.maze[self.row+1][self.column] == False:
            self.row
        elif self.battery == 0:
            self.row
            print("no gas")
        else:
            self.row += 1
            self.battery -=1


    def one_step_back(self):
        """
        move robot one step back
        :return : new position of robot
        """
        if self.row <= 0:
            self.row
        elif self.maze[self.row-1][self.column] == False:
            self.row
        elif self.battery == 0:
            self.row
            print("no gas")
        else:
            self.row -= 1
            self.battery -=1

    def one_step_right(self):
        """
        move robot one step right
        :return : new position
        """
        if self.column >= len(self.maze[self.row]):
            self.row
        elif self.maze[self.row][self.column+1] == False:
            self.row
        elif self.battery == 0:
            self.row
            print("no gas")
        else:
            self.column += 1
            self.battery -=1

    def one_step_left(self):
        """
        move robot one step left
        :return : new position
        """
        if self.column <= 0:
            self.row
        elif self.maze[self.row][self.column-1] == False:
            self.row
        elif self.battery == 0:
            self.row
            print("no gas")
        else:
            self.column -= 1
            self.battery -=1


    def forward(self, steps):
        """
        move robot forward
        :parameter : input how many steps go forward
        :return : new position of robot
        """
        for step in range(0,steps):
            self.one_step_forward()



    def backward(self, steps):
        """
        move robot backward
        :parameter : input how many steps go backward
        :return : new position of robot
        """
        for step in range(0,steps):
            self.one_step_back()

    def right(self, steps):
        """
        move robot to right
        :parameter : input how many steps go right
        :return : new position of robot
        """
        for step in range(0,steps):
            self.one_step_right()

    def left(self, steps):
        """
        move robot to left
        :parameter : input how many steps go left
        :return : new position of robot
        """
        for step in range(0,steps):
            self.one_step_left()


    # The method below has been written for you
    # You can use it when testing your class

    def show(self):
        """
            Draw a graphical representation of the robot in the maze.

            The robot's position and color are shown.
            The color is assumed to be one of the colors recognized by tkinter
            (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
            If the robot's battery is empty, the robot is shown in a
            horizontal position. Otherwise the robot is shown in an upright
            position.
            The obstacles in the maze are shown in red.

            Parameter: None
            Return: None
            """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else:  # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()