bronze_df = spark.read.parquet("s3://enterprise-bronze-zone/")

clean_df = bronze_df.dropDuplicates()

clean_df.write.mode("overwrite") \
    .partitionBy("ingestion_date") \
    .parquet("s3://enterprise-silver-zone/")