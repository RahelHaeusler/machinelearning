# This program displays a sales chart

import matplotlib.pyplot as plt


def main():
    # Create a list with the X coordinates of each bar's left edge.
    left_edges = [0, 10, 20, 30, 40]

    # Create a list with the heights of each bar.
    heights = [100, 200, 300, 400, 500]

    # Create a variable for the bar width.
    bar_width = 10

    # Build the bar chart.
    plt.bar(left_edges, heights, bar_width, color=('b', 'b', 'b', 'b', 'b'))

    # Add a title.
    plt.title('Salary Overview')

    # Add labels to the axes.
    plt.xlabel('Name')
    plt.ylabel('Salary')



# Call the main function.
if __name__ == '__main__':
    main()

