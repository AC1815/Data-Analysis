'''
import pyodbc


# Define your connection string using a raw string
conn_string = r"Driver={SQL Server};Server=DESKTOP-U4JA4I7\SQLEXPRESS;Database=ayush;Trusted_Connection=yes;"

# Connect to SQL Server

conn = pyodbc.connect(conn_string)
print("Connection successful!")
print(conn)

# Create a cursor object using the connection
cursor = conn.cursor()

# Example query: Fetch all tables
cursor.execute("SELECT * FROM EMPLOYEE")
tables = cursor.fetchall()

for table in tables:
    print(table)  # Print each table name
'''



'''
import pandas as pd


SEOAudit = pd.read_csv("list.csv")
#print(SEOAudit)


print(SEOAudit.columns)

'''


import pandas as pd
'''
# Load the original CSV file
input_file = 'list.csv'  # Replace with your file path
df = pd.read_csv(input_file)

# Filter the DataFrame based on the condition
filtered_df = df[df['Title 1 Length'] > 60]

# Select only the required columns
output_df = filtered_df[['Address', 'Title 1', 'Title 1 Length']]

# Save the filtered DataFrame to a new CSV file
output_file = 'filtered_output.csv'  # Specify the output file name
output_df.to_csv(output_file, index=False)
print("Filtered data saved to", output_file)
'''

#Load the original CSV file
df = pd.read_csv("list.csv")
print(df)

#Filter the required data
filter=df[df['Meta Description 1 Length']>160]

Description=filter[['Address','Meta Description 1','Meta Description 1 Length']]
Description.to_csv("Descriptionabove160.csv",index=False)







