from tkinter import *
from tkinter import ttk
from xml.sax.handler import feature_external_ges
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import time
import mysql.connector
from time import strftime
from datetime import datetime

class Face_Recognizer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("2560x1440+0+0")
        self.root.title("Face Recognizer")


        #img1
        img3 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\img11.jpg')
        img3 = img3.resize((1200,1350),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root,image = self.photoimg3)
        bg_image.place(x = 0 , y = 0,width = 1200,height = 1300)



        #img2
        img4 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\img10.jpg')
        img4 = img4.resize((1360,1350),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_image1 = Label(self.root,image = self.photoimg4)
        bg_image1.place(x = 1200 , y = 0,width = 1360,height = 1300)


        #title
        title_lable = Label(self.root,text="Mark Attendence",font=("times new roman",35,"bold"),bg = "red",fg = "white")
        title_lable.place(x = 0 , y = 0, width = 2560,height= 45)

        #buttons
        train_button = Button(bg_image1,text="Face Detection",command=self.face_recoger,  font=("times new roman",30,"bold"),bg='navy Blue',fg='white',width=50)
        train_button.place(x = 525 ,y = 1115,width=300,height=50)

        


    #---------------------------- attendence----------------------------
    def mark_attendece(self,name,roll,section):
        with open('Student Attendence.csv',"r+",newline="\n") as f :
            datalist = f.readlines()
            name_list = []
            for data in datalist:
                entry = data.split((","))
                name_list.append(entry[0])
            if ((name not in name_list) and (roll not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dt = now.strftime("%H:%M:%S")
                f.writelines(f"\n{name},{roll},{section},{dt},{d1},Present")




        # -----------------face recognition -----------------------------------

    def face_recoger(self):
        def draw_boundry(img,classifier,scaleFactors,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactors,minNeighbors)

            coord = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,128,0  ),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))


                conn = mysql.connector.connect(host = 'localhost',username='root',password='',database='face_recognition')
                my_cursor = conn.cursor()
                    

                my_cursor.execute("select Name from student where RollNo="+str(id))
                name = my_cursor.fetchone()
                name = "+".join(name)

                my_cursor.execute("select Gender from student where RollNo="+str(id))
                gen = my_cursor.fetchone()
                gen = "+".join(gen)
                    
                my_cursor.execute("select Section from student where RollNo="+str(id))
                section = my_cursor.fetchone()
                section = "+".join(section)

                my_cursor.execute("select RollNo from student where RollNo="+str(id))
                roll = my_cursor.fetchone()
                roll = "+".join(roll)


                if confidence>= 65:
                    cv2.putText(img,f"Name: {name}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,0.8,(50, 127, 205),3)
                    cv2.putText(img,f"Section: {section}",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll No: {roll}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Gender: {gen}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendece(name,roll,section)
                 
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),5)

                coord = [x,y,w,h]

            return coord

        def recognition(img,clf,faceCascade):
            coord = draw_boundry(img,faceCascade,1.1,10,(255,255,255),'Face',clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
            
        while True:
            ret,img = video_cap.read()
            img = recognition(img,clf,faceCascade)
            cv2.imshow('Marking Your Attendence',img)

            if cv2.waitKey(1) == 13:
                break   
                video_cap.release()
                cv2.destroyAllWindows()







if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognizer(root)
    root.mainloop()
