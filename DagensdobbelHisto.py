import pyodbc
import matplotlib.pyplot as plt

# Connect to the database
cnxn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-0CMQN56;"
    "Database=Trav;"
    "Trusted_Connection=yes;"
)

# Create a cursor
cursor = cnxn.cursor()

# Execute a query
query = "SELECT Baneid FROM [Trav].[dbo].[Dagensdobbel]"
cursor.execute(query)

# Fetch all the rows
data = cursor.fetchall()
datadec=data[0]
lengdedata = len(data)
print(lengdedata,"Lengde data")

# Create a histogram
plt.hist(data)
plt.show()
