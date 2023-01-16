print('CODING SUM OF A NAME')
import string
dict = {}
bool = False
user_string = input("Bitte gebe hier die Buchstaben ein, welche du Summieren möchtest:")
String_Num = ""

for i, char in enumerate(string.ascii_lowercase):
    dict[i] = char # This is dictinoary.

for val in user_string.lower():
    if(val.isdigit()):
        print("Entschuldige, der Vorgang konnte nicht abgeschlossen werden!")
        bool = True
        break
    for key, value in dict.items():
        if(val == value):
            String_Num += str(key+1)
            # For spaces
            String_Num += " "

if (not bool):
    print("Eingegebne Buchstaben:",user_string)
    print("Reihenfolge der Buchstaben in Nummern:",String_Num)
    print("Summe der Buchstaben:", sum(map(int, String_Num.split())))
