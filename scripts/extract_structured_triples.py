"""
Milestone 2 - Step 1: Structured Triple Extraction

Converts the cleaned, structured ticket columns (Customer, Product, Severity,
Channel, Resolution, etc.) into Knowledge Graph triples of the form:

    (Subject, Predicate, Object)

These are "structured" triples because they come directly from spreadsheet
columns - no LLM/NLP is involved here. Free-text description mining happens
separately in Milestone 2 - Step 2 (LLM-based extraction).

Run from the project root:
    python scripts/extract_structured_triples.py
"""

import pandas as pd

INPUT_PATH = "data/processed/cleaned_tickets.xlsx"
OUTPUT_PATH = "data/processed/structured_triples.csv"


def build_structured_triples(df: pd.DataFrame) -> pd.DataFrame:
    """Build (Subject, Predicate, Object) triples from structured ticket columns."""
    triples = []

    for _, row in df.iterrows():
        ticket_id = f"Ticket_{row['Ticket ID']}"
        customer = row["Customer Name"]
        product = row["Product Purchased"]

        # Customer -> PURCHASED -> Product
        triples.append([customer, "PURCHASED", product])

        # Customer -> RAISED -> Ticket
        triples.append([customer, "RAISED", ticket_id])

        # Ticket -> REPORTS_ISSUE -> Ticket Subject
        triples.append([ticket_id, "REPORTS_ISSUE", row["Ticket Subject"]])

        # Ticket -> HAS_SEVERITY -> Severity
        triples.append([ticket_id, "HAS_SEVERITY", row["Severity"]])

        # Ticket -> SUBMITTED_VIA -> Channel
        triples.append([ticket_id, "SUBMITTED_VIA", row["Ticket Channel"]])

        # Ticket -> PRODUCED -> Resolution
        triples.append([ticket_id, "PRODUCED", row["Resolution"]])

    return pd.DataFrame(triples, columns=["Subject", "Predicate", "Object"])


def main():
    df = pd.read_excel(INPUT_PATH)

    triples_df = build_structured_triples(df)
    triples_df.to_csv(OUTPUT_PATH, index=False)

    print(f"Structured triples saved to {OUTPUT_PATH}")
    print(f"Total triples generated: {len(triples_df)}")


if __name__ == "__main__":
    main()
