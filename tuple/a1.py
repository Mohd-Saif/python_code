from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("Querying Data") \
    .getOrCreate()

# Read data into DataFrame
df = spark.read.csv("data.csv", header=True)

# Selecting specific columns and filtering rows
result = df.select("name", "age", "city").filter(df["age"] > 30)

# Show the result
result.show()