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

# Plotting a Series of Points with scatter()

# To plot a series of points, we can pass scatter() separate lists of x- and y- values, like this:

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# Calculating Data Automatically
# Writing lists by hand can be inefficient, especially when we have many points.
# Rather than passing our points in a list, lets use a loop in Python to do the calculations of us
# Here's how this would look with 1000 points:

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()


# Using a colormap 
# A colormap is a series of colors in a gradient that moves from a starting to ending color. 
# You use colormaps in visualizations to emphasize a a pattern in the data. For example you might make low values a light color & high values a darker color

# The pyplot module includes a set of built-in colormaps. To use one of these colormaps, you need to specify how pyplot should assign a color to each point in the data set.
# Here is how to assign point a color based on its Y Value

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()
