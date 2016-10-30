def collatz(number):
    #Is this a even number
    if number % 2 == 0:
        b = number // 2
        print (b)
        return b
    else:
        b = 3 * number + 1
        print (b)
        return b
    
n = input('Please, give me a number: ')

while n != 1:
    n = collatz(int(n))
