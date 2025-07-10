import sys
import csv

def read_csv_first_column(filename):
    values = set()
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 1:
                values.add(row[0])
    return values

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_csv.py <master.csv> <test.csv>")
        sys.exit(1)

    master_file = sys.argv[1]
    test_file = sys.argv[2]

    master_values = read_csv_first_column(master_file)
    test_values = read_csv_first_column(test_file)

    true_positives_set = master_values & test_values
    false_negatives_set = master_values - test_values
    false_positives_set = test_values - master_values

    print(f"True Positives: {len(true_positives_set)}")
    print("  Values:")
    for val in sorted(true_positives_set):
        print(f"    {val}")
    print(f"False Negatives: {len(false_negatives_set)}")
    print("  Values:")
    for val in sorted(false_negatives_set):
        print(f"    {val}")
    print(f"False Positives: {len(false_positives_set)}")
    print("  Values:")
    for val in sorted(false_positives_set):
        print(f"    {val}")%   
