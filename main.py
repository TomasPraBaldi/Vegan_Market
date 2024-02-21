from functions import *

cart = []
cart_total = 0

welcome()

shopping(cart)

cart_total = payment(cart, cart_total)

creating_CSV(cart, cart_total)