import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform

def clrscreen():
 
 if platform.system()=="Windows":
     os.system("cls")

def insertSong():
 try:
     cnx = connection.MySQLConnection(user='root', password='', host='127.0.0.1',database='Library')
     Cursor = cnx.cursor()
     sname=input("Enter Song Name : ")
     singer=input("Enter Singer Name : ")
     genre=input("Enter Genre (Pr:Party, Gz: Ghazals ) : ")
     publ=input("Enter Publisher/Company : ")
     rlyr = input("Enter Release Year like 2020 : ")
     file_url = input("Enter youtube url : ")
     Qry = ("INSERT INTO Songs "\
"VALUES (NULL, %s, %s, %s, %s, %s, %s)")
     data = (sname,singer,genre,publ,rlyr, file_url)
     print(data)
     Cursor.execute(Qry,data)
     # Make sure data is committed to the database
     cnx.commit()
     Cursor.close()
     cnx.close()
     print("Record Inserted..............")
 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)

     cnx.close()


def displaySong():
 try:
     os.system('cls')
     cnx = connection.MySQLConnection(user='root', password='',host='localhost',database='LIbrary')
     Cursor = cnx.cursor()
     query = ("SELECT * FROM songs")
     Cursor.execute(query)
     for (sid,title,singer,genre,publ,release_yr,file_url) in Cursor:
         print("==============================================================")
         print("ID : ",sid)
         print("Title : ",title)
         print("Singer : ",singer)
         print("Genre : ",genre)
         print("Publisher : ",publ)
         print("Release Year : ",release_yr)
         print("File Url : ",file_url)
         print("===============================================================")
     Cursor.close()
     cnx.close()
     print("You have done it!!!!!!")
 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)
 
     cnx.close()




def playSong():
 try:
     cnx = connection.MySQLConnection(user='root',password='',host='127.0.0.1',database='Library')
     Cursor = cnx.cursor(dictionary=True)
     bno=input("Enter Song Id to play from the Library : ")

     Qry =("""SELECT * FROM Songs WHERE id = %s LIMIT 1""")
     play_rec=(bno,)
     Cursor.execute(Qry,play_rec)
     records = Cursor.fetchall()
     print(records)

     for row in records:
          print('File Url', row['file_url'])
          if row['file_url'] == 'na' :
              print('This file is not playable')
          else :
           import webbrowser
           #print (row['file_url'])
           webbrowser.open(row['file_url'], new=2)
     # Make sure data is committed to the database
     Cursor.close()
     cnx.close()
     print(Cursor.rowcount,"Record(s) Played Successfully.............")
 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
     else:
        print(err)

     cnx.close()



def SearchSongRec():
 try:
     cnx = connection.MySQLConnection(user='root',password='',host='127.0.0.1',database='Library')
     Cursor = cnx.cursor()
     bno=input("Enter Song Title to be Searched from the Library : ")
     query = ("SELECT * FROM songs where title LIKE %s ")

     rec_srch=(bno + '%',)
     Cursor.execute(query,rec_srch)

     Rec_count=0

     for (sid,title,singer,genre,publ,release_yr,file_url) in Cursor:
       Rec_count+=1
       print("==============================================================")
       print("ID : ",sid)
       print("Title : ",title)
       print("Singer : ",singer)
       print("Genre : ",genre)
       print("Publisher : ",publ)
       print("Release Year : ",release_yr)
       print("File Url : ",file_url)
       print("===============================================================")
       if Rec_count%2==0:
         input("Press any key to continue")
         clrscreen()
         print(Rec_count, "Record(s) found")
     # Make sure data is committed to the database
     cnx.commit()
     Cursor.close()
     cnx.close()

 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)

     cnx.close()


def deleteSong():
 try:
     cnx = connection.MySQLConnection(user='root',password='',host='127.0.0.1',database='Library')
     Cursor = cnx.cursor()
     bno=input("Enter Song ID to be deleted from the Library : ")

     Qry =("""DELETE FROM Songs WHERE ID = %s""")
     del_rec=(bno,)
     Cursor.execute(Qry,del_rec)

     # Make sure data is committed to the database
     cnx.commit()
     Cursor.close()
     cnx.close()
     print(Cursor.rowcount,"Record(s) Deleted Successfully.............")
 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)

     cnx.close()


def updateSong():
 try:
     cnx = connection.MySQLConnection(user='root',password='',host='127.0.0.1',database='Library')
     Cursor = cnx.cursor()
     bno=input("Enter Song ID to be Updated from the Library : ")
     query = ("SELECT * FROM songs where id = %s ")
     rec_srch=(bno,)
     print("Enter new data ")
     sname=input("Enter Song Name : ")
     singer=input("Enter Singer Name : ")
     genre=input("Enter Genre (Pr:Party, Gz: Ghazals ) : ")
     publ=input("Enter Publisher/Company : ")
     rlyr = input("Enter Release Year like 2020 : ")
     file_url = input("Enter youtube url : ")

     Qry = ("UPDATE songs SET title=%s,"\
 "singer=%s,genre=%s,publication=%s,release_year=%s,file_url=%s "\
 "WHERE id=%s")
     data = (sname,singer,genre,publ,rlyr,file_url,bno)
     Cursor.execute(Qry,data)
     # Make sure data is committed to the database'''
     cnx.commit()
     Cursor.close()
     cnx.close()
     print(Cursor.rowcount,"Record(s) Updated Successfully.............")
 except mysql.connector.Error as err: 
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)
     cnx.close()
