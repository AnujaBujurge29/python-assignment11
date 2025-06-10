import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect('../db/lesson.db')

# 1.1: SQL query to get employee revenue data

query = """
SELECT last_name, SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id
"""

# Load data into DataFrame
employee_results = pd.read_sql_query(query, conn)

# 1.3  Create bar chart


bar_plot = employee_results.plot(
    kind='bar',
    x='last_name',
    y='revenue',
    color='skyblue',
    edgecolor='black',
)

# 1.4 Customize the plot
# plt.figure(num='Employee Revenue Analysis')

plt.title('Employee Revenue Performance', pad=20, size=14)
plt.xlabel('Employee Last Name', size=12)
plt.ylabel('Revenue ($)', size=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of each bar
for i, v in enumerate(employee_results['revenue']):
    plt.text(i, v, f'${v:,.0f}', ha='center', va='bottom')

# # Adjust layout to prevent label cutoff
# plt.tight_layout()

# 1.5 Show plot
plt.show()
#
# Close connection
conn.close()
