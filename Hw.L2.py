name = input("What is your name?")
age = int(input("How old are you?"))

if age >= 18:
    print(f"Hello {name}, welcome to our magazine!")

    weight = int(input("Please enter the weight of goods you bought in our market."))
    if (weight  >= 10):
        print("Shipping is not free!")
        
    else:
        print("Shipping is free!")
else:
    print(f"Sorry, {name} your age don't suit for buying these product")
    
