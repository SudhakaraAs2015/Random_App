top_of_range = input("Please Enter Input")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please Enter number more than 0 next time")
        quit()

else:
    print("Please Enter Number next time")
    quit()