import pandas as pd
import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column):
        """Plot a histogram of a column"""
        if column in self.data.columns:
            self.data[column].hist(bins=20, edgecolor='black')
            plt.title(f"Histogram of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.show()
        else:
            print(f"Column '{column}' not found.")

    def plot_line(self, column):
        """Plot a line chart of a column"""
        if column in self.data.columns:
            self.data[column].plot(kind='line')
            plt.title(f"Line Plot of {column}")
            plt.xlabel("Index")
            plt.ylabel(column)
            plt.show()
        else:
            print(f"Column '{column}' not found.")


class CSVAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.columns = []

    def load_csv(self):
        """Load a CSV file"""
        try:
            self.data = pd.read_csv(self.filename)
            self.columns = self.data.columns.tolist()
            print(f"File {self.filename} loaded successfully.")
            print("Columns:", self.columns)
        except Exception as e:
            print("Error loading file:", e)

    def calculate_mean(self, column):
        """Calculate the mean of a column"""
        if self.data is not None and column in self.data.columns:
            return self.data[column].mean()
        else:
            print("Data not loaded or invalid column.")
            return None

    def summary(self):
        """Statistical summary of the data"""
        if self.data is not None:
            print(self.data.describe())
        else:
            print("Please load the file first.")

    def plot_column(self, column, plot_type="histogram"):
        """Plot a column using Visualizer"""
        if self.data is not None:
            viz = Visualizer(self.data)
            if plot_type == "histogram":
                viz.plot_histogram(column)
            elif plot_type == "line":
                viz.plot_line(column)
            else:
                print("Invalid plot type.")
        else:
            print("Please load the file first.")


# --- Example run ---
if __name__ == "__main__":
    analyzer = CSVAnalyzer("sample.csv")  # Put your CSV filename here
    analyzer.load_csv()
    analyzer.summary()
    mean_value = analyzer.calculate_mean("Age")  # Example column
    print("Mean Age:", mean_value)
    analyzer.plot_column("Age", plot_type="histogram")

