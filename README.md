# 📊 Task 7: Basic Sales Summary using SQLite & Python

## 📌 Objective
Use SQL inside Python to generate a basic sales summary — total quantity and revenue per product — and visualize it using a bar chart.

## 🛠 Tools Used
- Python
- SQLite (`sqlite3`)
- pandas
- matplotlib

## 📂 Dataset
A simple SQLite database (`sales_data.db`) with one table: `sales`

## ⚙️ What the Script Does
- Connects to `sales_data.db`
- Creates a table and inserts sample sales data (if needed)
- Runs a query to calculate total quantity sold and revenue
- Loads the result into pandas
- Prints the summary
- Displays a revenue bar chart and saves it as `sales_chart.png`

## 📈 Output Example

| product  | total_qty | revenue |
|----------|-----------|---------|
| Pen      | 10        | 50.0    |
| Notebook | 5         | 100.0   |
| Pencil   | 15        | 30.0    |
| Eraser   | 20        | 20.0    |
| Marker   | 7         | 70.0    |

## 💡 Learning Outcome
- Writing SQL queries inside Python
- Using pandas for SQL data manipulation
- Creating simple bar charts with matplotlib
