from operator import length_hint
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv

from tkinter import  filedialog



mydata = []

class Attendence:
    def __init__(self,root):
        self.root = root
        self.root.geometry("2560x1440+0+0")
        self.root.title("Attendece Database")




         #------------------------------variables-----------------------------------

        self.var_Name = StringVar()
        self.var_Rollno = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_section = StringVar()
        self.var_attendencestatus = StringVar()






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

        studentname_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_Name, font=("times new roman",20,"bold"))
        studentname_entry.grid(row = 0 , column=1,sticky=W)



        roll_no_label = Label(left_inside_frame,text='Roll No : ',font=("times new roman",20,"bold") , width=8,bg='white')
        roll_no_label.grid(row = 1 , column=0 ,pady=20,sticky=W,padx=10)

        roll_no_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_Rollno, font=("times new roman",20,"bold"))
        roll_no_entry.grid(row = 1 , column=1,pady = 20 ,sticky=W)






        time_label = Label(left_inside_frame,text='Time: ',font=("times new roman",20,"bold") , width=13,bg='white')
        time_label.grid(row = 2 , column=0,pady=20,sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_time, font=("times new roman",20,"bold"))
        time_entry.grid(row = 2 , column=1,pady = 20 ,sticky=W)






        studentsection_label = Label(left_inside_frame,text='Section : ',font=("times new roman",20,"bold") , width=8,bg='white')
        studentsection_label.grid(row = 0 , column=3 ,pady=40,sticky=W,padx=10)

        studentsection_entry = ttk.Entry(left_inside_frame, width=20, textvariable= self.var_section, font=("times new roman",20,"bold"))
        studentsection_entry.grid(row = 0 , column=4,sticky=W)

        



        date_label = Label(left_inside_frame,text='Date: ',font=("times new roman",20,"bold") , width=15,bg='white')
        date_label.grid(row = 1 , column=3 ,pady=40,sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_date, font=("times new roman",20,"bold"))
        date_entry.grid(row = 1 , column=4,pady = 40 ,sticky=W)




        attendence_label = Label(left_inside_frame,text='Attendence:',font=("times new roman",20,"bold"),bg = 'white',width=8)
        attendence_label.grid(row = 2 , column=3)

        attendence_combo = ttk.Combobox(left_inside_frame,width = 20,textvariable= self.var_attendencestatus, font=("times new roman",20,"bold"),state="readonly")
        attendence_combo['values'] = ("Status",'Present','Absent','Half Day')
        attendence_combo.current(0)
        attendence_combo.grid(row = 2 , column=4 ,pady=20,sticky=W)

        


        # button frame 

        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x = 0 , y = 700,width=1290,height=60)


        import_btn = Button(btn_frame,text="Import Csv", command=self.importCsv,font=("times new roman",20,"bold"),bg='blue',fg='white',width=19)
        import_btn.grid(row = 0 ,column=0)


        export_btn = Button(btn_frame,text="Export Csv",command=self.exportCsv ,font=("times new roman",20,"bold"),bg='blue',fg='white',width=20)
        export_btn.grid(row = 0 ,column=1)


        update_btn = Button(btn_frame,text="Update", font=("times new roman",20,"bold"),bg='blue',fg='white',width=19)
        update_btn.grid(row = 0 ,column=2)

        reset_btn = Button(btn_frame,text="Reset", command=self.reset_data, font=("times new roman",20,"bold"),bg='blue',fg='white',width=20)
        reset_btn.grid(row = 0 ,column=3)





       # right side frame
        Right_frame = LabelFrame(main_frame,bd=2 ,bg = "white", relief= RIDGE ,text= "Student Attendence Details",font=("times new roman",20,"bold"))
        Right_frame.place(x = 1320 , y = 10,width = 1105,height =1280)


        #----------------Table Frame ---------------------


        table_frame = Frame(Right_frame,bd=2 ,bg = "white", relief= RIDGE)
        table_frame.place(x = 2, y = 10,width = 1093,height = 1220)


        #----------------------------Scroll Bar--------------------

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("Name","Roll No","Section","TIME","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.xview)

        
        self.AttendenceReportTable.heading("Name",text="Student Name")
        self.AttendenceReportTable.heading("Roll No",text="Roll No ")
        self.AttendenceReportTable.heading("Section",text="Section")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("TIME",text="Time")
        self.AttendenceReportTable.heading("attendence",text="Status")


        self.AttendenceReportTable["show"] = "headings"

        '''self.AttendenceReportTable.column('Name',width=100)
        self.AttendenceReportTable.column('Roll No',width=100   )
        self.AttendenceReportTable.column('Section',width=100)
        self.AttendenceReportTable.column('date',width=100)
        self.AttendenceReportTable.column('TIME',width=100)
        self.AttendenceReportTable.column('attendence',width=100)'''


        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #----------------------------Fetching the Data------------------------------


    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    

    #------------------------- import button function here------------------------------
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Please Select Your File",filetypes=(("CSV Files","*.csv"),("All Files","*.*")),parent=self.root)

        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")

            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)



    

    #-----------------------export button function here-------------------------------

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data in the DataBase to export",parent= self.root)
                return False

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Please Select Your File",filetypes=(("CSV Files","*.csv"),("All Files","*.*")),parent=self.root)

            with open(fln,mode="w",newline="") as myfile:
                exp_write= csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Csv File has been exported successfully to "+ os.path.basename(fln))

        
        except Exception as es:
            messagebox.showerror('Error',f'Due to : {str(es)}',parent = self.root)

    
    def get_cursor(self,event=""):
        cursor_row = self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursor_row)
        rows = content['values']

        self.var_Name.set(rows[0])
        self.var_Rollno.set(rows[1])
        self.var_section.set(rows[2])
        self.var_time.set(rows[3])
        self.var_date.set(rows[4])
        self.var_attendencestatus.set(rows[5])


    def reset_data(self):

        self.var_Name.set("")
        self.var_Rollno.set("")
        self.var_section.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendencestatus.set("")





                    


        




if __name__ == '__main__':
    root = Tk()
    obj = Attendence(root)
    root.mainloop() 
