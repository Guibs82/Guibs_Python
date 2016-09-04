def make_pizza(size, *toppings):
    '''概述要制作的披萨'''
    print("做一个尺寸为: " + str(size) + ", 包含: ")
    for topping in toppings:
        print("- " + topping)
    print("的披萨")

def get_price():
    print("The price is 20")