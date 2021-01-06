import sqlite3

def connect_data():
    conn=sqlite3.connect("libBooks.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS libBooks (id INTEGER PRIMARY KEY,memberType text,fName text,lName text,bwDate text,odDate text,address text,mobNum text,\
              bookId text,bookName text,bookAuthor text,bookIsbn text,bookPrice text,bookPages text,ltRfine text)")
    conn.commit()
    conn.close()

def add_Data_Rec(memberType,fName,lName,bwDate,odDate,address,mobNum,bookId,bookName,bookAuthor,bookIsbn,bookPrice,bookPages,ltRfine):
    conn = sqlite3.connect("libBooks.db")
    c = conn.cursor()
    c.execute("INSERT INTO libBooks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
              (memberType,fName,lName,bwDate,odDate,address,mobNum,bookId,bookName,bookAuthor,bookIsbn,bookPrice,bookPages,ltRfine))

    conn.commit()
    conn.close()

def view_data():

    conn = sqlite3.connect("libBooks.db")
    c = conn.cursor()
    c.execute("SELECT * FROM libBooks")
    rows=c.fetchall()
    conn.close()
    return rows

def delect_record(id):
    conn = sqlite3.connect("libBooks.db")
    c = conn.cursor()
    c.execute("DELETE FROM libBooks WHERE id=?",(id,))
    conn.commit()
    conn.close()

def data_update(id,fName="",lName="",bwDate="",odDate="",address="",mobNum="",\
                bookId="",bookName="",bookAuthor="",bookIsbn="",bookPrice="",bookPages="",ltRfine=""):
    conn = sqlite3.connect("libBooks.db")
    c = conn.cursor()
    c.execute("UPDATE libBooks SET fName=?,lName=?,bwDate=?,odDate=?,address=?,mobNum=?,bookId=?,bookName=?,bookAuthor=?,bookIsbn=?,bookPrice=?,bookPages=?,ltRfine=? WHERE id=?",\
              (fName,lName,bwDate,odDate,address,mobNum,bookId,bookName,bookAuthor,bookIsbn,bookPrice,bookPages,ltRfine,id))
    conn.commit()
    conn.close()

def search_book(memberType="",fName="",lName="",bwDate="",odDate="",address="",mobNum="",\
                bookId="",bookName="",bookAuthor="",bookIsbn="",bookPrice="",bookPages="",ltRfine=""):
    conn = sqlite3.connect("libBooks.db")
    c = conn.cursor()
    c.execute("SELECT * FROM libBooks WHERE memberType=? OR fName=? OR lName=? OR bwDate=? OR odDate=? OR address=? OR mobNum=? OR bookId=? OR bookName=? OR bookAuthor=? OR bookIsbn=? OR bookPrice=? OR bookPages=? OR ltRfine=? ",(memberType,fName,lName,bwDate,odDate,address,mobNum,bookId,bookName,bookAuthor,bookIsbn,\
                                                                                                        bookPrice,bookPages,ltRfine))
    rows=c.fetchall()

    conn.close()
    return rows

def books_database_connect():

    conn2=sqlite3.connect("libBooks.db")
    c2=conn2.cursor()
    c2.execute("CREATE TABLE IF NOT EXISTS allBooks (id integer PRIMARY KEY , bookId text,bookName text,bookAuthor text,bookIsbn text,bookPrice text,bookPages text)")
    conn2.commit()
    conn2.close()

def add_data_avl(bookId,bookName,bookAuthor,booksIsbn,bookPrice,bookPages):
    conn2=sqlite3.connect("libBooks.db")
    c2=conn2.cursor()
    c2.execute("INSERT INTO allBooks VALUES (NULL,?,?,?,?,?,?)",(bookId,bookName,bookAuthor,booksIsbn,bookPrice,bookPages))
    conn2.commit()
    conn2.close()

def view_data_avl():
    conn2=sqlite3.connect("libBooks.db")
    c2=conn2.cursor()
    c2.execute("select allBooks.bookId,allBooks.bookName,allBooks.bookAuthor,allBooks.bookIsbn,allBooks.bookPrice,allBooks.bookPages  from allBooks join libBooks on libBooks.bookId=allBooks.bookId ")
    rows=c2.fetchall()

    conn2.close()
    return rows


connect_data()
books_database_connect()
