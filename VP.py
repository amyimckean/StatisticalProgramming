# Amy Wison, Joan Yoon
# October 14, 2018
# CPSC-51100 Statistical Programming
# Fall 1, 2018
# Programming Assignment 6: – Visualizing ACS PUMS Data
# For this assignment, we worked on our own implementations, and troubleshooted
# each. With comparisons and integration of both of our ideas, this is our code.
# We chose to match the output in figure_1_2v.png

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load file
data = pd.read_csv("ss13hil.csv")

# Create figure and 2x2 subplots
fig = plt.figure(figsize=(18, 10))
pie = fig.add_subplot(2, 2, 1)
hist = fig.add_subplot(2, 2, 2)
bar = fig.add_subplot(2, 2, 3)
scatter = fig.add_subplot(2, 2, 4)

# Create pie chart
pie.set_title("Household Languages", fontsize = 12)
pie_values = data["HHL"].value_counts()
pie_labels = ["English only", "Spanish", "Other Indo-European", "Asian and Pacific Island languages", "Other"]
pie.pie(pie_values, startangle = 242)
pie.legend(pie_labels, loc="upper left")
pie.axis("equal")

# Reset pie position to match png left location
box = pie.get_position()
box.x0 = box.x0 - 0.125
box.x1 = box.x1 - 0.125
pie.set_position(box)

# Create histogram
hist.set_title("Distribution of Household Income", fontsize = 12)
log_bins = np.logspace(1, 7, num = 100)
hist.hist(data['HINCP'], bins = log_bins, range=(0,1), color = "green", normed = True, alpha = 0.5)
data['HINCP'].plot(ax = hist, kind = "KDE", color = "black", linestyle = "dashed")
hist.set_xlabel("Household Income ($) - Log Scaled", fontsize = 10)
hist.set_ylabel("Density", fontsize = 10)
hist.set_xscale("log")
hist.tick_params(labelsize = 10)

# Create bar graph
bar.set_title("Vehicles Available in Households", fontsize = 12)
bar.set_xlabel("# of Vehicles", fontsize = 10)
bar.set_ylabel("Thousands of Households", fontsize = 10)
bar.tick_params(labelsize = 10)
bar.set_xlim([-.5, 6.5])
car_hh = data.groupby("VEH")["WGTP"].sum()/1000
bar.bar(car_hh.index, car_hh.values, color = "red")
    
# Create scatter plot setup 
scatter.set_title("Property Taxes vs. Property Values", fontsize = 12)
plt.xlabel("Property Value ($)", fontsize = 10)
plt.ylabel("Taxes ($)", fontsize = 10)
scatter.set_xlim([0, 1200000])
scatter.set_ylim([0, 10500])
scatter.tick_params(labelsize = 10)

# Reference of taxp to actual, lower bound interval
taxp_ref = {1: 0, 2: 1}
counter = 0
for key in range(3, 23):
    counter += 50
    taxp_ref[key] = counter
for key in range(23, 63):
    counter += 100
    taxp_ref[key] = counter
for key in range(63, 65):
    counter += 500
    taxp_ref[key] = counter
for key in range(65, 69):
    counter += 1000
    taxp_ref[key] = counter

# Convert TAXP into appropriate numeric value, based on ref
taxp_conv = []
for key in data["TAXP"]:
    if taxp_ref.has_key(key):
        taxp_conv.append(taxp_ref[key])
    else:
        taxp_conv.append(np.NaN)

# Create scatter plot graphing with colorbar        
mappable = scatter.scatter(data["VALP"], taxp_conv, s = data["WGTP"], c = data["MRGP"], cmap = "seismic", alpha = 0.18)

# Create colorbar
colorbar = fig.colorbar(mappable, ticks = [1250, 2500, 3750, 5000])
colorbar.set_label("First Mortgage Payment (Monthly $)", fontsize = 10)

# Save the figure
dpi = fig.get_dpi()
plt.savefig("pums.png", dpi=dpi*2)

# Display the figure
plt.show()
