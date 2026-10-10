#price = int(input("Please enter the price of car."))
#model = input("Pleace enter the model of car.")
#vehicle_mileage = input("Please enter the vehicle_mileage of car")
#info_car = [price, model, f"{vehicle_mileage} km."]
#print(info_car)

budjet = int(input("Please enter your budget to buy a car:"))
low_budjet_cars = ["Toyota RAV4, Camry 2016-2021", "Mazda CX-5, Mazda 3"]
high_budjet_cars = ["BMV X5", "Porshe 718"]
if budjet <=0:
    print("Please enter a valid code!")
if budjet <= 20000:
    print(f"We can offer you these car:{low_budjet_cars}")
else:
    print(f"We can offer you these car:{high_budjet_cars}")

companies = ("Microsoft", "Apple", "Google", "Amazon", "Meta")
for company in companies:
    if company == "Google":
        print(company)
    else:
        pass

    a = 5
    while a < 10:
        a += 1
        print(a)
