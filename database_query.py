# Write a query that will display the results below (Note: some columns might be renamed
# but use the column names above). It should only show 2020 data and order by driver
# points.

# to get a normal sql querry to work in python like in the one above
import sqlite3
import pandas as pd

# Database connection
connection = sqlite3.connect("races.db")

# CRaft query
query = """
SELECT 
    circuits.location AS circuit_location,
    results.grid,
    drivers.number AS driver_number,
    results.fastestLap AS fastest_lap,
    results.points,
    drivers.name AS driver_name,
    races.name AS race_name,
    results.time AS race_time,
    races.year AS race_year,
    constructors.name AS team,
    races.date AS race_date
FROM 
    results
JOIN 
    races ON results.raceId = races.raceId
JOIN 
    drivers ON results.driverId = drivers.driverId
JOIN 
    constructors ON results.constructorId = constructors.constructorId
JOIN 
    circuits ON races.circuitId = circuits.circuitId
WHERE 
    races.year = 2020
ORDER BY 
    results.points DESC;
"""
# dataframe
df = pd.read_sql_query(query, connection)

connection.close()

print(df)
