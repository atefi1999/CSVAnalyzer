# 📊 CSV Analyzer & Visualizer

A simple yet powerful tool to **analyze CSV files** and **visualize data** using Python, Pandas, and Matplotlib.  

---

## 🚀 Features
- 📂 Load CSV files and display available columns  
- 📈 Calculate the **mean** of any numeric column  
- 📊 Generate a statistical summary (count, mean, std, min, max, etc.)  
- 🔍 Visualize data with different chart types:
  - Histogram  
  - Line Plot  

---

## 🛠️ Requirements
Make sure you have Python installed with the following libraries:

```bash
pip install pandas matplotlib
```



▶️ Usage Example

from csv_analyzer import CSVAnalyzer

# Create analyzer object
analyzer = CSVAnalyzer("sample.csv")  # Replace with your CSV file

# Load data
analyzer.load_csv()

# Show summary statistics
analyzer.summary()

# Calculate mean of a column (example: Age)
mean_value = analyzer.calculate_mean("Age")
print("Mean Age:", mean_value)

# Plot histogram of Age column
analyzer.plot_column("Age", plot_type="histogram")

# Plot line chart of Age column
analyzer.plot_column("Age", plot_type="line")




📊 Example Output

Statistical summary of numeric columns

Histogram of selected column

Line chart of selected column



📂 Project Structure

.
├── csv_analyzer.py    # Main code file
├── sample.csv         # Example dataset
└── README.md          # Project documentation



