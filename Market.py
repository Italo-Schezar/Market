itens = ["Apple", "Banana", "Red Meat", "Chicken", "Cocumber", "Potato"];
prices = [5.0,23.0,4.0,6.0,10.0,14.0]; Orderlist = []
AdmPass = "Root123" ; tries = 0 ; n = 1; j = 1;k = 0;l = 0
User = input("Customer / Admnister: ")

if User == "Admnister":
    Pass = input("Administer password: ")
    while AdmPass != Pass and tries < 4:
        Pass = input("Administer password: ")
        tries +=1
        if tries == 4:
            print ("Blocked for Wrong password!")

elif User == "Customer":
    for i in itens:
        print(f"{n}. {i} - $ {prices[k]:.2f}")
        n+=1; k+=1

    while not 0 in Orderlist:
        Order = Orderlist.append(int(input("What's your order(0 to exit): ")))
    
    for l in Orderlist:
        print(Orderlist,prices[Orderlist[l]])
        l+=1




    
    
    
    
    
 
