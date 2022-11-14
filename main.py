import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()

# We first import the pyplot module using teh alias plt so we dont have to type pyplot repeatedly.
# subplots() function. This function can generate one or more plots in the same figure. 
# The variable fig represents the entire figure or collection of plots that are generated.
# The variable ax represents a single plot in the figure and is the variable well use most of the time.
# We then use the plot method which will try to plot the data its given in a meaningful way.
# The function plt.show() opens Matplotlib viewer and displays the plot

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()


# The linewidth parameter controlc thickness of the line that plot() generates.
# The set_title method at sets a title for the chart. 
# The fontsize parameters which appear repeatedly thorughout the code, control the size of the text in various elements on the chart.
# The set_xlabel() and set_ylabel() methods allow you to set a title for each of the axes and the method tick_params() styles the tick marks.

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()


# The new graph will plot the graph correctly because we providded input and output values

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)


# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()