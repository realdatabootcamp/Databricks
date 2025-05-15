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

# Key Questions for ETL: First Load vs. Incremental Load  

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

## 3. Final Considerations  
- Should we implement **Delta Lake for ACID compliance** in data lakes?  
- How do we ensure **ETL pipelines remain scalable** as data volumes grow?  
- What **performance benchmarks** should we track over time?  

This structured approach ensures **consistent, efficient, and scalable data processing** for both **full and incremental ETL loads**. 🚀  
