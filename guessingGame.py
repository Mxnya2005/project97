intro1=input("guess a number between 1-9: ")
number= 9
chances=5

for i in intro1:
    chances=chances-1
    if(i==number):
        number=number+1

print("Your guess was too low")
print(chances)
print("Retry your guess: ")
print(number)

