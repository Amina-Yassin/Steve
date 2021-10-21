
# def grade(evaluation):
#     if evaluation >= 80:
#         print ("You get an A! Congrats.")
#     elif evaluation >= 65:
#         print ("You get a B! Nice work.")
#     elif evaluation >= 50:
#         print ("You get a C! You passed.")
#     elif evaluation < 50:
#         print ("You got a D! So close.")

# mark = int(input("Please tell me your mark homie."))
# Final_eval = grade(mark)

# def is_even(n):
#     if n %2 == 0:
#         print ("Even.")
#     else:
#         print ("Odd.")

# n1 = int(input("Type in a number to check if it is even bro."))
# Check = is_even(n1)

# for jokes in ["Bob", "Steve", "John"]:
#     print ("How you doing fellow", jokes)

def sumTotal(number_for_accumulation):
    theSum = 0
    for aNumber in range(1, number_for_accumulation + 1):
        theSum = theSum + aNumber
        print (aNumber)
    return theSum
 
accumulation_amount = sumTotal(9)
print("Adds up to", accumulation_amount)

#so what is happening here is that the function sumTotal is called by accumulation_amount with the parameter of 9
#In the function there is the use of an accumulatior theSum
#Inside there is a for loop aNumber with a range of 1, and number_for accumulation + 1.
# This range makes it so that the number starts at 1, since the range ususally starts at 0
# and ends at number_for_accumulation + 1, so it actually runs the number up to nine instead of stopping at nine.
# theSum goes up from 0 by each number in the range being added to it. 
# it prints aNumber each time as well. 
# It returns theSum at the end, which gets returned to accumulation_amount and printed out. 