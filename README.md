# 🧠 (KGB) AI Knowledge Graph Builder for Enterprise Intelligence

### **Authors:** PUNIT KUMAR

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)]()
[![Neo4j](https://img.shields.io/badge/Neo4j_Aura_Cloud-018bff?style=for-the-badge&logo=neo4j&logoColor=white)]()
[![Groq](https://img.shields.io/badge/Groq_API-f55036?style=for-the-badge&logo=groq&logoColor=white)]()
[![Llama 3.1](https://img.shields.io/badge/Llama_3.1-0467df?style=for-the-badge&logo=meta&logoColor=white)]()
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)]()

---

# 📖 Project Overview -

This project builds an enterprise-level **AI-powered Knowledge Graph system** from structured and unstructured customer support data.

The system extracts entities and relationships from support tickets, constructs a **dynamic knowledge graph**, and enables **intelligent semantic search with a Retrieval-Augmented Generation (RAG) pipeline**. It provides high-speed automated troubleshooting responses via an interactive graph dashboard.

---

# 🎯 Objective

To transform enterprise support ticket data into a scalable, cloud-native knowledge graph that enables:

- **Relationship-based analysis** to uncover hidden connections.
- **Intelligent troubleshooting** driven by high-speed LLM inference.
- **Semantic search** over vast amounts of support tickets.
- **AI-assisted IT support responses** for actionable intelligence.

---

# 🏗 Project Architecture (Cloud-Native)

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
Embedding Generation (Local PyTorch OR Serverless Hugging Face API)
      ↓
Vector Database (FAISS)
      ↓
Semantic Search
      ↓
Retrieval-Augmented Generation (Groq API + Llama 3.1)
```



(full pipeline):
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

# 📂 Project Structure

```text
AI-Knowledge-Graph-Builder/
├── app/                 # Flask backend, routes, templates, static assets
├── data/
│   ├── raw/              # Original, untouched dataset
│   └── processed/        # Cleaned data and extracted triples
├── notebooks/           # Data loading & LLM extraction notebooks
├── scripts/             # Graph, embedding, and RAG pipeline scripts
├── requirements.txt      # Python dependencies
├── package.json          # Node dependencies (Ollama client)
└── README.md
```

> This README will be filled in section by section as each milestone is built (data ingestion, graph construction, semantic search, RAG, backend, deployment).

---

# 🛠 Setup (Work in Progress)

```bash
git clone <your-repo-url>
cd AI-Knowledge-Graph-Builder
pip install -r requirements.txt
```
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


Further setup instructions will be added as the project develops.
