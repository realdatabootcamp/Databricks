## Project: Generate Sales Report
### Requirements
Build a report that shows total sales by month and year
### Technical Requirements
- Use Databricks medallion architecture
- Use raw transactions data in bronze layer
- Build data model for customer, product and transactions in silver
- Build aggregated data (sales report) in gold layer
### Environment Setup
- Get Databricks Community Edition (Free)
- [Link](https://login.databricks.com/?dbx_source=CE&intent=CE_SIGN_UP) to sign-up for Databricks Community Edition
### Create a cluster (compute)
- Choose the latest Databricks runtime version available
- Rename cluster name by clicking the pencil (optional)
![image](https://github.com/user-attachments/assets/3a15c570-c19c-4c95-acac-c6b4d7688c4c)
### Create Notebook
![image](https://github.com/user-attachments/assets/584f870d-baba-4d47-a604-a977a0320025)
- Attach notebook to the cluster created
- Rename notebook to align to its purpose
![image](https://github.com/user-attachments/assets/86b0faaf-0d51-4003-8483-a843d970fe8f)
### Write Code in Notebook
- Full code available [here](https://github.com/realdatabootcamp/Databricks/blob/main/04%20Projects/Sales/generate-sales-report.py)
![image](https://github.com/user-attachments/assets/0d6cfd51-dfd8-4155-9991-203a08cbc934)

# Now that you have built your report, below are some Key Questions for ETL (Extract Transform and Loading data): First Load vs. Incremental Load (Ongoing) 

Understanding **first load vs. incremental load** in ETL processes is crucial for maintaining **data integrity, efficiency, and performance**. Below are essential questions to consider during each phase.

---

## 1. Questions for First Load (Initial Full Load)  

### ✅ Data Scope & Completeness  
- What is the **total volume** of data being ingested?  
- Are all **historical records** required, or should we filter specific date ranges?  
- How do we **verify data completeness** post-load?  

### ✅ Data Quality & Integrity  
- What **data validation rules** need to be enforced?  
- Are there any missing or corrupt records in the source system?  
- How do we handle **duplicate entries** or inconsistent formats?  

### ✅ Performance & Scalability  
- What is the expected **execution time** for the first load?  
- Are there any **system constraints** (memory, processing limits)?  
- Should we **partition large datasets** for better performance?  

### ✅ Error Handling & Recovery  
- How do we recover from failures during the **initial data migration**?  
- Are there **retry mechanisms** in place for handling failures?  
- How do we track **load progress and audit logs**?  

### ✅ Schema & Metadata Management  
- Are there any **schema changes** expected in future loads?  
- How do we manage **data lineage and metadata tracking**?  

---

## 2. Questions for Incremental Load (Ongoing Data Refresh)  

### ✅ Change Data Capture (CDC) Strategy  
- How do we identify **new, updated, or deleted records** in the source?  
- What is the **change detection mechanism** (timestamps, flags, CDC logs)?  
- Are there **soft deletes or hard deletes**, and how should they be processed?  

### ✅ Data Merge & Conflict Resolution  
- How should **conflicting updates** (e.g., duplicate primary keys) be handled?  
- What happens when a previously loaded record is **modified or deleted**?  
- Should updates be **merged in-place or appended** to maintain history?  

### ✅ Performance Optimization  
- How frequently should incremental loads be **scheduled**?  
- Do we need **indexing or partitioning strategies** for optimized queries?  
- Should we use **batch processing or real-time streaming** for updates?  

### ✅ Monitoring & Logging  
- What alerts should be triggered for **failed incremental loads**?  
- How do we track **incremental changes** across multiple ETL runs?  
- Is there a **checkpoint mechanism** to resume loads after failures?  

### ✅ Data Validation Post-Load  
- How do we compare **incrementally loaded data** with previous snapshots?  
- Are there **automated validation tests** for consistency?  
- How do we maintain **audit trails** for historical tracking?  

---
# ETL Load Types & Procedure  

ETL (Extract, Transform, Load) processes involve different load types based on **initial data ingestion, updates, and real-time streaming**. The procedure ensures **data integrity, efficiency, and scalability** for analytics and reporting.

---

## 1. Load Types in ETL  

### 🔹 Full Load (Initial Load)  
- **Definition:** Loads the entire dataset into the target system for the first time.  
- **Use Case:** Setting up a **new data warehouse or database**.  
- **Procedure:**  
  1. **Extract** all available data from the source.  
  2. **Transform** data by cleaning, standardizing, and structuring it.  
  3. **Load** the entire dataset into the target storage (e.g., Azure Data Lake, Snowflake).  
- **Challenges:** Large data volumes require **partitioning and indexing** for optimal performance.  

### 🔹 Incremental Load  
- **Definition:** Loads only **new or updated** records instead of refreshing the entire dataset.  
- **Use Case:** Periodic updates for **operational reporting**.  
- **Procedure:**  
  1. Identify **new or changed records** using timestamps or Change Data Capture (CDC).  
  2. Extract only the **modified data**.  
  3. Merge new records into the target system (**UPSERT method**).  
- **Methods:** Append-only load, CDC tracking, or Merge (Upsert).  

### 🔹 Batch Load  
- **Definition:** Loads data in **chunks** on a predefined schedule.  
- **Use Case:** Periodic ETL jobs in **data lakes and reporting systems**.  
- **Procedure:**  
  1. Extract data in **predefined batches** (e.g., hourly, daily).  
  2. Process data transformations **in stages**.  
  3. Store processed data in the **structured database**.  
- **Optimization:** Parallel processing improves batch load efficiency.  

### 🔹 Streaming Load (Real-Time Processing)  
- **Definition:** Continuously ingests **live data streams** for real-time analytics.  
- **Use Case:** IoT telemetry, fraud detection, and transactional updates.  
- **Procedure:**  
  1. Capture streaming data using **Kafka, Azure Event Hub, or AWS Kinesis**.  
  2. Apply transformations in **real-time via Spark Streaming**.  
  3. Load directly into **Delta Lake or real-time databases**.  
- **Optimization:** Uses event-driven architecture for **low-latency data processing**.  

### 🔹 Delta Load  
- **Definition:** Loads only the **differences** between source and target datasets.  
- **Use Case:** Efficient updates for **Delta Lake and slowly changing dimensions (SCD)**.  
- **Procedure:**  
  1. Identify **changed records** by comparing timestamps or checksums.  
  2. Extract only **modified rows**.  
  3. Merge with existing data in **Delta format**.  
- **Optimization:** Delta Lake maintains **ACID transactions** for scalable updates.  

### 🔹 Historical Load  
- **Definition:** Loads archived historical data separately from **current operational datasets**.  
- **Use Case:** Compliance audits, retrospective analytics, or machine learning training.  
- **Procedure:**  
  1. Extract archived data from **backup sources**.  
  2. Store in a **historical partition or separate table**.  
  3. Enable **time-travel queries** for analytics.  
- **Optimization:** Stored separately to prevent interference with **active datasets**.  

---

## 2. General ETL Load Procedure  

Regardless of load type, the **ETL workflow** follows these core steps:

1️⃣ **Extraction** – Retrieve data from **source databases, APIs, files, or streams**.  
2️⃣ **Transformation** – Apply cleaning, standardization, deduplication, and enrichment.  
3️⃣ **Loading** – Move processed data into the **target system (SQL warehouse, data lake, or BI platform)**.  
4️⃣ **Validation & Monitoring** – Ensure data quality using **audit logs, checksums, and alerts**.  
5️⃣ **Optimization** – Improve query performance via **indexing, partitioning, and caching**.  

---

## 3. Final Considerations  

Different ETL load types ensure **optimized, scalable, and accurate** data processing. 🚀  
Would you like a **detailed example of Delta Load implementation in Databricks?**  
## 3. Final Considerations  
- Should we implement **Delta Lake for ACID compliance** in data lakes?  
- How do we ensure **ETL pipelines remain scalable** as data volumes grow?  
- What **performance benchmarks** should we track over time?  

This structured approach ensures **consistent, efficient, and scalable data processing** for both **full and incremental ETL loads**. 🚀  
