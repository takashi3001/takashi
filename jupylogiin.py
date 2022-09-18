import getpass
condition = input("Want to capture the username automatically?: ")
if condition == "YES" or condition == "yes" or condition == "Yes":
    user = getpass.getuser()
else:
    user = input("User: ")

passw = getpass.getpass()

usrcredentialclient = user
print("NEW Username: ",usrcredentialclient)
passcredentialsclient = passw
print("NEW Password: ",passcredentialsclient)

servercredentialusr = "TAKASHI","ADM"
servercredentialpass = "TAKASHI","ADM"

if usrcredentialclient == servercredentialusr and passcredentialsclient == servercredentialpass:
    print("Sucefull Login")
else:
    print("Wrong Pass")