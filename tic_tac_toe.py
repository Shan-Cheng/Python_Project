# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:     Shan
# -----------------------------------------------------------------------------
'''
TicTacToe game,player try to marked 3 grid in horizon,vertical or diagonal
'''
import tkinter
import random
import re


class Game(object):
    '''
    A TicTacToe game, user play with computer

    :argument
    parent(object): a root window

    :attributes:
    parent(object) : a room window
    clicked (list) : represent a area that had been clicked
    rectangle_id(list) : list of id of rectangle in widget
    re_button (button) : to restart the game
    canvas(widget) : canvas for 3*3 grid
    result_label(label) : show the game result
    '''
    point = 100

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent
        # Add your instance variables  if needed here
        # Create the restart button widget
        # Create a canvas widget
        # Create a label widget for the win/lose message
        self.clicked = []
        self.rectangle_id = []

        self.re_button = tkinter.Button(self.parent,
                                        text="Restart",
                                        command=self.restart)
        self.re_button.grid()

        self.canvas = tkinter.Canvas(self.parent,
                                     width=self.point * 3,
                                     height=self.point * 3)
        self.canvas.grid()
        self.result_label = tkinter.Label(self.parent,
                                          text="", )
        self.result_label.grid()

        self.initialize_game()


    def initialize_game(self):
        """
        Initializations the game at the beginning and after restarts

        create rectangle on canvas , and bind it to play function
        """
        self.clicked = ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']
        self.rectangle_id = []
        p = 1
        for col in range(3):
            for row in range(3):
                id = self.canvas.create_rectangle(
                    self.point * col,
                    self.point * row,
                    self.point * (col + 1),
                    self.point * (row + 1),
                    fill='white')
                p += 1
                self.rectangle_id.append(id)

        for j in self.rectangle_id:
            self.canvas.tag_bind(j, "<Button-1>", self.play)


    def restart(self):
        """
        This method is invoked when the user clicks on the RESTART button.

        it will delete all items on canvas and invoke initialize_game to
        recreate rectangle, and also reset the result_label
        """
        self.canvas.delete("all")
        self.result_label.config(text='')
        self.initialize_game()

    def play(self, event):

        """
        This method is invoked when the user clicks on a square.

        when click, the rectangle show blue, and computer chose a random
        available rectangle to show red.
        If the square is already taken, do nothing.After user click and
        computer response , check it anyone wins.

        :param
        event : the click item from canvas

        """
        id = event.widget.find_withtag("current")[0]
        position = self.rectangle_id.index(id)
        available_grid = []
        game_on = True

        while game_on:

            if self.clicked[position] == 'F':
                self.canvas.itemconfig(id, fill='blue')
                self.clicked[position] = 'T'
                self.check_game()
            else:
                return None

            for z in range(0, 9):  # find the grid not clicked yet
                if self.clicked[z] == 'F':
                    available_grid.append(z)

            if len(available_grid) != 0:
                random_move = random.choice(available_grid)
                computer_move = self.rectangle_id[random_move]
                self.canvas.itemconfig(computer_move, fill='red')
                self.clicked[random_move] = 'X'

            elif len(available_grid) == 0:
                game_on = self.check_game()
                if game_on:
                    self.result_label.config(text='It is tie !')

            self.check_game()


    def check_game(self):
        """
            Check if the game is won or lost

            :return boolean
            """
        win = ['0\d*1\d*2', '3\d*4\d*5', '6\d*7\d*8', '0\d*3\d*6',
               '1\d*4\d*7', '2\d*5\d*8', '0\d*4\d*8', '2\d*4\d*6']


        t_list = []
        x_list = []
        for i in range(0, 9):
            if self.clicked[i] == 'T':
                char = str(i)
                t_list.append(char)
            elif self.clicked[i] == 'X':
                char = str(i)
                x_list.append(char)

        you_win = ''.join(t_list)
        i_win = ''.join(x_list)


        for j in win:

            if re.match(j,you_win):
                self.result_label.config(text='You Win!')
                self.stop_bind()


            elif re.match(j,i_win):
                self.result_label.config(text='I Win!')
                self.stop_bind()

        else:
            return True


    def stop_bind(self):
        """
            To stop binding rectangle with play function

            """
        for j in range(0, 9):
            id = self.rectangle_id[j]
            self.canvas.tag_unbind(id, "<Button-1>")


def main():
    # Instantiate a root window
    # Instantiate a Game object
    # Enter the main event loop

    root = tkinter.Tk()
    game_start = Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()