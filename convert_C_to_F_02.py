# FILE NAME - convert_C_to_F_02.py

# NAME: Evan Beer
# DATE: 3/4/26
# BRIEF DESCRIPTION: The same thing as the previous temperature converter except it can do both celsius to fahrenheit and fahrenheit to celsius.   



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YOUR CODE BELOW THIS LINE ##########

def main():
    Temperature_converter()

def Temperature_converter():
    print('===== Temperature Converter =====')
    print()
    print('  1. Convert from Celsius to Fahrenheit')
    print('  2. Convert from Fahrenheit to Celsius')
    print()
    choice = int(input('Please choose from the above menu: '))
    if choice == 1:
        Celsius = float(input('Enter a temperature to convert: '))
        temperature = Celsius * 9/5 + 32
        print()
        print (f'{Celsius} degrees Celsius is {temperature} degrees Fahrenheit')
    else:
        Fahrenheit = float(input('Enter a temperature to convert: '))
        temperature_2 = (Fahrenheit - 32 ) * 5/9
        print()
        print(f'{Fahrenheit} degrees Fahrenheit is {temperature_2} degrees Celsius')
        
main()









########### END YOUR CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

How to convert fahrenheit to celsius.





'''
