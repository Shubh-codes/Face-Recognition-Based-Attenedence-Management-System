
from tkinter import *
from tkinter import ttk
from turtle import circle, update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class  Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("2560x1440+0+0")
        self.root.title("Train Your Face")




        #bg image
        img3 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\img4.jpg')
        img3 = img3.resize((2560,1440),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root,image = self.photoimg3)
        bg_image.place(x = 0 , y = 45,width = 2560,height = 1440)

        #title
        title_lable = Label(self.root,text="Train Your Face for Recognition  ",font=("times new roman",35,"bold"),bg = "red",fg = "white")
        title_lable.place(x = 0 , y = 0, width = 2560,height= 45)


        #button
        train_button = Button(self.root,text="Train Your Face for attendence",command=self.train_classifier, font=("times new roman",40,"bold"),bg='navy Blue',fg='white',width=50)
        train_button.place(x = 0 ,y = 700,width=2549,height=50)



    def train_classifier(self):
        data_dir = ('data')
        path  = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        
        for image in path:
            img = Image.open(image).convert('L') # for gray scaling the img
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training Your Face',imageNp)
            cv2.waitKey(1) == 13
        
        ids = np.array(ids)


        # ------------------------------------- training the classifier--------------------------

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo('Results','Your face has been trained...',parent= self.root)









if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()
