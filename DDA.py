## Data Driven Application
#Import Module
from tkinter import *
from PIL import *
from PIL import Image,ImageTk
from tkinter import messagebox
import requests

#create root window
root = Tk() 

root.title('Data Driven Application')
#Create a title in the output

root.geometry('360x640')
#Creates a output Window of size 400x240

root.resizable(0, 0) #Output Window size is fixed

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()

#Create a messagebox showinfo 
def onClick(): 
    instr = "I’m Mecha Senku, here to test your knowledge of science! \n \nPick the category and answer the questions (True/False); \ndo good, and you’ll get 1 billion points! \n \n (Make sure it's True or False, capitalize first letter)"
    messagebox.showinfo("Instructions", instr) 

#Fetching data from the Computers API
def comp_data():
    url = "https://opentdb.com/api.php?amount=10&category=17&type=boolean"
    response = requests.get(url)
    data = response.json()
    return data['results']

#Checking user's answer for the Computers API
def check_comp_answer():
    user_answer = var_comp.get()
    question_data = comp_data()
    correct_answer = question_data[comp_question_no]['correct_answer']
    if user_answer == 'True' and correct_answer == 'True':
        comp_result_label.config(text='Correct!')
    elif user_answer == 'False' and correct_answer == 'False':
        comp_result_label.config(text='Correct!')
    else:
        comp_result_label.config(text='Incorrect!')
    if comp_question_no < len(question_data) - 1:
        next_comp_question()
    else:
        if user_answer == correct_answer:
            comp_result_label.config(text='Correct! That was the last question!')
        else:
            comp_result_label.config(text="Incorrect! Correct answer: {}".format(correct_answer))
        comp_check_button.config(state='disabled')

#Moving on to the next question
def next_comp_question():
    global comp_question_no
    comp_question_no += 1
    if comp_question_no < len(comp_question_data):
        comp_question_label.delete(1.0, END)
        comp_question_label.insert(END, comp_question_data[comp_question_no]['question'])
        var_comp.set('')
    else:
        comp_result_label.config(text='That was the last question!')
        comp_check_button.config(state='disabled')

## Start frame

Startframe = Frame(root, width=360, height=640)

image = Image.open("background/bg1.png") #background img
resize_image = image.resize((360,640))

bg1 = ImageTk.PhotoImage(resize_image)

bg_image_label1 = Label(Startframe, image=bg1)
bg_image_label1.place(x=0,y=0)

startButton = Button(Startframe, text = "START",bg="#CEBAA4" ,fg="#483D20", #start btn
                     font=('Roboto', 18,'bold'), activebackground="#CEBAA4" , bd=0, command=lambda:show_frame(CategoryFrame))
startButton.place(x=130, y=425)

InstrButton = Button(Startframe, text = "Instructions",bg="#F7F3EB" , #Instructions btn
                     fg="#483D20",font=('Roboto', 15,'bold'), activebackground="#F7F3EB", bd=0, command=onClick)
InstrButton.place(x=115, y=507)

Startframe.place(x=-1,y=-1)

## Category Frame 

CategoryFrame = Frame(root, width=360, height=640)

image = Image.open("background/bg2.png")
resize_image = image.resize((360,640))

bg2 = ImageTk.PhotoImage(resize_image)

bg_image_label2 = Label(CategoryFrame, image=bg2)
bg_image_label2.place(x=0,y=0)

category2 = Button(CategoryFrame, text = "Science: Nature",bg="#7A604F" ,fg="#F7F3EB",
                   font=('Roboto', 15,'bold'), activebackground="#7A604F", bd=0, command=lambda:show_frame(TriviaFrame))
category2.place(x=105, y=363)

CategoryFrame.place(x=-1,y=-1)


## Trivia Frame

TriviaFrame = Frame(root, width=360, height=640)

image = Image.open("background/bg3.png")
resize_image = image.resize((360,640))

bg3 = ImageTk.PhotoImage(resize_image)

bg_image_label3 = Label(TriviaFrame, image=bg3)
bg_image_label3.place(x=0,y=0)

#variables for the Science Trivia
var_comp = StringVar()
comp_question_no = 0
comp_question_data = comp_data()

#the questions for trivia
comp_question_label = Text(TriviaFrame, wrap=WORD, width=31, height=12)
comp_question_label.insert(END, comp_question_data[comp_question_no]['question'])
comp_question_label.place(x=61,y=160)

#answer entry for trivia
comp_answer_entry = Entry(TriviaFrame, textvariable=var_comp, width=10, bg="#E4D2BD" ,fg="#7A604F",font=('Roboto', 12,'bold'))
comp_answer_entry.place(x=145,y=372)

#checking for answer button, for trivia
comp_check_button = Button(TriviaFrame, text="SUBMIT", bg="#AE9F68" , fg="#F7F3EB",
                           font=('Roboto', 13,'bold'), activebackground="#AE9F68", bd=0, command=check_comp_answer)
comp_check_button.place(x=82,y=452)

#to move on the next question button, for trivia
comp_next_button = Button(TriviaFrame, text="SKIP", bg="#6B9571" , fg="#F7F3EB",
                          font=('Roboto', 13,'bold'), activebackground="#6B9571", bd=0, command=next_comp_question)
comp_next_button.place(x=232,y=452)

#to output if the user got it right or not
comp_result_label = Label(TriviaFrame, text="", bg="#F7F3EB" , fg="#483D20",font=('Roboto', 11,'bold'))
comp_result_label.place(x=75,y=520)

exit_button = Button(TriviaFrame, text="Exit", bg="#AF5050" ,fg="#F7F3EB",font=('Roboto', 11,'bold'), 
                     activebackground="#AF5050", bd=0, command=root.destroy) 
exit_button.place(x=275,y=23) 

TriviaFrame.place(x=-1,y=-1)

# Set the initial visible frame
show_frame(Startframe)

root.mainloop()