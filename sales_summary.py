import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Connect to or create the SQLite database
db_file = 'sales_data.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# 2. Create the sales table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# 3. Insert sample data (skip if already present)
cursor.execute("SELECT COUNT(*) FROM sales")
if cursor.fetchone()[0] == 0:
    sample_data = [
        ('Pen', 10, 5.0),
        ('Notebook', 5, 20.0),
        ('Pencil', 15, 2.0),
        ('Eraser', 20, 1.0),
        ('Marker', 7, 10.0)
    ]
    cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
    conn.commit()

# 4. Query to get total quantity and revenue per product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# 5. Load query results into pandas DataFrame
df = pd.read_sql_query(query, conn)

# 6. Print the results
print("📦 Sales Summary:")
print(df)

# 7. Plot the revenue as a bar chart
plt.figure(figsize=(8, 5))
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("💰 Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Save the chart
plt.show()

# 8. Close the connection
conn.close()
