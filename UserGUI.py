from tkinter import *
from ClusterCustomers import ClusterCustomers

gui = Tk()
gui.geometry('500x300')
gui.title("Customer Segmentation")

title = Label(gui, text="Customer Segmentation",width=20,font=("bold", 18))
title.place(x=90,y=50)

userInput = Label(gui, text="Enter Number of Segments :",width=40,font=("bold", 10))
userInput.place(x=00,y= 117)

userEntry = Entry(gui)
userEntry.place(x = 250,y=120)


def callback():
	string_clusters = userEntry.get()
	int_clusters = int(string_clusters)
	a = ClusterCustomers(int_clusters)
	a.clusteringAlgorithm()
	a.modifyCsv()

Button(gui, text='Submit',width=10,bg='green',fg='white', command=callback).place(x=200,y=180)
Button(gui, text="Exit", width=10,bg='green',fg='white',command=gui.destroy).place(x=300,y=180)


gui.mainloop()