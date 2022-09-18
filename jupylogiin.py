#YOU CAN COPY AND PASTE THIS CODE
#IMPORT THIS MODULE 

import getpass

#ASK IF YOU WANT CAPTURE THE USER AUTOMATICALLY

condition = input("Want to capture the username automatically?: ")
if condition == "YES" or condition == "yes" or condition == "Yes":
    #What Happens if conditiom is correct
    user = getpass.getuser()
else:
    #What Happens if condition is incorrect
    user = input("User: ")

#inputs password

passw = getpass.getpass()

#new var // print the credentials

usrcredentialclient = user
print("NEW Username: ",usrcredentialclient)
passcredentialsclient = passw
print("NEW Password: ",passcredentialsclient)

#Credential Bank (List)

servercredentialusr = None
servercredentialpass = None

if usrcredentialclient == servercredentialusr and passcredentialsclient == servercredentialpass:
    #What Happens if credentials is correct
    print("Sucefull Login")
else:
    #What happens if its incorrect
    print("Wrong Pass")
