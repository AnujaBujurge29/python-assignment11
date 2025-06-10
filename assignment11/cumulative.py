import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect('../db/lesson.db')

# 2.1 QL query to get order totals
query = """
SELECT o.order_id, SUM(p.price * l.quantity) as total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

# Create DataFrame
df = pd.read_sql_query(query, conn)

# 2.2 Add cumulative column using cumsum()
df['cumulative'] = df['total_price'].cumsum()

# 2.3 Create line plot
df.plot(
    kind='line',
    # kind='scatter',
    x='order_id',
    y='cumulative',
    color='blue',
    marker='.',
    markeredgecolor='red'  # Adds black edge to dots
    # markersize=4
)

# Customize plot
plt.title('Cumulative Revenue by Order', pad=20, size=14)
plt.xlabel('Order ID', size=12)
plt.ylabel('Cumulative Revenue ($)', size=12)
plt.grid(True, linestyle='-', alpha=0.7)

# Format y-axis labels as currency
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['${:,.0f}'.format(x) for x in current_values])

# 2.4 Adjust layout and display
plt.show()

# Close connection
conn.close()
