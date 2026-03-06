silver_df = spark.read.parquet("s3://enterprise-silver-zone/")

open_df = silver_df.filter("status = 'OPEN'")
nonopen_df = silver_df.filter("status != 'OPEN'")

open_df.write.mode("overwrite").parquet("s3://enterprise-open-zone/")
nonopen_df.write.mode("overwrite").parquet("s3://enterprise-nonopen-zone/")