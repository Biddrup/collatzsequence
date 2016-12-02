def collatz(number):
    #Is this a even number
    if number % 2 == 0:
        b = number // 2
        return b
    #This one is for odd number
    else:
        b = 3 * number + 1
        return b
    
#Will take a number from you
n = input('Please, give me a number: ')

#Do a list of sequence
sequence = []

#This loop will contune untill it gets 1
while n != 1:
    n = collatz(int(n))
    sequence.append(n)
    
print (sequence)
