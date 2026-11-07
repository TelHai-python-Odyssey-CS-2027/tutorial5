# Q: Write an import statement that imports the function pyplot from the module matplotlib and renames it to plt.


def build_histogram(data):
    pass  # Replace the `pass` with your code


def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel("Items")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()
