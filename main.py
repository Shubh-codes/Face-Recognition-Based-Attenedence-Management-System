import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recongizer import Face_Recognizer
from attendence import Attendence
import time
from time import strftime

class Face_Rocognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("2560x1440+0+0")
        self.root.title("Attendance Management Application")

 
        #background image
        img3 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\img4.jpg')
        img3 = img3.resize((2560,1440),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root,image = self.photoimg3)
        bg_image.place(x = 0 , y = 0,width = 2560,height = 1440)

        #title

        title_lable = Label(bg_image,text="Attendance Management System",font=("times new roman",35,"bold"),bg = "red",fg = "white")
        title_lable.place(x = 0 , y = 0, width = 2560,height= 45)

        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_lable,font = ("times new roman",30,"bold"),background = "red",foreground='white')
        lbl.place(x=40,y=0,width=220,height=40)
        time()



        student_details = self.student_details
        
        #student button
        img4 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\student.jpg')
        img4 = img4.resize((400,350),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_image,command=self.student_details, image=self.photoimg4,cursor="hand2")
        b1.place(x = 300,y = 200,width=400,height=350)

        b1_1 = Button(bg_image,text='1. Student Details',command=self.student_details, cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 300,y = 520,width=400,height=40)

    
        # train face button

        img5 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\train.jpg')
        img5 = img5.resize((400,350),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_image,command=self.train ,image=self.photoimg5,cursor="hand2")
        b1.place(x = 800,y = 200,width=400,height=350)

        b1_1 = Button(bg_image,text='2. Train Your Face',command=self.train,cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 800,y = 520,width=400,height=40)


        # mark face attendence detection button

        img6 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\detect.jpg')
        img6 = img6.resize((400,350),Image.ANTIALIAS)
        self.photoimg6= ImageTk.PhotoImage(img6)
        b1 = Button(bg_image,command= self.Face, image=self.photoimg6,cursor="hand2")
        b1.place(x = 1300,y = 200,width=400,height=350)

        b1_1 = Button(bg_image,text='3. Mark Attendence',command= self.Face,cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 1300,y = 520,width=400,height=40)

        # attendence button

        img7 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\attendence.jpg')
        img7 = img7.resize((400,350),Image.ANTIALIAS)
        self.photoimg7= ImageTk.PhotoImage(img7)
        b1 = Button(bg_image,command=self.attendence_data, image=self.photoimg7,cursor="hand2")
        b1.place(x = 1800,y = 200,width=400,height=350)

        b1_1 = Button(bg_image,text='4. Check Attendence',command=self.attendence_data,cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 1800,y = 520,width=400,height=40)


        #view photos button
        img8 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\photo.jpg')
        img8 = img8.resize((400,350),Image.ANTIALIAS)
        self.photoimg8= ImageTk.PhotoImage(img8)
        b1 = Button(bg_image,command=self.open_images,  image=self.photoimg8,cursor="hand2")
        b1.place(x = 800,y = 800,width=400,height=340)

        b1_1 = Button(bg_image,command=self.open_images, text='View Image Dataset',cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 800,y = 1135,width=400,height=40)




        #exit button

        img10 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\exit.jpg')
        img10 = img10.resize((400,350),Image.ANTIALIAS)
        self.photoimg10= ImageTk.PhotoImage(img10)
        b1 = Button(bg_image,image=self.photoimg10,cursor="hand2",command=self.iexit)
        b1.place(x = 1300,y = 800,width=400,height=340)

        b1_1 = Button(bg_image,text='Exit',command=self.iexit,cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 1300,y = 1135,width=400,height=40)



    

    

        # ----------------------Functions ------------------------------------

    def iexit(self):
        self.iexit = askyesno("Are you sure","Do You Want to Exit this application?",parent= self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return




        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def open_images(self):
        os.startfile('data')

    def train(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    
    def Face(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognizer(self.new_window)

    
    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)










if __name__ == '__main__':
    root = Tk()
    obj = Face_Rocognition_System(root)
    root.mainloop()
