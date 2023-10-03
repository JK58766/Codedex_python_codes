height = int(input("Height (integer number. Ex: 180): "))
credits = int(input("Your credits (integer number. Ex: 150): "))

if height >= 155 and credits >= 25:
    print("Enjoy the ride! ")

elif credits >= 25 and height < 155:
    print("I'm sorry, you're not tal enough to ride...")

elif height >= 155 and credits < 25:
    print("You don't have enough credits.")

else:
    print("You've not met either requirement")