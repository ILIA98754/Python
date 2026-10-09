name = input("What is your name?")
age = int(input("How old are you?"))

if age >= 18:
    print(f"Hello {name}, welcome to our magazine!")
    quantity_goods = int(input("Please enter how many goods you bought in our market?"))
    if (quantity_goods > 0 and quantity_goods < 10):
        print("We are sorry, your goods would be transer 5$!")
    if (quantity_goods >= 10):
        print("Your goods would be transfer Free!")
    if (quantity_goods < 10):
        print("You have goods it is not too much")
else:
    print(f"Sorry, {name} your age don't suit for buying these product")
    

#films = ["Garry Potter", "The Lord of the Rings", "Star Wars", "Witcher"]
#           0
#print(films[1])
#print(films[2])
#print(films[3])