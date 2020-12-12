from tkinter import *
from PIL import Image, ImageTk
import random
import sqlite3
root = Tk()
root.title('Rock Paper Scissors Game')
root.resizable(width=False, height=False)
click = True
userWin = 0
compWin = 0
counter = 0
turns = 5

#----------------Image set----------------
rHandPhoto = PhotoImage(file = 'rHand.png')
pHandPhoto = PhotoImage(file = 'pHand.png')
sHandPhoto = PhotoImage(file = 'sHand.png')
rock = Image.open("RockPaperScissorsImages/Rockimg.jpg")
rockImage = ImageTk.PhotoImage(rock)
paper = Image.open("RockPaperScissorsImages/Paperimg.jpg")
paperImage = ImageTk.PhotoImage(paper)
scissors = Image.open("RockPaperScissorsImages/Scissorsimg.jpg")
scissorImage = ImageTk.PhotoImage(scissors)
win = Image.open("RockPaperScissorsImages/YouWin.jpg")
winImage = ImageTk.PhotoImage(win)
lose = Image.open("RockPaperScissorsImages/YouLose.jpg")
loseImage = ImageTk.PhotoImage(lose)
tie = Image.open("RockPaperScissorsImages/YouTie.jpg")
tieImage = ImageTk.PhotoImage(tie)




#------------------------------------------

rHandButton = ''
pHandButton = ''
sHandButton = ''
def changeLight():
    boardb.configure(bg='white')
    board.configure(bg='white')
    light.configure(bg='black', fg='white')
    dark.configure(bg='black', fg='white')
    return
def changeDark():
    boardb.configure(bg='black')
    board.configure(bg='black')
    light.configure(bg='white', fg='black')
    dark.configure(bg='white', fg='black')
    return
def exitall():
    boardb.quit()
    root.quit()

def getLeaderboard():
    global boardb, board, light, dark
    boardb = Tk()
    boardb.title("Leader Board :)")
    boardb.configure(bg = 'white')
    board = Frame(boardb, bg  ='white', padx = 10, pady = 10)
    board.grid(row = 0, column = 0, columnspan = 3)
    conn = sqlite3.connect('LeaderBoard.db')
    c = conn.cursor()
    c.execute("SELECT * FROM LEADERBOARD")
    data = c.fetchall()
    rowno = 2
    Heading = Label(board, text = "Leaderboard", bg = '#dd2c00', fg = 'white', width = 45, pady = 10, padx = 10)
    Heading.config(font=("Times", 20, "bold"))
    Heading.grid(row = 0, column = 0, columnspan = 6, padx = 5, pady  = 5)

    name = Label(board, text="Name", width=15, bg='#0069b3', fg='white', padx=5, pady=5)
    name.grid(row=1, column=0, padx=2, pady=2)
    won = Label(board, text="Games Won", width=15, bg='#a617ff', fg='white', padx=5, pady=5)
    won.grid(row=1, column=1, padx=2, pady=2)
    lost = Label(board, text="Games Lost", width=15, bg='#e01717', fg='white', padx=5, pady=5)
    lost.grid(row=1, column=2, padx=2, pady=2)
    tied = Label(board, text="Games Tied", width=15, bg='#e77c00', fg='white', padx=5, pady=5)
    tied.grid(row=1, column=3, padx=2, pady=2)
    played = Label(board, text="Games Played", width=15, bg='#30b000', fg='white', padx=5, pady=5)
    played.grid(row=1, column=4, padx=2, pady=2)
    rate = Label(board, text="Winning Rate", width=15, bg='#ff1f60', fg='white', padx=5, pady=5)
    rate.grid(row=1, column=5, padx=2, pady=2)

    for record in data:
        name = Label(board, text = record[0], width = 15, bg = '#3d7eac', fg = 'white', padx = 5, pady = 5)
        name.grid(row = rowno, column = 0, padx = 2, pady = 2)
        won = Label(board, text=record[1], width = 15, bg = '#b846ff', fg = 'white', padx = 5, pady = 5)
        won.grid(row = rowno, column=1, padx = 2, pady = 2)
        lost = Label(board, text=record[2], width = 15, bg = '#e33f3f', fg = 'white', padx = 5, pady = 5)
        lost.grid(row = rowno, column=2, padx = 2, pady = 2)
        tied = Label(board, text=record[3], width = 15, bg = '#e38d2a', fg = 'white', padx = 5, pady = 5)
        tied.grid(row = rowno, column=3, padx = 2, pady = 2)
        played = Label(board, text=record[4], width = 15, bg = '#62be40', fg = 'white', padx = 5, pady = 5)
        played.grid(row = rowno, column=4, padx = 2, pady = 2)
        rate = Label(board, text=record[5], width = 15, bg = '#ff5385', fg = 'white', padx = 5, pady = 5)
        rate.grid(row = rowno, column=5, padx = 2, pady = 2)
        rowno += 1

    conn.commit()
    conn.close()
    light = Button(boardb, text = "Light Theme", pady = 7, command = changeLight, bg = 'black', fg = 'white', width = 30)
    light.grid(row = 1, column = 0, pady = (0, 20))
    dark = Button(boardb, text="Dark Theme", pady = 7, command = changeDark, bg = 'black', fg = 'white', width = 30)
    dark.grid(row=1, column=1, pady = (0, 20))
    exit = Button(boardb, text="Exit", pady=7, command=exitall, bg='red', fg='white', width=30)
    exit.grid(row=1, column=2, pady=(0, 20))

