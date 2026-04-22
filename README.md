# HW5 – CSV Date Column Validator

## What this skill does
This skill validates a CSV file by checking whether required columns exist, detecting missing values, verifying that a date column follows the YYYY-MM-DD format, and generating a structured data quality report.

## Why I chose this skill
I chose this skill because it requires a real Python script to do deterministic work that a prompt alone should not handle. The script parses a CSV file, validates structure, checks date values row by row, and produces a repeatable report. This makes the script central to the workflow rather than decorative.

## How to use it
This skill is used when an agent or coding assistant needs to validate CSV data.

Example prompts:
- Validate the CSV file at data/sample.csv using the csv-date-column-validator skill.
- Validate the CSV file at data/missing_date_column.csv using the csv-date-column-validator skill.
- Validate the CSV file at data/us_date_format.csv using the csv-date-column-validator skill.

You can also run the script directly in terminal:
python .agents/skills/csv-date-column-validator/scripts/csv_tool.py

## What the script does
The script performs the deterministic part of the task. It:
- reads a CSV file
- checks whether required columns are present
- checks for missing required values
- validates the date column using the YYYY-MM-DD format
- counts valid and invalid rows
- returns a structured validation report

## What worked well
The skill worked well for:
- detecting missing required columns
- finding missing values in rows
- identifying invalid date formats
- generating a clear summary report
- handling multiple test cases in the coding assistant

## What limitations remain
This skill still has some limitations:
- it only supports the YYYY-MM-DD date format
- it does not automatically repair invalid data
- it assumes the CSV file is local
- it is designed for simple validation, not complex schema validation

## Demo video
PASTE_YOUR_VIDEO_LINK_HERE