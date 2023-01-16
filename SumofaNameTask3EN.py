print('CODING SUM OF A NAME')
import string
dict = {}
bool = False
user_string = input("Please enter the letters here that you want to add up:")
String_Num = ""

for i, char in enumerate(string.ascii_lowercase):
    dict[i] = char # This is dictinoary.

for val in user_string.lower():
    if(val.isdigit()):
        print("Sorry, the process could not be completed! Make sure you use letters.")
        bool = True
        break
    for key, value in dict.items():
        if(val == value):
            String_Num += str(key+1)
            # For spaces
            String_Num += " "

if (not bool):
    print("Entered letters:",user_string)
    print("Order of letters in numbers:",String_Num)
    print("sum of the letters:", sum(map(int, String_Num.split())))

input('Press any key to close the program!')