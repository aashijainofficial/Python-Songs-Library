import songs

def MenuSong():
 while True:
     songs.clrscreen()
     print("\t\t\t Song Record Management\n")
     print("==============================================================")
     print("1. Add New Song ")
     print("2. Display Song List ")
     print("3. Search Song ")
     print("4. Delete Song ")
     print("5. Update Song Record ")
     print("6. Play Song ")
     print("7. Return to Main Menu ")
     print("===============================================================")
     choice=int(input("Enter Choice between 1 to 6-------> : "))
     if choice==1:
         songs.insertSong()
     elif choice==2:
         songs.displaySong()
     elif choice==3:
         songs.SearchSongRec()
     elif choice==4:
         songs.deleteSong()
     elif choice==5:
         songs.updateSong()
     elif choice==6:
         songs.playSong()
     elif choice==7:
         return
     else:
         print("Wrong Choice......Enter Your Choice again")
         x=input("Enter any key to continue")
#---------------------------------------------------------------------------------------

MenuSong();
