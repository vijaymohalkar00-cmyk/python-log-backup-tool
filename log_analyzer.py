def analyze_log(file_path):
    errors = 0
    warnings = 0

    with open(file_path, "r") as f:
        for line in f:
            if "error" in line.lower():
                errors += 1
            if "warning" in line.lower():
                warnings += 1

    return errors, warnings
