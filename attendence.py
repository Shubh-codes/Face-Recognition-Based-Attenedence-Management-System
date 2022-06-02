from tkinter import *
from tkinter import ttk
from turtle import circle, left, update
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("2560x1440+0+0")
        self.root.title("Attendece Database")

        img1 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\\img4.png')
        img1 = img1.resize((2560,1440),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_image = Label(self.root,image = self.photoimg1)
        bg_image.place(x = 0 , y = 0,width = 2560,height = 1440)

        #title
        title_lable = Label(bg_image,text="Attendence Management",font=("times new roman",35,"bold"),bg = "red",fg = "white")
        title_lable.place(x = 0 , y = 0, width = 2560,height= 45)

        #frame

        main_frame = Frame(bg_image,bd=2)
        main_frame.place(x = 45 , y = 65 , width = 2450 , height = 1310)

        # left side frame
        left_frame = LabelFrame(main_frame,bd=2 ,bg = "white", relief= RIDGE , text= "Attendance Details",font=("times new roman",20,"bold"))
        left_frame.place(x = 10 , y = 10,width = 1300,height =1280)

        img_left = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\student.jpg')
        img_left = img_left.resize((660,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_left)

        f_lable = Label(left_frame,image = self.photoimg)
        f_lable.place(x = 5 , y = 0,width = 660,height = 200)


        img_left1 = Image.open('C:\\Users\\shubh\\Desktop\\Coding Projects\\Machine Learning Projects\\Face Recognition based attendence system\\collect images\student3.jpg')
        img_left1= img_left1.resize((630,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img_left1)

        f_lable = Label(left_frame,image = self.photoimg2)
        f_lable.place(x = 665 , y = 0,width = 630,height = 200)


        #frame

        left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg='white')
        left_inside_frame.place(x = 0 , y = 205 , width = 1295 , height = 1040)

        #label and entries

        #student name
        studentname_label = Label(left_inside_frame,text='Name : ',font=("times new roman",20,"bold") , width=8,bg='white')
        studentname_label.grid(row = 0 , column=0 ,pady=40,sticky=W)

        studentname_entry = ttk.Entry(left_inside_frame, width=20,font=("times new roman",20,"bold"))
        studentname_entry.grid(row = 0 , column=1,sticky=W)


         #student id
        id_label = Label(left_inside_frame,text='Attendence ID : ',font=("times new roman",20,"bold") , width=20,bg='white')
        id_label.grid(row = 0 , column=2 ,pady=20,sticky=W)

        id_entry = ttk.Entry(left_inside_frame, width=20,font=("times new roman",20,"bold"))
        id_entry.grid(row = 0 , column=3,pady = 20 ,sticky=W)


        #student roll no
        roll_no_label = Label(left_inside_frame,text='Roll No : ',font=("times new roman",20,"bold") , width=8,bg='white')
        roll_no_label.grid(row = 1 , column=0 ,pady=20,sticky=W,padx=20)

        roll_no_entry = ttk.Entry(left_inside_frame, width=20,font=("times new roman",20,"bold"))
        roll_no_entry.grid(row = 1 , column=1,pady = 20 ,sticky=W)




        #student date
        date_label = Label(left_inside_frame,text='Date: ',font=("times new roman",20,"bold") , width=20,bg='white')
        date_label.grid(row = 1 , column=2 ,pady=40,sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20,font=("times new roman",20,"bold"))
        date_entry.grid(row = 1 , column=3,pady = 40 ,sticky=W)



        #student stream 

        dep_label = Label(left_inside_frame,text='Department: ',font=("times new roman",20,"bold") , width=13,bg='white')
        dep_label.grid(row = 2 , column=0 ,pady=20,sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, width=20,font=("times new roman",20,"bold"))
        dep_entry.grid(row = 2 , column=1,pady = 20 ,sticky=W)


        #time

        time_label = Label(left_inside_frame,text='Date: ',font=("times new roman",20,"bold") , width=20,bg='white')
        time_label.grid(row = 2 , column=2 ,pady=40,sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20,font=("times new roman",20,"bold"))
        time_entry.grid(row = 2 , column=3,pady = 40 ,sticky=W)


        #attedence

        attendence_label = Label(left_inside_frame,text='Attendence:',font=("times new roman",20,"bold"),bg = 'white',width=8)
        attendence_label.grid(row = 3 , column=0)

        attendence_combo = ttk.Combobox(left_inside_frame,width = 20,font=("times new roman",20,"bold"),state="readonly")
        attendence_combo['values'] = ("Status",'Present','Absent','Half Day')
        attendence_combo.current(0)
        attendence_combo.grid(row = 3 , column=1 ,pady=20,sticky=W)

        


        # button frame 

        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x = 0 , y = 700,width=1290,height=60)


        import_btn = Button(btn_frame,text="Import Csv",font=("times new roman",20,"bold"),bg='blue',fg='white',width=19)
        import_btn.grid(row = 0 ,column=0)


        export_btn = Button(btn_frame,text="Export Csv", font=("times new roman",20,"bold"),bg='blue',fg='white',width=20)
        export_btn.grid(row = 0 ,column=1)


        update_btn = Button(btn_frame,text="Update", font=("times new roman",20,"bold"),bg='blue',fg='white',width=19)
        update_btn.grid(row = 0 ,column=2)

        reset_btn = Button(btn_frame,text="Reset", font=("times new roman",20,"bold"),bg='blue',fg='white',width=20)
        reset_btn.grid(row = 0 ,column=3)





        # right side frame
        Right_frame = LabelFrame(main_frame,bd=2 ,bg = "white", relief= RIDGE ,text= "Attendence data",font=("times new roman",20,"bold"))
        Right_frame.place(x = 1320 , y = 10,width = 1105,height =1280)

        

        #frame

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x = 0 , y = 700,width=1290,height=60)
        




if __name__ == '__main__':
    root = Tk()
    obj = Attendence(root)
    root.mainloop() 
