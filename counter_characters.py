# function to count characters
def counter_letters(list_words):
    #count=[]
    summation=0
    for i in list_words:
        #amount=len(i)
        summation=summation+ len(i)
        #count.append(amount)
    return summation

count_letters= lambda list_test: [len(x) for x in list_test] # function lambda to count letters in a word

calculator= { # lambda function dictionary for a calculator
    'sum': lambda x,y: x+y,
    'sub': lambda x,y: x-y, 
    'mult': lambda x,y: x*y,
    'div': lambda x,y: x/y,
}

if __name__ == "__main__": # used so that this code is used only when using the main file
    
    list_of_words=['dog is gay','elefant is fat', 'tiger is fast']
    text=input('please type a text: ')
    print(counter_letters(list_of_words))
    print(counter_letters(text))
    print(count_letters(list_of_words))
    
    print(type(calculator))
    addition=calculator['sum']
    subtration=calculator['sub']
    multiplication=calculator['mult']
    division=calculator['div']
    print(addition(10,5))
    print(subtration(10,5))
    print(multiplication(10,5))
    print(division(10,5))