getLeaderboard()


def play():
    global rHandButton, pHandButton, sHandButton, userWin, compWin, Scoreboard, rockLabel, paperLabel, scissorLabel, buttonHolder
    rockLabel = Label(root, text = 'Rock', bg = '#238f02', fg = 'white', width = 35, padx = 10, pady =10)
    paperLabel = Label(root, text='Paper', bg='#de9a03', fg='white', width = 35, padx = 10, pady =10)
    scissorLabel = Label(root, text='Scissors', bg='#c20c0c',fg = 'white', width = 35, padx = 10, pady =10)
    rockLabel.grid(row = 0, column = 0, padx = 5, pady  =7)
    paperLabel.grid(row=0, column=1, padx = 5, pady  =5)
    scissorLabel.grid(row=0, column=2, padx = 5, pady  =5)
    rHandButton = Button(root, image=rHandPhoto, command = lambda:youPick('rock'))
    pHandButton = Button(root, image=pHandPhoto, command=lambda: youPick('paper'))
    sHandButton = Button(root, image=sHandPhoto, command=lambda: youPick('scissors'))
    rHandButton.grid(row = 1, column = 0)
    pHandButton.grid(row = 1, column = 1)
    sHandButton.grid(row = 1, column = 2)
    Scoreboard = Label(root, text="SCORE \n\n    USER - "+str(userWin)+"\t\tCOMPUTER - "+str(compWin), bg = 'blue', fg='white', padx = 10, pady = 20)
    Scoreboard.config(font=("Times", 15))
    Scoreboard.grid(row = 2, column = 0, columnspan = 2, sticky = W+E, padx = 10, pady = 10)
    buttonHolder = Frame(root)
    buttonHolder.grid(row = 2, column=2)
    resetButton = Button(buttonHolder, text = 'RESET',fg = 'white', command=lambda: reset_frame(), bg = 'green', width = 30, pady = 10)
    resetButton.pack(pady = 5)
    LeaderBoardBtn = Button(buttonHolder, text = 'Leader Board',fg = 'white', command=lambda: reset_frame(), bg = 'black', width = 30, pady = 10)
    LeaderBoardBtn.pack(pady = 5)

def computerPick():
    choice = random.choice(['rock','paper','scissors'])
    return choice

