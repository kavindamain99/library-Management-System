from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
import booksDatabase
from tkcalendar import DateEntry

class Library:

    def __init__(self,root):
        self.root = root
        self.root.title("Library Management system")
        self.root.geometry("1920x1080")
        self.root.configure(background='black')


        memberType = StringVar()
        fName = StringVar()
        lName = StringVar()
        bwDate = StringVar()
        odDate = StringVar()
        address = StringVar()
        mobNum = StringVar()
        bookId = StringVar()
        bookName = StringVar()
        bookAuthor = StringVar()
        bookIsbn = StringVar()
        bookPrice = StringVar()
        bookPages = StringVar()
        ltRfine = StringVar()

        #Button Functions
        def exit_system():
            exit=tkinter.messagebox.askyesno("Library Management system","Confirm it you want to exit")
            if exit:
                root.destroy()

        def clear_data():
            self.cboMemberType.current(0)
            self.getFirstName.delete(0,END)
            self.getLastName.delete(0,END)
            self.getDateBorrowed.delete(0,END)
            self.getDateDue.delete(0,END)
            self.getAddress.delete(0,END)
            self.getMobileNo.delete(0,END)
            self.getBookId.delete(0,END)
            self.getBookTitle.delete(0,END)
            self.getBookPrice.delete(0,END)
            self.getBookPages.delete(0,END)
            self.getBookAuthor.delete(0,END)
            self.getLateReturn.delete(0,END)
            self.getIsbn.delete(0,END)

        def add_data():
            if(len(memberType.get())!=0):
                booksDatabase.add_Data_Rec(memberType.get(),fName.get(),lName.get(),bwDate.get(),odDate.get(),address.get(),mobNum.get(),\
                                         bookId.get(),bookName.get(),bookAuthor.get(),bookIsbn.get(),bookPrice.get(),bookPages.get(),ltRfine.get())

            bookList.delete(0,END)

            bookList.insert(END,(memberType.get(),fName.get(),lName.get(),bwDate.get(),odDate.get(),address.get(),mobNum.get(),\
                                 bookId.get(),bookName.get(),bookAuthor.get(),bookIsbn.get(),bookPrice.get(),bookPages.get(),ltRfine.get()))


        def add_data_avl_db():

            if(len(bookId.get())!=0):
                booksDatabase.add_data_avl(bookId.get(),bookName.get(),bookAuthor.get(),bookIsbn.get(),bookPrice.get(),bookPages.get())

            bookList.delete(0,END)



        def display_data():

            bookList.delete(0,END)

            for rows in booksDatabase.view_data():
                bookList.insert(END,rows)

        def available_books():
            bookList2.delete(0,END)

            for row in booksDatabase.view_data_avl():
                bookList2.insert(END,row)

        #select a record and get it
        def select_book(event):
            global slctBk
            selectBook=bookList.curselection()[0]
            slctBk=bookList.get(selectBook)

            self.cboMemberType.current(0)
            self.getFirstName.delete(0, END)
            self.getLastName.delete(0, END)
            self.getDateBorrowed.delete(0, END)
            self.getDateDue.delete(0, END)
            self.getAddress.delete(0, END)
            self.getMobileNo.delete(0, END)
            self.getBookId.delete(0, END)
            self.getBookTitle.delete(0, END)
            self.getBookPrice.delete(0, END)
            self.getBookPages.delete(0, END)
            self.getBookAuthor.delete(0, END)
            self.getLateReturn.delete(0, END)
            self.getIsbn.delete(0, END)

            self.cboMemberType.insert(END,slctBk[1])
            self.getFirstName.insert(END,slctBk[2])
            self.getLastName.insert(END,slctBk[3])
            self.getDateBorrowed.insert(END,slctBk[4])
            self.getDateDue.insert(END,slctBk[5])
            self.getAddress.insert(END,slctBk[6])
            self.getMobileNo.insert(END,slctBk[7])
            self.getBookId.insert(END,slctBk[8])
            self.getBookTitle.insert(END,slctBk[9])
            self.getBookPrice.insert(END,slctBk[12])
            self.getBookPages.insert(END,slctBk[14])
            self.getBookAuthor.insert(END,slctBk[10])
            self.getLateReturn.insert(END,slctBk[11])
            self.getIsbn.insert(END,slctBk[13])

        def select_available_book(event):
            global slctAvBk
            selectBook2=bookList.curselection()[0]
            slctAvBk=bookList.get(selectBook2)

        def delete_data():
            booksDatabase.delect_record(slctBk[0])
            clear_data()
            display_data()

        def update_data():
            booksDatabase.data_update(slctBk[0],fName.get(),lName.get(),bwDate.get(),odDate.get(),address.get(),mobNum.get(),\
                                 bookId.get(),bookName.get(),bookAuthor.get(),bookIsbn.get(),bookPrice.get(),bookPages.get(),ltRfine.get())


        def search_data():

            bookList.delete(0,END)
            for row in booksDatabase.search_book(memberType.get(),fName.get(),lName.get(),bwDate.get(),odDate.get(),address.get(),mobNum.get(),\
                                                 bookId.get(),bookName.get(),bookAuthor.get(),bookIsbn.get(),bookPrice.get(),bookPages.get(),ltRfine.get()):
                bookList.insert(END,row)


        #Frame

        mainFrame = Frame(self.root)
        mainFrame.grid()

        titleFrame = Frame(mainFrame,width=1920,padx=20,bd=20,relief=RIDGE)
        titleFrame.pack(side="top")
        self.lblTitle = Label(titleFrame,width=50,font=('arial',35,'bold'),text="\tLibrary Management System\t")
        self.lblTitle.grid()

        buttonFrame = Frame(mainFrame,bd=20,width=1500,height=50,padx=20,relief=RIDGE)
        buttonFrame.pack(side="bottom")

        frameDetail = LabelFrame(mainFrame,bd=10,width=1500,height=240,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Available Book ")
        frameDetail.pack(side='bottom')


        dataFrame = Frame(mainFrame,bd=20,width=1500,height=400,padx=20,relief=RIDGE)
        dataFrame.pack(side="bottom")

        dataFrameLeft = LabelFrame(dataFrame,bd=10,width=900,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Library Membership Info : ")
        dataFrameLeft.pack(side="left")
        dataFrameRight = LabelFrame(dataFrame, bd=10, width=550, height=300, padx=20, relief=RIDGE,font=('arial',12,'bold'),text="Book Details : ")
        dataFrameRight.pack(side="right")

        #member Details

        self.lblMemberType=Label(dataFrameLeft,font=('arial',10,'bold'),text="Member Type : ",padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)

        self.cboMemberType = ttk.Combobox(dataFrameLeft, font=('arial', 10, 'bold'),state='readonly',width=20,textvariable=memberType)
        self.cboMemberType['value']=('','Child','Adult','Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)


        self.lblFirstName = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="First Name : ", padx=2, pady=2)
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.getFirstName = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=fName, width=23)
        self.getFirstName.grid(row=1, column=1)



        self.lblLastName = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Last Name : ", padx=2, pady=2)
        self.lblLastName.grid(row=2, column=0, sticky=W)
        self.getLastName = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=lName, width=23)
        self.getLastName.grid(row=2, column=1)


        self.lblDateBorrowed = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Date Borrowed : ", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=3, column=0, sticky=W)
        self.getDateBorrowed = DateEntry(dataFrameLeft, width=24, year=2021, month=1, day=6,background='darkblue', foreground='white', borderwidth=2,textvariable=bwDate)
        self.getDateBorrowed.grid(row=3, column=1)

        self.lblDateDue = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Date Over Due : ", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=0, sticky=W)
        self.getDateDue = DateEntry(dataFrameLeft, width=24, year=2021, month=1, day=22,background='darkblue', foreground='white', borderwidth=2,textvariable=odDate)
        self.getDateDue.grid(row=4, column=1)


        self.lblAddress = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Address : ", padx=2, pady=2)
        self.lblAddress.grid(row=5, column=0, sticky=W)
        self.getAddress = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=address, width=23)
        self.getAddress.grid(row=5, column=1)


        self.lblMobileNo = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Mobile Number: ", padx=2, pady=2)
        self.lblMobileNo.grid(row=6, column=0, sticky=W)
        self.getMobileNo = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=mobNum, width=23)
        self.getMobileNo.grid(row=6, column=1)


        #book Details

        self.lblBookId = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Book Id  : ", padx=2, pady=2)
        self.lblBookId.grid(row=0, column=3, sticky=W)
        self.getBookId = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=bookId, width=23)
        self.getBookId.grid(row=0, column=4)

        self.lblBookTitle = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Book Name : ", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=3, sticky=W)
        self.getBookTitle = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=bookName, width=23)
        self.getBookTitle.grid(row=1, column=4)

        self.lblBookAuthor = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Book Author  : ", padx=2, pady=2)
        self.lblBookAuthor.grid(row=2, column=3, sticky=W)
        self.getBookAuthor = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=bookAuthor, width=23)
        self.getBookAuthor.grid(row=2, column=4)

        self.lblIsbn = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="ISBN Number  : ", padx=2, pady=2)
        self.lblIsbn.grid(row=3, column=3, sticky=W)
        self.getIsbn = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=bookIsbn, width=23)
        self.getIsbn.grid(row=3, column=4)

        self.lblBookPages = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Pages : ", padx=2, pady=2)
        self.lblBookPages.grid(row=4, column=3, sticky=W)
        self.getBookPages = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=bookPages, width=23)
        self.getBookPages.grid(row=4, column=4)

        self.lblBookPrice = Label(dataFrameLeft, font=('arial', 10, 'bold'), text="Selling Price  : ", padx=2, pady=2)
        self.lblBookPrice.grid(row=5, column=3, sticky=W)
        self.getBookPrice = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=bookPrice, width=23)
        self.getBookPrice.grid(row=5, column=4)

        self.lblLateReturn = Label(dataFrameLeft,font=('arial', 10, 'bold'), text="Late return Fine : ", padx=2, pady=2)
        self.lblLateReturn.grid(row=6,column=3, sticky=W)
        self.getLateReturn = Entry(dataFrameLeft, font=('arial', 10, 'bold'),textvariable=ltRfine, width=23)
        self.getLateReturn.grid(row=6,column=4)

        #details
        textDisplayData=Text(dataFrameRight,font=('arial', 12, 'bold'),padx=8,pady=20,width=50,height=15)
        textDisplayData.grid(row=0,column=0)

        scrollbar=Scrollbar(dataFrameRight)
        scrollbar.grid(row=0,column=1,stick='ns')

        bookList = Listbox(dataFrameRight,width=64,height=18,font=('arial', 10, 'bold'),yscrollcommand=scrollbar.set)
        bookList.bind('<<ListboxSelect>>',select_book)
        bookList.grid(row=0,column=0,padx=8)
        scrollbar.config(command=bookList.yview)

        #available books
        textDisplayData2=Text(frameDetail,font=('arial', 12, 'bold'),padx=8,pady=20,width=157,height=8)
        textDisplayData2.grid(row=0,column=0)

        scrollbar2=Scrollbar(frameDetail)
        scrollbar2.grid(row=0,column=1,stick='ns')

        bookList2 = Listbox(frameDetail,width=200,height=11,font=('arial', 10, 'bold'),yscrollcommand=scrollbar2.set)
        bookList2.bind('<<ListboxSelect>>',select_available_book)
        bookList2.grid(row=0,column=0,padx=8)
        scrollbar2.config(command=bookList2.yview)

        self.btnAddBooks = Button(buttonFrame, text="Add Book", font=('arial', 12, 'bold'), width=15, bd=4, command=add_data_avl_db)
        self.btnAddBooks.grid(row=0,column=7)

        self.btnAddBooks = Button(buttonFrame, text="Available Book", font=('arial', 12, 'bold'), width=15, bd=4,command=available_books)
        self.btnAddBooks.grid(row=0, column=8)


        #Buttons

        self.btnAddData = Button(buttonFrame, text="Add", font=('arial', 12, 'bold'), width=15, bd=4,command=add_data)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData=Button(buttonFrame,text="Display",font=('arial', 12, 'bold'), width=15,bd=4,command=display_data)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnDeleteData = Button(buttonFrame, text="Delete", font=('arial', 12, 'bold'), width=15, bd=4,command=delete_data)
        self.btnDeleteData.grid(row=0, column=2)

        self.btnClearData = Button(buttonFrame, text="Clear", font=('arial', 12, 'bold'), width=15, bd=4,command=clear_data)
        self.btnClearData.grid(row=0, column=3)

        self.btnUpdateData = Button(buttonFrame, text="Update", font=('arial', 12, 'bold'), width=15, bd=4,command=update_data)
        self.btnUpdateData.grid(row=0, column=4)

        self.btnSearchData = Button(buttonFrame, text="Search", font=('arial', 12, 'bold'), width=15, bd=4,command=search_data)
        self.btnSearchData.grid(row=0, column=5)

        self.btnExitData = Button(buttonFrame, text="Exit", font=('arial', 12, 'bold'), width=15, bd=4,command=exit_system)
        self.btnExitData.grid(row=0, column=6)





if __name__=='__main__':
    root = Tk()
    application=Library(root)
    root.mainloop()