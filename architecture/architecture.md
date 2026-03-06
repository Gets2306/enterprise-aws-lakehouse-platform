# Architecture Overview

## Ingestion Layer

Apache NiFi deployed on EC2 cluster.
ZooKeeper manages cluster coordination and node failover.

Handles:
- Database extraction
- Flat files
- Excel documents
- Salesforce data
- Semi-structured JSON
- Unstructured payloads

## Streaming Layer

Custom Application → API Gateway → Lambda → DynamoDB → S3 Raw Zone

## Processing Layer

AWS Glue ETL:

Bronze Layer:
- Raw ingestion validation
- Partition by ingestion_date

Silver Layer:
- Deduplication
- Cleansing

Daily Classification:
- Segregation into Open / Non-Open zones

## Storage Layer

S3 used as data lake (HDFS equivalent).
Partitioning by:
- ingestion_date
- source_system
- table_name

## Query Layer

Hive external tables built on S3 partitions.