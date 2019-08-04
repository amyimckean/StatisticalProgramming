 September 22nd, 2018
# CPSC-51100 Statistical Programming
# Fall 1, 2018
# Programming Assignment 4: Estimating Probabilities
import pandas as pd

# Prints the program header
def print_header():
    print ("CPSC-51100, Fall 2018")
    print ("Name: Amy Wilson")
    print ("PROGRAMMING ASSIGNMENT #4")
    
# Prompts the user for input and checks that it is
# greater than 0    
def get_input():
    number_of_cars = raw_input("Enter the number of car instances: ")
    try:
        casted_input = int(number_of_cars)      
        if casted_input >= 0:
            return casted_input
        else:
            return -1    
    except ValueError:
        return -1
 
# Prompts the user for car input and checks that
# 4 items separated by a comma have been added       
def get_car_input():
    user_selection = raw_input("Enter the make,model,type,rating: ")
    try:
        attributes = [x.strip() for x in user_selection.split(',')]
        if len(attributes) == 4:
            return attributes
        else:
            return None
    except ValueError:
        return -1      
   
# Fills the car dataframe with user input and prints it to
# the screen
def get_print_car_dataframe(number_of_cars):
    car_df = pd.DataFrame(columns=['make','model','type','rating'])
    iteration = 0
    while iteration < number_of_cars:
        user_cars = get_car_input()
        if user_cars != None: 
            car_df.loc[iteration] = user_cars
        iteration += 1       
    print  "\n", car_df, "\n"
    return car_df
    
# Calculates and prints the rating probability    
def calculate_print_rating(car_df):
    rating = pd.DataFrame(columns=['calculations', 'index', 'printconcat'])
    rating['calculations'] = car_df.groupby('rating').size().div(len(car_df))
    rating['index'] = rating.index.map(lambda x: str.format("Prob(rating={})", x))
    rating['printconcat'] =  [str.format("{} = {:,.6f}", y[0], y[1]) for y in map(tuple, rating[['index', 'calculations']].values)]  
    print rating.printconcat.to_string(index=False, header=False), "\n"

# Calculates and prints the rating and type probability
def calculate_print_type_rating(car_df):
    rating_type = pd.DataFrame(columns=['calculations', 'index', 'printconcat'])
    rating_type['calculations'] = car_df.groupby(['rating', 'type']).size().unstack(fill_value=0).stack().div(car_df.groupby('rating').size())
    rating_type['index'] = rating_type.index.map(lambda x: str.format("Prob(type={}|rating={})", x[1], x[0]))
    rating_type['printconcat'] =  [str.format("{} = {:,.6f}", y[0], y[1]) for y in map(tuple, rating_type[['index', 'calculations']].values)]  
    print rating_type.printconcat.to_string(index=False, header=False) 
     
# Print the file header
print_header()

# Query the user for an input and validate it is 
# non-negative integer
number_of_cars = get_input();

# Get cars and process rating and rating/type calculations
car_df = get_print_car_dataframe(number_of_cars)   
calculate_print_rating(car_df)
calculate_print_type_rating(car_df)