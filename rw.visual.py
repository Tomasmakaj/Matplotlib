import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk

rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()


# Generate Multiple Random Walks

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
# This code generates a random walk and displays it. When you close the viewer you'll be asked whether you want to generate another walk
# Press y to generate walks that start near the starting point