import random

gesuchteZahl= random.randint(0,100)
versuche=0
User_Zahl= 0

User_Zahl = int(input("Versuchen Sie eine Zahl zu erraten zwischen 0 und 100: "))


while User_Zahl != gesuchteZahl:
    if User_Zahl == gesuchteZahl:
        versuche+=1
        break
    elif User_Zahl < gesuchteZahl:
        User_Zahl= int(input("Zu niedrig! Versuchen Sie es noch ein Mal: "))
        versuche+=1
        continue
    else:
        User_Zahl=int(input("Zu hoch !! Versuchen Sie es noch ein Mal: "))
        versuche+=1
        continue

print("\n")
print("Richtig erraten glückwünsch!! ;)")
print("Sie brauchten ", versuche,"versuche um es zu erraten")


