---
name: csv-date-column-validator
description: Validate a CSV file by checking required columns, detecting missing values, verifying date format in a date column, and generating a structured data quality report.
---

## When to use this skill

Use this skill when you need to:
- Validate the structure of a CSV file
- Ensure a required date column exists
- Check whether date values follow the YYYY-MM-DD format
- Identify missing or invalid data in a dataset
- Generate a quick quality report for tabular data
- When you need to validate required columns in a CSV file

## When NOT to use this skill

Do not use this skill when:
- The input is not a CSV file
- You only need simple reasoning or text generation
- There is no need to validate structured data
- The dataset is extremely large and requires distributed processing

## Expected inputs

- file_path (string): Path to the CSV file
- date_column (string): Name of the column containing dates

## Step-by-step instructions

1. Load the CSV file using Python's csv module
2. Check whether required columns (e.g., id, name, date) exist
3. Iterate through each row:
   - Check for missing required values
   - Validate whether the date follows the YYYY-MM-DD format
4. Count:
   - Total rows
   - Valid rows
   - Invalid rows
5. Track row indices with errors
6. Generate a structured validation report

## Expected output format

A dictionary containing:
- total_rows
- valid_rows
- invalid_rows
- missing_values
- invalid_row_indices (list)

Example:

{
  "total_rows": 4,
  "valid_rows": 2,
  "invalid_rows": 1,
  "missing_values": 1,
  "invalid_row_indices": [3]
}

## Limitations and checks

- Assumes CSV is well-formatted (no complex quoting issues)
- Only validates date format, not semantic correctness
- Does not handle multiple date formats
- File must be accessible locally

## Why this skill requires a script

Validating a CSV file row-by-row is a deterministic, structured task that involves parsing files, checking formats, and aggregating statistics. This is inefficient and unreliable for a language model to perform directly. A Python script ensures fast, accurate, and consistent validation.