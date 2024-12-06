#import cake from cake file 
from rt_make_cake import get_cake  

print(get_cake())

#function to call for feedback using IF statements
def feedback():
    satisfied = input("Did you like the cake? Yes or No? ")   #Question to ask user and to see their feedback
    if  satisfied == ("yes"):     #Function to see if you liked the cake?
        print("Perfect!!! I am glad!")
    else: 
        print("Oh no! I am sorry!")   #Function to see if you didn't like the cake
    return satisfied # Closes the function terms

#Call the function
feedback()
