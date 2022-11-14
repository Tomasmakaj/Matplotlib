# Plotting and Styling Individual Points with scatter()

# Sometimes its useful to play and style individual points based on certain characteristics.
# You might plot small values in one color and larger values in another color
# You can plot a large data set with one set of styling options and then emphasize individaul points
# To plot a single point use the scatter() method. 
# Pass the single (x, y) values of the point of interest to scatter() to plot those values:


import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4)

plt.show()

# Style the output to make it more interesting. We will add a title, label the axes and make sure all the text is large enough to read

import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

