selection=-1

flag=True
while flag:
    print("1. Apple")
    print("2. Orange")
    print("3. Grapes")
    print("4. Banana")
    selection=int(input("Enter your choice "))
    if selection > 4:
        flag=False
    print("Your previous choice was ",selection)
        
