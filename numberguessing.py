import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def update_button_state():
    if name.get():
        start.config(state="normal")
    else:
        start.config(state="disabled")


def startgame():
    global guess_entry, NUM, attempts_label, result, name_entry
    NUM = random.randint(1, 100)
    name_entry = name.get()
    widgets = root.winfo_children()
    for widget in widgets:
        widget.destroy()
    gamelabel = ttk.Label(root, font=data_font, text=f"Hi, {name_entry}! Guess a number between 1 and 100.")
    gamelabel.pack()
    line_break = Label(root, text="\n")
    line_break.pack()
    guess_entry = ttk.Entry(root, font=data_font)
    guess_entry.pack()
    line_break = Label(root, text="\n")
    line_break.pack()
    style.configure('Custom.TButton', font=button_font)
    submit_button = ttk.Button(root, text="Guess", command=checkguess, width=18, padding=8, style="Custom.TButton")
    submit_button.pack()
    line_break = Label(root, text="\n")
    line_break.pack()
    attemptleft = ttk.Label(root, font=data_font, text="Attempt number :")
    attemptleft.pack()
    attempts_label = Label(root, text="0", fg="blue", font=data_font)
    attempts_label.pack()
    line_break = Label(root, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    line_break.pack()
    result = Label(root, text="", fg="red", font=data_font)
    result.pack()


def checkguess():
    guess = guess_entry.get()
    guess_entry.delete(0, END)
    try:
        guess = int(guess)
        attempts = int(attempts_label["text"]) + 1
        attempts_label.config(text=str(attempts))

        if guess < NUM:
            result.config(text="Result: Too low!")
        elif guess > NUM:
            result.config(text="Result: Too high!")
        else:
            result.config(text=f"Result: Congratulations, {name_entry}! You guessed the number in {attempts} attempts!",font=subhead_font)
            restart_game()

        if attempts == 10:
            result.config(text=f"Result: Game over! The number was {NUM}.")
            restart_game()

    except ValueError:
        result.config(text="Error, Please enter a valid number.")


def restart_game():
    choice = messagebox.askyesno("Restart", "Do you want to play again?")
    if choice:
        global gamelabel, start, name, entername, rules, ruleheading, heading
        widgets = root.winfo_children()
        for widget in widgets:
            widget.destroy()
        style = ttk.Style()
        heading = Label(root, text='Welcome to Number Guessing Game', font=head_font)
        heading.pack()
        # Adding a line break
        line_break = Label(root, text="\n")
        line_break.pack()
        line_break = Label(root, text="\n")
        line_break.pack()
        ruleheading = Label(root, text='\t\t Rules :', font=subhead_font)
        ruleheading.pack(anchor='w')
        rules = Label(root, text='''
        1. Player has to guess number between 1 to 100.
        2. Player will be given 10 chances to guess the correct number.
        3. For every wrong guess, player will be told that the guessed
            number is too high or too low than the correct number    
        ''', font=data_font, fg="grey", width=50, justify="left")
        rules.pack()
        line_break = Label(root, text="\n")
        line_break.pack()
        line_break = Label(root, text="\n")
        line_break.pack()
        entername = Label(root, text='\t\t Enter your name :', font=subhead_font)
        entername.pack(anchor='w')
        name = ttk.Entry(root, font=data_font, width=50)
        name.pack()
        line_break = Label(root, text="\n")
        line_break.pack()
        style.configure('Custom.TButton', font=button_font)
        start = ttk.Button(root, text="Start Game", style='Custom.TButton', padding=20, state="disabled",command=startgame)
        start.pack()
        name.bind("<KeyRelease>", lambda event: update_button_state())
        gamelabel = ttk.Label(root, font=data_font)

    else:
        root.destroy()


root = Tk()
root.geometry("1000x700")
root.title("Number Guessing Game")
head_font = ("Arial", 30, "bold")
subhead_font = ("Arial", 18, "bold")
button_font = ("Arial", 15)
data_font = ("Arial", 15)
style = ttk.Style()
heading = Label(root, text='Welcome to Number Guessing Game', font=head_font)
heading.pack()
# Adding a line break
line_break = Label(root, text="\n")
line_break.pack()
line_break = Label(root, text="\n")
line_break.pack()
ruleheading = Label(root, text='\t\t Rules :', font=subhead_font)
ruleheading.pack(anchor='w')
rules = Label(root, text='''
1. Player has to guess number between 1 to 100.
2. Player will be given 10 chances to guess the correct number.
3. For every wrong guess, player will be told that the guessed
    number is too high or too low than the correct number    
''', font=data_font, fg="grey", width=50, justify="left")
rules.pack()
line_break = Label(root, text="\n")
line_break.pack()
line_break = Label(root, text="\n")
line_break.pack()
entername = Label(root, text='\t\t Enter your name :', font=subhead_font)
entername.pack(anchor='w')
name = ttk.Entry(root, font=data_font, width=50)
name.pack()
line_break = Label(root, text="\n")
line_break.pack()
style.configure('Custom.TButton', font=button_font)
start = ttk.Button(root, text="Start Game", style='Custom.TButton', padding=20, state="disabled", command=startgame)
start.pack()
name.bind("<KeyRelease>", lambda event: update_button_state())
gamelabel = ttk.Label(root, font=data_font)
# start.config(command=game_start)
if __name__ == '__main__':
    root.mainloop()
