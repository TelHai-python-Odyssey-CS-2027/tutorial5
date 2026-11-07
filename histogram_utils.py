# Q: Write an import statement that imports pyplot from matplotlib and renames it to plt.


def build_histogram(data):
    """Return a dict mapping each distinct value in data to its count.

    Example: [1, 2, 2, 3] -> {1: 1, 2: 2, 3: 1}
    """
    pass  # Replace the pass with your code


def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel("Items")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()
