## 📚 GradeBook Analyzer
The GradeBook Analyzer is a Python command-line utility for managing and analyzing student marks. It uses the csv module for file operations and the NumPy library for efficient statistical calculations.

## ✨ Features
Data Entry: Supports both manual entry of student names and marks or loading from a CSV file.

Statistical Analysis: Calculates average, median, maximum, and minimum scores using NumPy.

Grading: Assigns letter grades (A, B, C, D, F) based on predefined thresholds.

Distribution: Generates the grade distribution (count for each grade).

Pass/Fail: Identifies lists of students who passed and failed based on a default pass mark (40.0).

Reporting: Prints a formatted summary and a detailed table of names, marks, and grades.

CSV Output: Allows saving the final results (Name, Marks, Grade) to a new CSV file.

## ⚙️ Prerequisites
This script requires Python 3 and the NumPy library.

You can install NumPy using pip:

Bash
pip install numpy

## 🚀 How to Run
1.Save the provided code as a Python file (e.g., gradebook.py).
2.Run the script from your terminal:

Bash
python gradebook.py
3.Follow the prompts in the menu:

1) Manual entry: You will be prompted to enter a Name and Marks for each student. Enter a blank name to stop.

2) Load from CSV: The script will ask for a CSV path (default is students.csv). The CSV must contain rows with the format: Name,Marks.
