# September 22nd, 2018
# CPSC-51100 Statistical Programming
# Fall 1, 2018
# Programming Assignment 3: Nearest Neighbor Classification
# For this assignment, we decided to work on our
# own implementations and compare the resulting 
# solutions. After some comparisons, this is the 
# solution we decided on."
import numpy as np

# Prints the program header
def print_header():
    print ("CPSC-51100, Fall 2018")
    print ("Name: Amy Wilson, Joan Yoon")
    print ("PROGRAMMING ASSIGNMENT #3")
    print ("")
    
# Prints the actual labels, calculated labels, and accuracy percentage
def print_results(testing_labels, predicted_labels):
    inaccuracies = 0.0
    print "#, True, Predicted"
    for index, value in enumerate(predicted_labels):
        count = index + 1
        if value != testing_labels[index]:
            inaccuracies += 1
        print count, testing_labels[index], " ", value
    print "Accuracy: ", ((count - inaccuracies) / count) * 100, "%"  
    
# Calculate nearest neighbor using distance formula 
def calculate_nearest_neighbor(testing_data, training_data):
    difference_squared = (testing_data[:, None] - training_data)**2
    sum_differences = difference_squared.sum(axis=2)
    return np.sqrt(sum_differences)

# Print file header
print_header()

# The input and output files
testing_data_file = "iris-testing-data.csv"
training_data_file = "iris-training-data.csv"

# Load and parse datasets into arrays
# Attributes into 2d arrays, class labels into 1d arrays
testing_data = np.loadtxt(testing_data_file, delimiter = ",", usecols = range(4))
training_data= np.loadtxt(training_data_file, delimiter = ",", usecols = range(4))
testing_labels = np.loadtxt(testing_data_file, delimiter = ",", dtype="string", usecols = 4)
training_labels = np.loadtxt(training_data_file, delimiter = ",", dtype="string", usecols = 4)

# Calculate results using numpy
nearest_neighbors = calculate_nearest_neighbor(testing_data, training_data)

# Create an array of indicies of minimum values
predicted_labels = [training_labels[index] for index in nearest_neighbors.argmin(axis=1)]

# Print the actual labels and the calculated labels
print_results(testing_labels, predicted_labels)