from hello import hello

if __name__ == "__main__":
    times = int(input("Enter times for printing: "))
    name = input("Enter name: ")

    hello(times, name)