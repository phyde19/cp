import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Example translation CSV data
data = {
    'old_table': ['old_table1', 'old_table1', 'old_table2', 'old_table3'],
    'old_column': ['col1', 'col2', 'col3', 'col4'],
    'new_table': ['new_table1', 'new_table2', 'new_table1', 'new_table3'],
    'new_column': ['colA', 'colB', 'colC', 'colD']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Get unique old and new tables
old_tables = df['old_table'].unique()
new_tables = df['new_table'].unique()

# Create an empty DataFrame with old tables as rows and new tables as columns
matrix = pd.DataFrame('', index=old_tables, columns=new_tables)

# Populate the matrix with column translations
for _, row in df.iterrows():
    old_table = row['old_table']
    new_table = row['new_table']
    translation = f"{row['old_column']} -> {row['new_column']}"
    if matrix.at[old_table, new_table]:
        matrix.at[old_table, new_table] += f", {translation}"
    else:
        matrix.at[old_table, new_table] = translation

# Add an empty top-left corner
matrix.columns.name = 'New Tables'
matrix.index.name = 'Old Tables'

# Plot the matrix
fig, ax = plt.subplots(figsize=(10, 8))

# Hide the axes
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Draw the table
table = plt.table(cellText=matrix.values, rowLabels=matrix.index, colLabels=matrix.columns, cellLoc='center', loc='center', colColours=['lightgray']*len(new_tables), rowColours=['lightgray']*len(old_tables))

# Adjust layout
table.scale(1.2, 1.2)
table.auto_set_font_size(False)
table.set_fontsize(10)

# Add title
plt.title('Table and Column Translation Matrix', fontsize=14)

plt.show()
