# Enterprise AWS Lakehouse Platform

Enterprise-scale multi-source data lake architecture handling:

- 8 heterogeneous source systems
- 230+ tables
- Structured, semi-structured, unstructured data
- Batch + Streaming ingestion
- Salesforce (SFSC & SFMC)
- Custom application streaming
- Daily Open / Non-Open data classification
- Hive query enablement

---

# High-Level Architecture

Sources → NiFi Cluster (EC2 + ZooKeeper)
Streaming → API Gateway → Lambda → DynamoDB → S3
Glue → Bronze → Silver → Daily Classification
Storage → Partitioned S3
Query → Hive Metastore

---

# Tech Stack

Apache NiFi  
ZooKeeper  
AWS Glue  
Amazon S3  
AWS Lambda  
API Gateway  
DynamoDB  
Hive Metastore  
EC2  

---

# Key Engineering Capabilities

✔ Multi-source ingestion  
✔ Streaming + Batch unification  
✔ 230+ table onboarding  
✔ Daily partition-based processing  
✔ Open vs Non-Open storage segregation  
✔ Hive query exposure  
✔ Enterprise-scale ingestion framework  

---

# Portfolio Objective

Demonstrates advanced enterprise data engineering architecture for large-scale lakehouse environments.
