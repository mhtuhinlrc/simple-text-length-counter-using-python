# Define a fuction
# In this example I've use countLength() as function name
# And "i" is a parameter that contains the text that we want to count

def countLength(i):
    
    # count the length of "i"
    # Note: Counting the length of "i" using len() gives a int number
    # So, I've use a str() to convert it to string
    a = str(len(i))

    # Here I've convert it to int data type for the condition
    # If text length is between 0-1 character give this output( without s )
    if int(a) <= 1: 
        return "Your text is a total of " + a + " character long"

    # If the text length is bigger than 1
    else:
        return "Your text is a total of " + a + " characters long"

# Get the text from user and convert it to string
text = str(input())

# Run the function from the user input text
calculateLength = countLength(text)

# Print the result
print(calculateLength)
