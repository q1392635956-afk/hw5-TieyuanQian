import csv
from datetime import datetime

REQUIRED_COLUMNS = ["id", "name", "date"]
DATE_FORMAT = "%Y-%m-%d"


def validate_date(date_str):
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False


def validate_csv(file_path):
    report = {
        "missing_required_columns": [],
        "total_rows": 0,
        "valid_rows": 0,
        "invalid_rows": 0,
        "rows_with_missing_required_values": [],
        "rows_with_invalid_date": [],
    }

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            report["missing_required_columns"] = REQUIRED_COLUMNS.copy()
            return report

        missing_columns = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
        report["missing_required_columns"] = missing_columns

        if missing_columns:
            return report

        for row_index, row in enumerate(reader, start=2):  # header is row 1
            report["total_rows"] += 1

            missing_value = False
            for col in REQUIRED_COLUMNS:
                value = row.get(col, "")
                if value is None or str(value).strip() == "":
                    missing_value = True
                    break

            if missing_value:
                report["invalid_rows"] += 1
                report["rows_with_missing_required_values"].append(row_index)
                continue

            if not validate_date(row["date"].strip()):
                report["invalid_rows"] += 1
                report["rows_with_invalid_date"].append(row_index)
                continue

            report["valid_rows"] += 1

    return report


def format_report(report):
    lines = []
    lines.append("CSV Validation Report")
    lines.append("---------------------")
    lines.append(f"Missing required columns: {report['missing_required_columns']}")
    lines.append(f"Total rows: {report['total_rows']}")
    lines.append(f"Valid rows: {report['valid_rows']}")
    lines.append(f"Invalid rows: {report['invalid_rows']}")
    lines.append(
        f"Rows with missing required values: {report['rows_with_missing_required_values']}"
    )
    lines.append(f"Rows with invalid date: {report['rows_with_invalid_date']}")
    return "\n".join(lines)


if __name__ == "__main__":
    sample_path = "data/sample.csv"
    result = validate_csv(sample_path)
    print(format_report(result))