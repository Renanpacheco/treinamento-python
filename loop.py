#Calculate prime numbers up to a certain value

decision='y' # Variable to decide repetition
while decision=='y':
    limit= int(input('Enter with a number: ')) # Input to be calculated
    #print(number%2)
    if limit==0:
        print('0 is neither prime, nor composite number, also, zero has an infinite number of divisors (any nonzero whole number divides zero).')
    elif limit==1:
        print('1 is not a prime number, because Prime Numbers are numbers greater than 1, because Prime Numbers should have 1 and the number itself, as its factor, which means, it must have only two positive factors')
    else:
        for number in range(2,limit+1):
            number_div=0 # variable to keep the number of divisions
            for i in range (2, number): # Repeating loop to calculate the dividers
                remainder=number%i # Variable to cauculate remainder of division
                #print(i, remainder)
                if remainder==0:
                    number_div=number_div+1

            if number_div ==0: # Decision to define which part will be printed
                print(number)
                #print('This number {} is a prime number'.format(number))
            #else:
                #print('This number {} is not a prime number'.format(number))
    decision=input('If you want to repeat press y, otherwise press any other letter: ')

print('Thanks for using me')