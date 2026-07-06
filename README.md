# 🧠 (KGB) AI Knowledge Graph Builder for Enterprise Intelligence
### **Developed as part of the Infosys Springboard Internship** 
### **Authors:** PUNIT KUMAR
<a href="https://kgb-12g3.onrender.com/"><img src="https://img.shields.io/badge/🔴_Live_Demo-00D4AA?style=for-the-badge&logoColor=white" alt="Live Demo"/></a>
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)]()
[![Neo4j](https://img.shields.io/badge/Neo4j_Aura_Cloud-018bff?style=for-the-badge&logo=neo4j&logoColor=white)]()
[![Groq](https://img.shields.io/badge/Groq_API-f55036?style=for-the-badge&logo=groq&logoColor=white)]()
[![Llama 3.1](https://img.shields.io/badge/Llama_3.1-0467df?style=for-the-badge&logo=meta&logoColor=white)]()
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)]()

----

# 📖 Project Overview

This project builds an enterprise-level **AI-powered Knowledge Graph system** from structured and unstructured customer support data. 

The system extracts entities and relationships from support tickets, constructs a **dynamic knowledge graph**, and enables **intelligent semantic search with a Retrieval-Augmented Generation (RAG) pipeline**. By moving completely to the cloud, it provides high-speed automated troubleshooting responses via an interactive graph dashboard.

---

# 🎯 Objective

To transform enterprise support ticket data into a scalable, cloud-native knowledge graph that enables:

- **Relationship-based analysis** to uncover hidden connections.
- **Intelligent troubleshooting** driven by high-speed LLM inference.
- **Semantic search** over vast amounts of support tickets.
- **AI-assisted IT support responses** for actionable intelligence.

---

# 🏗 Project Architecture (Cloud-Native)

> *The journey of a support ticket from raw data to an interactive neural graph.*

```text
Raw Dataset  
      ↓
Data Cleaning (Pandas)
      ↓
Structured Triple Extraction
      ↓
LLM-based Entity Extraction 
      ↓
Merge Structured + LLM Triples
      ↓
Neo4j Graph Construction (AuraDB Cloud)
      ↓
Embedding Generation (Hybrid: Local PyTorch OR Serverless Hugging Face API)
      ↓
Vector Database (FAISS)
      ↓
Semantic Search
      ↓
Retrieval-Augmented Generation (Groq API + Llama 3.1)
```

---

# 🚀 Technologies Used

- **Python & Pandas** (Data Processing)
- **Sentence Transformers & FAISS** (Vector Database & Embeddings)
- **Hugging Face Inference API** (Serverless Embedding for Cloud Deployment)
- **Groq API / Llama 3.1** (High-Speed Cloud LLM for Intelligent Assistant)
- **Neo4j AuraDB** (Cloud Graph Database)
- **Flask** (Backend API)
- **Vis.js** (Frontend Graph Visualization)
- **GitHub** (Version Control)

---

# ✅ Milestone 1 – Data Ingestion & Preprocessing

### Tasks Completed
- Data cleaning using Pandas.
- Removal of null values and duplicates.
- Data normalization and feature enrichment.
- Processed dataset generation.

### Output
```text
cleaned_tickets.xlsx
```

---

# ✅ Milestone 2 – Entity Extraction & Graph Construction

## Step 1: Structured Triple Extraction
Extracted **entity–relationship–entity triples** from structured columns.
*Example triples:*
```text
Customer → RAISED → Ticket
Ticket → HAS_SEVERITY → Severity
Ticket → SUBMITTED_VIA → Channel
```
**Output:** `structured_triples.csv`

## Step 2: LLM-Based NER
Used LLMs to extract semantic relationships from raw ticket descriptions.
*Example triples:*
```text
(Dell XPS, EXPERIENCING, Not turning on)
(Dell XPS, REQUIRED_ACTION, Troubleshoot power issues)
```
**Output:** `llm_triples.csv`

## Step 3: Graph Construction (Neo4j Cloud)
- Combined structured and LLM-generated triples.
- Inserted triples into **Neo4j AuraDB** using the Python Neo4j driver.
- Constructed graph nodes and relationships.

### Graph Statistics
```text
Graph Statistics (Sample Run – First 20 Rows)
Nodes: ~160+
Relationships: ~240+

Note: Running the pipeline on the full dataset generates a significantly larger, interconnected knowledge graph.
```

## Step 4: Graph Validation
Validated graph integrity using Cypher queries directly in the cloud.

*Count Nodes & Relationships:*
```cypher
MATCH (n) RETURN count(n);
MATCH ()-[r]->() RETURN count(r);
```

---
