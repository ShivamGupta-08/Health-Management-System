def getdate():
    import datetime
    return datetime.datetime.now()
def input_name(name):
   ask = name +": What do you want to choose - 1 for diet and 2 for exercise"
   return ask
def retrive (doe,name):
    if doe == 1 and name == "Harry":
        with open("harry_diet.txt")as f:
            for lines in f:
                print(lines, end=" ")

    elif doe == 1 and name == "Rohan":
        with open("rohan_diet.txt")as f:
            for lines in f:
                print(lines, end=" ")
    elif doe == 1 and name == "Hammad":
        with open("hammad_diet.txt")as f:
            for lines in f:
                print(lines, end=" ")
    elif doe == 2 and name == "Harry":
        with open("harry_ex.txt")as f:
            for lines in f:
                print(lines, end=" ")
    elif doe == 2 and name == "Rohan":
        with open("rohan_ex.txt")as f:
            for lines in f:
                print(lines, end=" ")
    elif doe == 2 and name == "Hammad":
        with open("hammad_ex.txt")as f:
            for lines in f:
                print(lines, end=" ")

def take(doe, name):
    if doe == 1 and name == "Harry":
        write = input("Enter your data\n")
        with open("harry_diet.txt", "a")as f:
           f.write(str([str(getdate())])+":"+write+"\n")

    elif doe == 1 and name == "Rohan":
        write = input("Enter your data\n")
        with open("rohan_diet.txt")as f:
            f.write(str([str(getdate())]) + ":" + write + "\n")


    elif doe == 1 and name == "Hammad":
        write = input("Enter your data\n")
        with open("hammad_diet.txt")as f:
            f.write(str([str(getdate())]) + ":" + write + "\n")


    elif doe == 2 and name == "Harry":
        write = input("Enter your data\n")
        with open("harry_ex.txt")as f:
            f.write(str([str(getdate())]) + ":" + write + "\n")


    elif doe == 2 and name == "Rohan":
        write = input("Enter your data\n")
        with open("rohan_ex.txt")as f:
            f.write(str([str(getdate())]) + ":" + write + "\n")


    elif doe == 2 and name == "Hammad":
        write = input("Enter your data\n")
        with open("hammad_ex.txt")as f:
            f.write(str([str(getdate())]) + ":" + write + "\n")


print("Health Management System")
print("Enter your name")
name=input()
print(input_name(name))
doe = int(input())
print("What do you want to do - 1 for retrieve and 2 - log")
rorw = int(input())
#1 for diet and 2 for exersice
#1 for read and 2 for write
if rorw == 1 :
  ret = (retrive(doe,name))

elif  rorw == 2 :
  take(doe,name)
  print("Enter successfully!!!")
