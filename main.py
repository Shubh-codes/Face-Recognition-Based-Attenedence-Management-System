from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recongizer import Face_Recognizer


class Face_Rocognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("2560x1440+0+0")
        self.root.title("Face Recognizer")

        # first img
        '''img = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\img1.jpg')
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lable = Label(self.root,image = self.photoimg)
        f_lable.place(x = 0 , y = 0,width = 500,height = 130)

        # second img

        img1 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\img3.jpg')
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lable = Label(self.root,image = self.photoimg1)
        f_lable.place(x = 500 , y = 0,width = 500,height = 130)

        # third image

        img2 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\img2.jpeg')
        img = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lable = Label(self.root,image = self.photoimg2)
        f_lable.place(x = 1000  , y = 0,width = 700,height = 130)'''
    

        #background image


        img3 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\img4.jpg')
        img3 = img3.resize((2560,1440),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root,image = self.photoimg3)
        bg_image.place(x = 0 , y = 0,width = 2560,height = 1440)

        #title
        title_lable = Label(bg_image,text="Attendance Management System",font=("times new roman",35,"bold"),bg = "red",fg = "white")
        title_lable.place(x = 0 , y = 0, width = 2560,height= 45)

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
        b1 = Button(bg_image,image=self.photoimg7,cursor="hand2")
        b1.place(x = 1800,y = 200,width=400,height=350)

        b1_1 = Button(bg_image,text='4. Check Attendence',cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 1800,y = 520,width=400,height=40)


        #view photos button
        img8 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\photo.jpg')
        img8 = img8.resize((400,350),Image.ANTIALIAS)
        self.photoimg8= ImageTk.PhotoImage(img8)
        b1 = Button(bg_image,command=self.open_images,  image=self.photoimg8,cursor="hand2")
        b1.place(x = 600,y = 800,width=400,height=340)

        b1_1 = Button(bg_image,command=self.open_images, text='View Photos',cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 600,y = 1135,width=400,height=40)

        # contact me
        img9 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\contact.jpg')
        img9= img9.resize((400,350),Image.ANTIALIAS)
        self.photoimg9= ImageTk.PhotoImage(img9)
        b1 = Button(bg_image,image=self.photoimg9,cursor="hand2")
        b1.place(x = 1100,y = 800,width=400,height=350)

        b1_1 = Button(bg_image,text='Contact Me',cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 1100,y = 1145,width=400,height=40)


        #exit button

        img10 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\exit.jpg')
        img10 = img10.resize((400,350),Image.ANTIALIAS)
        self.photoimg10= ImageTk.PhotoImage(img10)
        b1 = Button(bg_image,image=self.photoimg10,cursor="hand2")
        b1.place(x = 1600,y = 800,width=400,height=340)

        b1_1 = Button(bg_image,text='Exit',cursor="hand2",font=("times new roman",30,"bold"),bg = "dark blue",fg = "white")
        b1_1.place(x = 1600,y = 1135,width=400,height=40)
    

    

        # ----------------------Functions ------------------------------------
        
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










if __name__ == '__main__':
    root = Tk()
    obj = Face_Rocognition_System(root)
    root.mainloop()
