from lists import *
from art import *
import os
from time import sleep


def loading():
    print('.', end="", flush=True),sleep(0.3),print('.', end="", flush=True),sleep(0.3),print('.'),sleep(0.3)

def welcome():
    print(f"{logo}\nWelcome to the vegan market!") , sleep(1), loading()
    os.system('cls')
    print(f"{prod_list}\nChoose a item by typping his number to add in your basket.") ,sleep(1), loading()
    print("\n# | Price | Item\n-----------------") , {sleep(0.5)}
    for item in products:
        sleep(0.3)
        print(f"{item} | ${products[item][1]/100} | {products[item][0]}")


def shopping(shopping_Cart):
    loading()
    while True:
        choice = 0
        while choice not in products:
            try:
                choice = int(input("Type the respective number of the item you want: "))
            except:
                print("Please, type a valid number.")
                loading()

        while True:
            try:
                qtd = int(input(f"How much {products[choice][0]} that cost ${products[choice][1]/100} you want?\nType a number:  "))
                break
            except:
                loading()
                print("Please, type a number.")
                continue

        while qtd != 0:
            shopping_Cart.append({products[choice][0]:products[choice][1]})
            qtd -= 1
        try:
            keep = int(input("Type 1 to add more items in your cart or 2 to finish: "))
            if keep == 2:
                break
        except:
            print("Please, type a number.")

def payment(shopping_Cart, total): 
    os.system('cls') 

    for each_dict in shopping_Cart:
        for key in each_dict:
            total += int(each_dict[key])

    while True:
        try:
            method = int(input(f"Cart total: ${total/100}\nType: \n1 to use Money(5% disccount)\n2 to use Debit(5% disccount)\n3 to use Credit\n: "))
            if method == 3:
                print("Insert your credit card to pay: ")
                return total
            elif method == 1 or method == 2:
                total -= total*0.05
                print(f"Insert your cedules or debit card to pay: ")
                return total
            else:
                os.system('cls')
                print("Please choose a valid option.")
                loading()
                continue
        except:
            os.system('cls')
            print("You must type a number.")
            loading()


def creating_CSV(shopping_cart, total):  
    with open('Shopping_Cart.csv','w') as f:
        fields_n = ['Cost' ' | ' 'Product']
        f.write(' | '.join(fields_n))
        f.write('\n')
        for row in shopping_cart:
            f.write(','.join(str(x) for x in row.values() ))
            f.write(' | ')
            f.write(','.join(str(x) for x in row))
            f.write('\n')
        if total < 100:
            f.write(f'Total: $0,{int(total)}')
            loading()
            return print(f'You paid: $0,{int(total)}. Thank you!\nYour invoice is saved in the "Shopping_Cart.csv" archive.')
        else:
            total = total/100
            f.write(f'Total: ${"%.2f" % total}')
            loading()
            return print(f'You paid: ${"%.2f" % total}. Thank you!\nYour invoice is saved in the "Shopping_Cart.csv" archive.')