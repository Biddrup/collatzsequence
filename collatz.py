#This is for positive number
def collatzPositive(positiveNumber):
    if positiveNumber % 2 == 0:
        print(positiveNumber // 2)
        return positiveNumber // 2
    else:
        print(positiveNumber * 3 + 1)
        return positiveNumber * 3 + 1

#This is for negative number    
def collatzNegative(negativeNumber):
    if negativeNumber % 2 == 0:
        print(negativeNumber // 2)
        return negativeNumber // 2
    else:
        print(negativeNumber * 3 - 1)
        return negativeNumber * 3 - 1
    
#Starts
try:
    givenNumber = int(input('Enter number: '))
    if givenNumber > 0:
        while givenNumber != 1:
            givenNumber = collatzPositive(givenNumber)
    else:
        while givenNumber != -1:
            givenNumber = collatzNegative(givenNumber)
except ValueError:
    print('Type an interger')
