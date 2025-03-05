itens = ["Apple", "Banana", "Red Meat", "Chicken", "Cocumber", "Carriot"];
prices = [6.71,1.11,8.0,6.0,16.50, 2.87,1.34]; Orderlist = []
AdmPass = "Root123"; Pass=""; tries = 0 ; n = 1; j = 1;k = 0;l = 0;m = 0;total = 0;
User = input("Customer / Admnister: ")

if User == "Admnister":
    while AdmPass != Pass or tries < 4:
        Pass = input("Administer password: ")
        tries +=1
        if tries == 4:
            print ("Blocked for Wrong password!")
        elif AdmPass == Pass:
            AddorRem = input("Add / Remove (l -> list, e -> exit): ")
            
            if AddorRem == "Add":
                Add = itens.append(input("What do you wanna add: "))
                AddP = prices.append(float(input("For which price: ")))
            
            elif AddorRem == "Remove":
                Remo = itens.remove(input("What do you wanna Remove: "))
                RemoP = prices.remove(float(input("For which price: ")))
            
            elif AddorRem == "l":
                for i in itens:
                    print(f"{n}. {i} - $ {prices[k]:.2f} per Kg")
                    n+=1; k+=1

elif User == "Customer":
    for i in itens:
        print(f"{n}. {i} - $ {prices[k]:.2f} per Kg")
        n+=1; k+=1

    while not 0 in Orderlist:
        Order = Orderlist.append(int(input("What's your order(0 to exit): ")))
    
    for l in Orderlist:
        print(itens[l-1],"$ ",prices[Orderlist[m]])
        total += prices[Orderlist[m]]
        l+=1;m+=1

    print(f"The total amount is : {total} $")


    
    
    



    
    
    
    
    
 
