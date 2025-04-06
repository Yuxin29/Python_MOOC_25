tem = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
if tem > 20:
    print("Wear jeans and a T-shirt")
elif tem > 10:
    print("I recommend a jumper as well")
    print("Wear jeans and a T-shirt")
elif tem > 5:
    print("I recommend a jumper as well")
    print("Wear jeans and a T-shirt")
    print("Take a jacket with you")
else:
    print("I recommend a jumper as well")
    print("Wear jeans and a T-shirt")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!")
else:
    print()