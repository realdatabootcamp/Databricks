# Databricks notebook source
# MAGIC %md
# MAGIC ## 1 Generate Synthetic Data - Bronze Layer
# MAGIC

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DecimalType, TimestampType
import random
import datetime
from decimal import Decimal

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("DeltaLake Bronze Layer - Improved Names") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Define schema
schema = StructType([
    StructField("CustomerName", StringType(), True),
    StructField("ProductName", StringType(), True),
    StructField("TransactionDate", TimestampType(), False),
    StructField("Quantity", StringType(), False),
    StructField("Price", DecimalType(10,2), False),
    StructField("TotalAmount", DecimalType(10,2), False)
])

# Product names
product_names = [
    "SmartEcho Wireless Earbuds", "QuantumX Gaming Laptop", "VoltCharge Power Bank",
    "ArcticShield Winter Jacket", "Skyline Flex Sneakers", "UrbanWeave Denim Jeans",
    "PureBrew Coffee Maker", "BreezeFlow Air Purifier", "UltraSoft Memory Foam Pillow",
    "TitanGrip Adjustable Dumbbells", "HydroFuel Sports Bottle", "ZenTrack Smart Fitness Watch"
]

# Customer names
customer_names = [
    "Alice Johnson", "Michael Smith", "Sophia Brown", "Daniel Martinez", "Olivia Taylor",
    "Ethan White", "Emma Gonzalez", "Liam Hernandez", "Ava Thompson", "Noah Clark",
    "Isabella Lopez", "James Rodriguez", "Charlotte Lewis", "William Walker", "Amelia Hall"
]

# Generate synthetic raw data
data = []
for _ in range(100):  # Generating 100 rows
    customer_name = random.choice(customer_names)  # Selecting better customer names
    product_name = random.choice(product_names)  # Selecting better product names
    transaction_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
    quantity = random.randint(1, 5)
    price = Decimal(str(round(random.uniform(10, 100), 2)))
    total_amount = Decimal(str(quantity * price))

    data.append((customer_name, product_name, transaction_date, str(quantity), price, total_amount))

# Create DataFrame
df = spark.createDataFrame(data, schema=schema)

# Save to Delta Lake (Bronze Layer)
delta_path = "dbfs:/mnt/bronze/raw_transactions"
df.write.format("delta").mode("overwrite").save(delta_path)

# Read and verify saved data
df_read = spark.read.format("delta").load(delta_path)
df_read.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2 Build Silver Layer
# MAGIC

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import row_number, monotonically_increasing_id
from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DecimalType, TimestampType

# Read Raw Bronze Data
bronze_path = "dbfs:/mnt/bronze/raw_transactions"
df_raw = spark.read.format("delta").load(bronze_path)

# Deduplicate Customer Data
customer_df = df_raw.select("CustomerName").distinct() \
    .withColumn("CustomerID", monotonically_increasing_id())  # Generate unique IDs

# Deduplicate Product Data
product_df = df_raw.select("ProductName").distinct() \
    .withColumn("ProductID", monotonically_increasing_id())  # Generate unique IDs

# Normalize Transactions Data
transactions_df = df_raw.join(customer_df, "CustomerName", "left") \
                        .join(product_df, "ProductName", "left") \
                        .select("CustomerID", "ProductID", "TransactionDate", "Quantity", "Price", "TotalAmount") \
                        .withColumn("TransactionID", monotonically_increasing_id())  # Generate unique Transaction IDs

# Define Silver Table Paths
silver_customer_path = "dbfs:/mnt/silver/customers"
silver_product_path = "dbfs:/mnt/silver/products"
silver_transactions_path = "dbfs:/mnt/silver/transactions"

# Write to Delta Lake (Silver Layer)
customer_df.write.format("delta").mode("overwrite").save(silver_customer_path)
product_df.write.format("delta").mode("overwrite").save(silver_product_path)
transactions_df.write.format("delta").mode("overwrite").save(silver_transactions_path)

# Verify Data Saved
spark.read.format("delta").load(silver_customer_path).show()
spark.read.format("delta").load(silver_product_path).show()
spark.read.format("delta").load(silver_transactions_path).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3 Build Gold
# MAGIC
# MAGIC

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, month, year
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DecimalType, TimestampType

# Read Transaction Data from Silver Layer
silver_transactions_path = "dbfs:/mnt/silver/transactions"
transactions_df = spark.read.format("delta").load(silver_transactions_path)

# Aggregate Sales per Month
sales_report_df = transactions_df \
    .groupBy(year("TransactionDate").alias("Year"), month("TransactionDate").alias("Month")) \
    .agg(sum("TotalAmount").alias("TotalSales")) \
    .orderBy("Year", "Month")

# Define Gold Table Path
gold_sales_report_path = "dbfs:/mnt/gold/sales_per_month"

# Write to Delta Lake (Gold Layer)
sales_report_df.write.format("delta").mode("overwrite").save(gold_sales_report_path)

# Verify Data Saved
spark.read.format("delta").load(gold_sales_report_path).show()