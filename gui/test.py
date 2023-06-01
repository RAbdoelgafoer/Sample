# import math
# import sys
# from os import rename
import requests

# print(sys.version)
# print(sys.executable)
# name = input("Your name?")
# print(f"Hello, {name}")


# def greet(who_to_greet):
#     test = "test"
#     greeting = f"hello, {who_to_greet}"
#     return greeting

r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
# print(greet("Reza"))


# ====== ignore... output below this line =====================================
