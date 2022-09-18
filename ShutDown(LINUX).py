#This Command Just Works On Linux!!
#The Command That Work on Windows its on my GitHub

#Module Import

import os

#Variable Create // Ask If You Want ShutDown

Quest = input("Want To ShutDown? (Yes/No) ")

#Checks If You Want ShutDown // Execute The command to ShutDown

if Quest == "Yes" or Quest == "YES" or Quest == "yes":
    os.system("shutdown now")
else:
    print("Ok I I'Il Dont ShudDown")
