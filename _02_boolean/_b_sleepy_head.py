"""
Use boolean variables to control program logic between two different code
paths.
"""

from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    is_weekday = True
    if(is_weekday == True):
        messagebox.showinfo('', 'It is the weekday')
    passed = True
    if(passed == False):
        messagebox.showinfo('', 'you failed lol')
    elif(passed == True):
        messagebox.showinfo('', "Literally no way you didn't cheat lol")


    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    pass
