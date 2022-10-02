# The following snippet is a library function that might be installed on a Databricks cluster. It is a simple function that adds a new column, populated by a literal, to an Apache Spark DataFrame.
# addcol.py
import pyspark.sql.functions as F

def with_status(df):
    return df.withColumn("status", F.lit("checked"))