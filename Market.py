itens = ["Apple", "Banana", "Red Meat", "Chicken", "Cocumber", "Potato"]
AdmPass = "Root123" ; tries = 0 ; n = 1
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
        print(n,i)
        n+=1
        
    Order = itens[int(input("What's your order: "))]
    
    if len(Order) > 1:
        for j in len(Order)
        Order[j] = itens [Order[j]]
        j += 1
    
    
    
 
