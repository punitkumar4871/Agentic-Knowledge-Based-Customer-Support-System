## Step 2: LLM-based Entity Extraction
Used a local LLM (**Mistral via Ollama**) to mine free-text `Ticket Description`
fields for relationships that structured columns can't capture — the specific
problem a product is experiencing, and the specific action required to fix it.

**Output:** `llm_triples.csv`

## Step 3: Merge Structured + LLM Triples
Combined rule-based structured triples with LLM-mined triples into a single,
unified triple set — the source of truth for graph construction.

**Output:** `final_triples.csv` (180 structured + 39 LLM-mined = 219 total triples)

---