def youPick(yourChoice):
    global click, userWin, compWin, Scoreboard, counter, turns
    compPick = computerPick()
    if click:
        counter += 1
        if yourChoice == 'rock':
            rHandButton.configure(image = rockImage)
            rockLabel.configure(text = 'Rock')
            if compPick == 'rock':
                pHandButton.configure(image = rockImage)
                sHandButton.configure(image = tieImage)
                paperLabel.configure(text='Rock')
                scissorLabel.configure(text='Tie')
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image = paperImage)
                sHandButton.configure(image = loseImage)
                paperLabel.configure(text='Paper')
                scissorLabel.configure(text='Lose')
                compWin+=1
                click = False
            else :
                pHandButton.configure(image = scissorImage)
                sHandButton.configure(image = winImage)
                paperLabel.configure(text='Scissors')
                scissorLabel.configure(text='Win')
                userWin+=1
                click = False
        elif yourChoice == 'paper':
            rHandButton.configure(image=paperImage)
            rockLabel.configure(text='Paper')
            if compPick == 'rock':
                pHandButton.configure(image=rockImage)
                sHandButton.configure(image=winImage)
                paperLabel.configure(text='Rock')
                scissorLabel.configure(text='Win')
                userWin += 1
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image=paperImage)
                sHandButton.configure(image=tieImage)
                paperLabel.configure(text='Paper')
                scissorLabel.configure(text='Tie')
                click = False
            else:
                pHandButton.configure(image=scissorImage)
                sHandButton.configure(image=loseImage)
                paperLabel.configure(text='Scissors')
                scissorLabel.configure(text='Lose')
                compWin += 1
                click = False
        else:
            rHandButton.configure(image=scissorImage)
            rockLabel.configure(text='Scissors')
            if compPick == 'rock':
                pHandButton.configure(image=rockImage)
                sHandButton.configure(image=loseImage)
                paperLabel.configure(text='Rock')
                scissorLabel.configure(text='Lose')
                compWin += 1
                click = False
            elif compPick == 'paper':
                pHandButton.configure(image=paperImage)
                sHandButton.configure(image=winImage)
                paperLabel.configure(text='Paper')
                scissorLabel.configure(text='Win')
                userWin += 1
                click = False
            else:
                pHandButton.configure(image=scissorImage)
                sHandButton.configure(image=tieImage)
                paperLabel.configure(text='Scissors')
                scissorLabel.configure(text='Tie')
                click = False
    else:
        if yourChoice == 'rock' or yourChoice == 'paper' or yourChoice == 'scissors':
            rHandButton.configure(image = rHandPhoto)
            pHandButton.configure(image = pHandPhoto)
            sHandButton.configure(image = sHandPhoto)
            rockLabel.configure(text='Rock')
            paperLabel.configure(text='Paper')
            scissorLabel.configure(text='Scissors')
            click = True

    Scoreboard = Label(root, text="SCORE \n\n    USER - " + str(userWin) + "\t\tCOMPUTER - " + str(compWin), bg='blue',
                       fg='white', padx=10, pady=20)
    Scoreboard.config(font=("Times", 15))
    Scoreboard.grid(row=2, column=0, columnspan=2, sticky=W + E, padx=10, pady=10)
    if counter == turns:
        message = ''
        if userWin>compWin:
            message = 'You Won!!'
        elif userWin<compWin:
            message = 'You Lose!!'
        else:
            message = 'You Tied!!'
        top = Toplevel()
        top.geometry('300x300')
        confetiImg = PhotoImage(file = "RockPaperScissorsImages/confeti.gif")
        confetiLabel = Label(top, image = confetiImg)
        confetiLabel.image = confetiImg
        confetiLabel.grid(row = 0, column = 0)
        messageFrame = Frame(top)
        messageFrame.grid(row = 0, column=0)
        message = Label(messageFrame, text = message)
        message.config(font=("Times", 30, 'bold'))
        message.pack()
        exitButton = Button(messageFrame, text = "Exit", bg = 'red', fg = 'white', width = 10, padx = 5, pady = 5, command = root.quit)
        exitButton.config(font=("Times", 12))
        exitButton.pack(pady = 5, padx = 5)
        rHandButton.configure(state = "disabled")
        pHandButton.configure(state="disabled")
        sHandButton.configure(state="disabled")

def reset_frame():
    global click
    rHandButton.configure(image=rHandPhoto)
    pHandButton.configure(image=pHandPhoto)
    sHandButton.configure(image=sHandPhoto)
    rockLabel.configure(text='Rock')
    paperLabel.configure(text='Paper')
    scissorLabel.configure(text='Scissor')
    click = True
play()
root.mainloop()
