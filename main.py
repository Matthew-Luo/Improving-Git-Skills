# This is the main program

print("Hello, how do you do?")
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


print("Look " + user_name + ", I can also count by 2's")
for i in range(0, user_num + 1, 2):
    print(i)
    
# New feature
while True:
    user_interval = input("Please enter a number to count by: ")

    if user_interval.isdigit():
        user_interval = int(user_interval)
        break
    else:
        print("hmmmm, I don't recognize that input")
        
for i in range(0, user_num + 1, user_interval):
    print(i)
    