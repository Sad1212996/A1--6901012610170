# - say_hello( choice )
# function name: say_hello
# parameter name: choice
# when choice equal 1, it will print out "Hello, KMUTNB"
# when choice equal 2, it will print out "Sawasdee, KMUTNB"
# when choice equal 3, it will print out "<hello in another language>, KMUTNB"
# when choice equal 4, it will print out "Error: there is no choice 4, please try
# again"

    # definition
def say_hello():
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        print("Hello, KMUTNB")
    elif choice == 2:
        print("Sawasdee, KMUTNB")
    elif choice == 3:
        print("Bonjour, KMUTNB")
    elif choice == 4:
        print("Error: there is no choice 4, please try again")
        
say_hello() # การเรียกใช้งาน call


# Lab 2: Function :L2
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

