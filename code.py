print("""BOOK LIST:-
1) Alchemist - ₹150
2) My Journey - ₹200
3) Blue Umbrella - ₹75
""")

n1=int(input("Enter number of books you want to purchase"))

if n1==1:
    na=int(input("Enter Book Number"))

    if na==1:
        print("You Want to buy Alchemist")
        print("Your total bill is ₹150")
        print("PayTM - +917042183366 \n pls call before ordering")

    if na==2:
        print("You Want to buy My journey")
        print("Your total bill is ₹200")
        print("PayTM - +917042183366 \n pls call before ordering")

    if na==3:
        print("You Want to buy Blue Umbrella")
        print("Your total bill is ₹75")  
        print("PayTM - +917042183366 \n pls call before ordering")   

if n1==2:

    nb=int(input("Enter Book Number"))  
    nc=int(input("Enter Book Number"))  

    if nb==1 and nc==2:
       print("You Want to buy alchemist and my journey")
       print("Your total bill is ₹350")
       print("PayTM - +917042183366 \n pls call before ordering")

    if nc==1 and nb==2:
       print("You Want to buy alchemist and my journey")
       print("Your total bill is ₹350")
       print("PayTM - +917042183366 \n pls call before ordering")

    if nb==1 and nc==3:  
       print("You want to buy alchemist and blue umbrella")
       print("Your total bill is ₹225")
       print("PayTM - +917042183366 \n pls call before ordering")

    if nc==1 and nb==3:  
       print("You want to buy alchemist and blue umbrella")
       print("Your total bill is ₹225")
       print("PayTM - +917042183366 \n pls call before ordering")

    if nb==2 and nc==3:
       print("You want to buy my journey and blue umbrella")
       print("Your total bill is ₹275")
       print("PayTM - +917042183366 \n pls call before ordering")

    if nc==2 and nb==3:   
        print("You want to buy my journey and blue umbrella")
        print("Your total bill is ₹275")
        print("PayTM - +917042183366 \n pls call before ordering")
