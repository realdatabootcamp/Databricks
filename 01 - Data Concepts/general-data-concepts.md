# General Data Concepts  

Understanding fundamental **data concepts** is essential for data engineering, analytics, and machine learning.  

## 1. Data Types  
- **Structured Data** – Organized in databases with rows & columns (e.g., SQL tables).  
- **Unstructured Data** – Freeform content like images, videos, and raw text.  
- **Semi-structured Data** – Hybrid format like JSON & XML with partial structure.  

## 2. Data Storage & Management  
- **Databases** – Structured storage (Relational: MySQL, PostgreSQL; NoSQL: MongoDB, DynamoDB).  
- **Data Lakes** – Store large raw datasets (Azure Data Lake, AWS S3).  
- **Data Warehouses** – Optimized for reporting & analytics (Azure Synapse, Snowflake).  
- **Delta Lake** – Enables **ACID transactions** on data lakes for consistency.  

## 3. Data Processing & Transformation  
- **ETL (Extract, Transform, Load)** – Cleans and moves data from source to destination.  
- **Batch Processing** – Handles large volumes periodically (Apache Spark, Hadoop).  
- **Stream Processing** – Processes real-time data flows (Kafka, Spark Streaming).  
- **Data Wrangling** – Cleans and reshapes data for usability.  

## 4. Data Quality & Governance  
- **Data Cleaning** – Removes errors, duplicates, and inconsistencies.  
- **Data Lineage** – Tracks data origins and transformation history.  
- **Data Security** – Protects sensitive information via encryption & access controls.  
- **Data Governance** – Policies ensuring compliance, integrity, and accessibility.  

## 5. Data Analytics & Visualization  
- **Descriptive Analytics** – Summarizes past trends from data.  
- **Predictive Analytics** – Uses **machine learning** for forecasting outcomes.  
- **Prescriptive Analytics** – Recommends actions based on data insights.  
- **Business Intelligence (BI)** – Dashboards and reporting tools (Power BI, Tableau).  

## 6. Data Architecture Approaches  
- **Medallion Architecture** – Bronze (raw), Silver (cleaned), Gold (aggregated).  
- **Star & Snowflake Schemas** – Optimized for data warehouse queries.  
- **Data Mesh** – Decentralized data ownership for scalable systems.  
- **Lambda Architecture** – Combines batch and real-time data processing.  
