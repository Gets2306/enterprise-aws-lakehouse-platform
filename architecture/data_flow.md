# Detailed Data Flow

Batch Sources
    ↓
NiFi Cluster
    ↓
S3 Raw Zone

Streaming Source
    ↓
API Gateway
    ↓
Lambda
    ↓
DynamoDB
    ↓
S3 Raw Zone

S3 Raw
    ↓
Glue Bronze
    ↓
Partitioned Bronze
    ↓
Glue Silver
    ↓
Daily Classification
    ↓
Open / Non-Open Zones
    ↓
Hive Query Layer