from tkinter import * 
import random 
import time 
import tkinter 
import tkinter.messagebox  
colours=['blue','red','yellow','green','red','pink','red','black','green','cyan'] 
global i 
i =0 
global redcount 
redcount = 0 
global greencount 
greencount = 0 
global canvas 
 
def startgame(): 
    global canvas 
    x = startclick() 
    if x ==1 : 
         
        time.sleep(5) 
        tkinter.messagebox.showinfo("ANSWER  ","number of red balls  =" + str (redcount) + " and number of green balls  ="+ str(greencount) ) 
        
        
        
def  startclick():     
    global i 
    global canvas 
    global redcount 
    global greencount 
               
    for i in range (1,26) : 
        m= random.randint(0,10)     
        if  m == 1 or m==4 or m == 6:
            redcount = redcount+1 
        if  m == 3 or m==8 : 
            greencount = greencount+1 
        try:
            a= random.randint(50,250) 
            b= random.randint(50,300) 
            canvas.create_oval(a, b, a+50, b+50, outline="white", fill=colours[m], width=2) 
            canvas.update() 
        except: 
            print() 
    return(1) 
root = Tk() 
root.title("COUNT THE COLOURS") 
root.geometry("800x700+20+20") # dimensions and position 
canvas = Canvas(width = 500,height=500,bg = '#87ceeb') 
canvas.place(x= 20, y =20)   
#===CREATING BUTTON 
w = Label(root, text="Can you count the number of red and green coloured balls ?",bg = "black",fg="yellow") 
w.place (x = 20,y = 500) 
y = Label(root, text="you have 10 seconds to answer ..press the start button to play !!",bg = "white",fg="blue") 
y.place (x = 20,y = 550) 
 
b= Button(root, text="START", bg="#e79700", width=20, height=1, font=("Open Sans", 13, 'bold'), fg='white',command=startgame)  
b.place(x=20, y=600)  
 
root.mainloop() 