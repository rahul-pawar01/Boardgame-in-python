import time
import threading
import random
from tkinter import *
previousButton=NONE
def topDesign(frame):
    def randomColorChange():
        global previousButton
        frame=bottomFrame
        rowCount=varRow.get()
        columnCount=varColumn.get()
        while(True):
            r=random.choice(range(rowCount))
            c=random.choice(range(columnCount))


            newbtn=frame.grid_slaves(row=r,column=c)[0]
            previousButton['bg']='white'
            newbtn['bg']='red'
            previousButton=newbtn
            time.sleep(1)
    def createGrid_Click():
        global previousButton
        createGrid(bottomFrame, varRow.get(), varColumn.get())
        previousButton=bottomFrame.grid_slaves(row=0,column=0)[0]
        th1=threading.Thread(target=randomColorChange)
        th1.start()
        #randomColorChange(bottomFrame, varRow.get(), varColumn.get())
    def createGrid(frame, rowCount, columnCount):
        def btn_Click(e):
            btn1=e.widget
            if(btn1['bg']=='red'):
                varClicked.set(varClicked.get()+1)
                #write code for clicked

            else:
                varMissed.set(varMissed.get()+1)
                #write code for missed

            #print(btn1['bg'])

        for r in range(rowCount):
            for c in range(columnCount):
                btn=Button(master=frame,text=str(r)+"_"+str(c), width=4,height=2)
                btn.bind("<Button-1>",btn_Click)
                btn.grid(row=r, column=c)

    lblRow = Label(master=frame,text='Row')
    lblRow.grid(row=0,column=0)
    varRow = IntVar()
    txtRow = Entry(master=frame,textvariable=varRow,width=2)
    txtRow.grid(row=0,column=1)
    varRow.set(6)

    lblColumn=Label(master=frame,text='Column')
    lblColumn.grid(row=0,column=2)
    varColumn=IntVar()
    txtColumn=Entry(master=frame,textvariable=varRow,width=2)
    txtColumn.grid(row=0,column=3)
    varColumn.set(6)

    lblClicked = Label(master=frame, text='Clicked')
    lblClicked.grid(row=1, column=1)
    varClicked = IntVar()
    txtClicked = Entry(master=frame, textvariable=varClicked, width=2)
    txtClicked.grid(row=1, column=2)

    lblMissed = Label(master=frame, text='Missed')
    lblMissed.grid(row=1, column=3)
    varMissed = IntVar()
    txtMissed = Entry(master=frame, textvariable=varMissed, width=2)
    txtMissed.grid(row=1, column=4)

    btnCreateGrid=Button(master=frame,text="Create Grid",command=createGrid_Click)
    btnCreateGrid.grid(row=0,column=4)


root=Tk()
topFrame=Frame(master=root,height=50,bg='red')
topFrame.pack(fill="x")

middleFrame=Frame(master=root,height=50,bg='yellow')
middleFrame.pack(fill="x")

bottomFrame=Frame(master=root,height=50,bg='blue')
bottomFrame.pack(side='bottom',fill="x")

topDesign(topFrame)
root.mainloop()