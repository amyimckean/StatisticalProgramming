# Amy Wilson
# September 4th, 2018
# CPSC-51100 Statistical Programming
# Fall 1, 2018
# Programming Assignment 1: Descriptive Statistics

# Prints the program header
def print_header():
    print ("CPSC-51100, Fall 2018")
    print ("Name: Amy Wilson")
    print ("PROGRAMMING ASSIGNMENT #1")
    print ("")
        
# Verifies the user provided input is an integer value 
# greater than 0    
def check_input(user_input):
    try:
        #Try to cast user input to an int
        casted_input = int(user_input)
        if casted_input >= 0:
            # Return the casted input if it's a value greater 
            # or equal to 0
            return casted_input
        else:
            # Return -1 for values less than 0
            return -1
    except ValueError:
        # If the input is not an int, return -1 because we can't 
        #process the value
        return -1
      
# Calculates the mean with the user provided number 
# and the previously persisted mean 
def calculate_mean(number):
    return persisted_mean + (number - persisted_mean)/number_of_inputs 
    
# Calculates the variance based on the new mean, user 
# provided number, and persisted mean and variance values
def calculate_variance(number, mean):
    if number_of_inputs > 1:
        # Calculate separate parts of the equation for clarity
        second_factor = (number - persisted_mean)**2/number_of_inputs
        third_factor = persisted_variance/(number_of_inputs - 1)
        return persisted_variance + second_factor - third_factor
    else:
        # Return 0 in cases where there are 1 or fewer inputs
        return 0

# Stores the number of inputs provided by the user		
number_of_inputs = 0 

# Stores the previously calculated mean
persisted_mean = 0.0

# Stores the previously calculated variance
persisted_variance = 0.0

# Stores whether or not the user has provided valid values
valid_value = True

# Print the file header
print_header()

# Continue to promp the user for values until we receive a bad value
while valid_value:
    
    # Query the user for an input and validate it is 
    # non-negative integer
    number = raw_input("Enter a number: ")
    validated_input = check_input(number);
	
    # The user has provided a valid value that 
    # we will process
    if validated_input >= 0 :
        
        # Increment the number of inputs to account 
        # for an additional processed value
        number_of_inputs += 1
        
        # Perform mean and variance calculations
        mean = calculate_mean(validated_input)
        variance = calculate_variance(validated_input, mean)
		
        # Set persisted values to newly calculated 
        # mean and variance
        persisted_mean = mean
        persisted_variance = variance
        
        # Print the values to the console
        print "Mean is ", mean, " variance is ", variance
        print ("")
        
    else:
        # A valid value was not provided
        valid_value = False
    
           