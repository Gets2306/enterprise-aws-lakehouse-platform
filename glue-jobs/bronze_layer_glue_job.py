from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

raw_df = spark.read.json("s3://enterprise-raw-zone/")

raw_df.write.mode("append") \
    .partitionBy("ingestion_date") \
    .parquet("s3://enterprise-bronze-zone/")