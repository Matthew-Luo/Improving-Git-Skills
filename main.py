# This is the main program

print("Hello there, how are you?")
user_name = input("What's your name? ")

while True:
    user_input = input("Please enter a number: ")

    if user_input.isdigit():
        user_num = int(user_input)
        
        if user_num < 100 and user_num >= 0 :
            break
        else:
            print("Number is too high")
    else:
        print("hmmmm, I don't recognize that number")
         
print("I can count to you number")

for i in range(user_num + 1):
    print(i)

