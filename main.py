from hello import hello
from boo import boo
from foo import foo

if __name__ == "__main__":
    times = int(input("Enter times for printing: "))
    name = input("Enter name: ")
    print('My name is Rodion from RT5')

    hello(times, name)
    boo()
    foo()

    print("New message")

    for _ in range(10):
        continue