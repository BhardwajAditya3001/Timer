# Here i have used datetime module so that i can datetime.timedelta and datetime.sleep from this module
import time
import datetime


# Creating a function called countdown so that is actual my Timer
def countdown(h,m,s):

    total_seconds = h*3600 + m*60 +s #coverting given input in the form of seconds 
    while total_seconds > 0:

        timer = datetime.timedelta(seconds = total_seconds)
        print(timer , end="\r")

        time.sleep(1) # delaying my program by one second and reprint it again

        total_seconds = total_seconds - 1 #r educing one second from ttal seconds evry time while loop runs 
    print("You ran out of time !")

#Taking input from the user in the form of hours minutes and seconds 
h = int(input("Enter the number of hours : "))
m = int(input("Enter the number of minutes : "))
s = int(input("Enter the number of seconds : "))

countdown(h,m,s)   # calling my function