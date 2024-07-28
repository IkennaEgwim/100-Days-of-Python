print("SECURE LOGIN")

username = input("Username > ")
password = input("Password > ")

if username == "mark" and password == "password":
    print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
    print("Hey there Suzanne!")
elif username == "admin" and password == "admin1":
    print("Hello Admin!")
else:
    print("Go away")