import time

num = int(input("Enter your number: "))

if num<2:
    print("Not a Prime number as it is less than 2")

else:
    for i in range(2, num):
        if num % i == 0:
            print("Checking for prime number", end=' ')
            for x in range(3):
                time.sleep(0.3)
                print(".", end=' ')
            time.sleep(0.1)
            print(False)
            break
    else:
        print("Checking for prime number", end=' ')
        for x in range(3):
            time.sleep(0.3)
            print(".", end=' ')

        time.sleep(0.1)
        print(True)
