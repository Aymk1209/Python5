# PROJECT 1: TRANSACTION DATA PIPELINE
# 1. Read transactions.txt line by line
# 2. Validate each row
# 3. Write valid rows to clean.txt
# 4. Write invalid rows with reason to error.log
# 5. Use flush() for logs
# 6. Generate report.txt with:
#    - Total Records
#    - Valid Records
#    - Invalid Records
#    - Total Revenue
#    - Category-wise Revenue
# 7. Use seek() or tell() somewhere in the program
# Write a Python program using only file handling that processes
# the above transaction file and produces clean data, error logs, and a final report.
def is_valid_amount(s: str) -> bool:
    if not s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


def main():
    total_records = 0
    valid_records = 0
    invalid_records = 0
    total_revenue = 0.0
    category_revenue = {}

    # Step 1: open all needed files
    with open("transactions.txt.py", "r", encoding="utf-8") as tx_file, \
         open("clean.txt", "w", encoding="utf-8") as clean_file, \
         open("error.log", "w", encoding="utf-8") as error_log:

        # Demonstrate tell(): record start position
        start_pos = tx_file.tell()
        print(f"Start file position: {start_pos}", file=error_log, flush=True)

        # Read header line once (skip validation for it)
        header = tx_file.readline()
        total_records += 1
        if header.strip():
            clean_file.write(header)  # Write header to clean.txt
        else:
            print("Line 1: EMPTY HEADER -> skipped", file=error_log, flush=True)

        # Read remaining lines one by one
        for line_num, line in enumerate(tx_file, start=2):
            total_records += 1
            line = line.strip()

            if not line:
                invalid_records += 1
                print(
                    f"Line {line_num}: EMPTY LINE -> skipped",
                    file=error_log,
                    flush=True,
                )
                continue

            parts = line.split(",", maxsplit=2)

            if len(parts) != 3:
                invalid_records += 1
                print(
                    f"Line {line_num}: INVALID FORMAT (expected 3 fields, got {len(parts)}) -> {line!r}",
                    file=error_log,
                    flush=True,
                )
                continue

            user_id, amount_str, category = map(str.strip, parts)

            # Validate user_id (non‑empty)
            if not user_id:
                invalid_records += 1
                print(
                    f"Line {line_num}: INVALID USER_ID (empty) -> {line!r}",
                    file=error_log,
                    flush=True,
                )
                continue

            # Validate amount (must be float)
            if not is_valid_amount(amount_str):
                invalid_records += 1
                print(
                    f"Line {line_num}: INVALID AMOUNT '{amount_str}' -> {line!r}",
                    file=error_log,
                    flush=True,
                )
                continue

            try:
                amount = float(amount_str)
            except Exception:
                invalid_records += 1
                print(
                    f"Line {line_num}: UNEXPECTED AMOUNT ERROR -> {line!r}",
                    file=error_log,
                    flush=True,
                )
                continue

            # Validate category (non‑empty)
            if not category:
                invalid_records += 1
                print(
                    f"Line {line_num}: INVALID CATEGORY (empty) -> {line!r}",
                    file=error_log,
                    flush=True,
                )
                continue

            # If we reach here, row is valid
            valid_records += 1
            total_revenue += amount

            # Add to category revenue
            category_revenue[category] = category_revenue.get(category, 0.0) + amount

            # Write valid line to clean.txt
            clean_file.write(line + "\n")

        # Step 7: example of seek() / tell() to show file positioning
        # Record current position before seeking
        mid_pos = tx_file.tell()
        print(f"Final read position (mid_pos): {mid_pos}", file=error_log, flush=True)

        if tx_file.seekable():
            if mid_pos > 0:
                # Move back 10 bytes (or as far as possible)
                backward_amount = min(10, mid_pos)
                tx_file.seek(mid_pos - backward_amount)
                snippet = tx_file.read(20)  # read up to 20 bytes
                print(
                    f"DEMONSTRATION: From pos {mid_pos - backward_amount}, read snippet: {repr(snippet)}",
                    file=error_log,
                    flush=True,
                )

    # Step 6: generate report.txt
    with open("report.txt", "w", encoding="utf-8") as report:
        report.write("=== TRANSACTION REPORT ===\n")
        report.write(f"Total Records: {total_records}\n")
        report.write(f"Valid Records: {valid_records}\n")
        report.write(f"Invalid Records: {invalid_records}\n")
        report.write(f"Total Revenue: {total_revenue:.2f}\n\n")

        report.write("Category-wise Revenue:\n")
        if category_revenue:
            # Sort by category name for predictable output
            for cat in sorted(category_revenue):
                amount = category_revenue[cat]
                report.write(f"{cat}: {amount:.2f}\n")
        else:
            report.write("(No valid categories)\n")

    # Optional: print summary to console
    print("\n=== Summary ===")
    print(f"Total Records: {total_records}")
    print(f"Valid Records: {valid_records}")
    print(f"Invalid Records: {invalid_records}")
    print(f"Total Revenue: {total_revenue:.2f}")
    print("Category-wise Revenue:")
    for cat in sorted(category_revenue):
        print(f"  {cat}: {category_revenue[cat]:.2f}")


if __name__ == "__main__":
    main()
