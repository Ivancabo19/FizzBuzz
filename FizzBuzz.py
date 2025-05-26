# Contador FizzBuzz

counter = 1
while counter <= 1000:
    if counter % 5 == 0 and counter % 3 == 0:
        print("FizzBuzz")    
    elif counter % 5 == 0:
        print("Buzz")
    elif counter % 3 == 0:
        print("Fizz")
    else:
        print(counter)
    counter += 1