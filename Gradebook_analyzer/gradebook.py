# Name: Tanisq Kumar
# Date: November 26, 2025
# Project Title: GradeBook Analyzer
# Course: Programming for Problem Solving using Python
"""
GradeBook Analyzer - only uses csv and numpy
Student: Tanishq
"""

import csv
import numpy as np

# ---------- CSV load/save ----------
def load_from_csv(path):
    """
    Expect CSV rows: Name,Marks
    Returns dict {name: float_mark}
    """
    marks = {}
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                name = row[0].strip()
                if name == "" or len(row) < 2:
                    # skip invalid rows
                    continue
                try:
                    score = float(row[1])
                except ValueError:
                    continue
                marks[name] = score
    except FileNotFoundError:
        print("CSV file not found:", path)
    return marks

def save_to_csv(path, marks, grades):
    """
    Save Name,Marks,Grade
    """
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])
        for n, m in marks.items():
            writer.writerow([n, m, grades.get(n, "")])
    print("Saved to", path)

# ---------- Stats using numpy ----------
def calculate_average(marks):
    if not marks:
        return 0.0
    arr = np.array(list(marks.values()), dtype=float)
    return float(np.mean(arr))

def calculate_median(marks):
    if not marks:
        return 0.0
    arr = np.array(list(marks.values()), dtype=float)
    return float(np.median(arr))

def find_max_score(marks):
    if not marks:
        return ("", 0.0)
    # numpy argmax on array, map back to name
    names = list(marks.keys())
    scores = np.array(list(marks.values()), dtype=float)
    idx = int(np.argmax(scores))
    return (names[idx], float(scores[idx]))

def find_min_score(marks):
    if not marks:
        return ("", 0.0)
    names = list(marks.keys())
    scores = np.array(list(marks.values()), dtype=float)
    idx = int(np.argmin(scores))
    return (names[idx], float(scores[idx]))

# ---------- Grade logic ----------
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def build_grades(marks):
    return {n: assign_grade(m) for n, m in marks.items()}

def grade_distribution(grades):
    cats = ["A","B","C","D","F"]
    return {c: sum(1 for g in grades.values() if g==c) for c in cats}

# ---------- Pass/Fail (list comprehensions) ----------
def pass_fail_lists(marks, pass_mark=40.0):
    passed = [n for n, m in marks.items() if m >= pass_mark]
    failed = [n for n, m in marks.items() if m < pass_mark]
    return passed, failed

# ---------- Manual entry ----------
def manual_entry():
    print("Enter student data. Blank name to stop.")
    marks = {}
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        s = input("Marks (0-100): ").strip()
        try:
            m = float(s)
        except ValueError:
            print("Invalid mark, try again.")
            continue
        marks[name] = m
    return marks

# ---------- Print table ----------
def print_table(marks, grades):
    print("\n{:<20}{:<10}{}".format("Name","Marks","Grade"))
    print("-"*40)
    for n, m in marks.items():
        print("{:<20}{:<10}{}".format(n, str(m), grades.get(n,"")))
    print("-"*40)

# ---------- Main flow ----------
def analyze_marks(marks):
    if not marks:
        print("No data to analyze.")
        return
    avg = calculate_average(marks)
    med = calculate_median(marks)
    max_name, max_score = find_max_score(marks)
    min_name, min_score = find_min_score(marks)
    grades = build_grades(marks)
    dist = grade_distribution(grades)
    passed, failed = pass_fail_lists(marks)

    print("\n--- Summary ---")
    print("Students:", len(marks))
    print("Average: {:.2f}".format(avg))
    print("Median: {:.2f}".format(med))
    print("Max: {} -> {}".format(max_name, max_score))
    print("Min: {} -> {}".format(min_name, min_score))
    print("\nGrade Distribution:")
    for k, v in dist.items():
        print(" {}: {}".format(k, v))
    print("\nPassed ({}): {}".format(len(passed), ", ".join(passed) if passed else "None"))
    print("Failed ({}): {}".format(len(failed), ", ".join(failed) if failed else "None"))
    print_table(marks, grades)

    # offer CSV save
    ans = input("Save results to CSV? (y/n): ").strip().lower()
    if ans == 'y':
        out = input("Output filename (default final_grades.csv): ").strip()
        if out == "":
            out = "final_grades.csv"
        save_to_csv(out, marks, grades)

def main():
    while True:
        print("\n1) Manual entry")
        print("2) Load from CSV")
        print("3) Exit")
        c = input("Choose (1/2/3): ").strip()
        if c == "1":
            marks = manual_entry()
            analyze_marks(marks)
        elif c == "2":
            path = input("CSV path (default students.csv): ").strip()
            if path == "":
                path = "students.csv"
            marks = load_from_csv(path)
            if not marks:
                print("No valid data loaded from CSV.")
                continue
            analyze_marks(marks)
        elif c == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
