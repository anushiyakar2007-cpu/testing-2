import pandas as pd

data = {
    'RollNumber': [101, 102, 103, 104, 105],
    'Name': ['Anushiya', 'Ashly', 'Dharshini', 'Kiruba', 'Nivetha'],
    'English': [85, 78, 92, 65, 88],
    'Tamil': [90, 82, 85, 70, 95],
    'Maths': [95, 88, 76, 60, 98],
    'Science': [88, 90, 84, 75, 92],
    'Social': [82, 85, 90, 80, 89]
}

df_sample = pd.DataFrame(data)
df_sample.to_csv('students_marks.csv', index=False)
print('Sample file "students_marks.csv" created successfully.')
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

CSV_FILE = "students_marks.csv"


def load_and_process_data():
    """Loads student dataset and computes performance analytics metrics."""

    if not os.path.exists(CSV_FILE):
        print(f"Error: '{CSV_FILE}' not found.")
        return None

    df = pd.read_csv(CSV_FILE)
    df.columns = df.columns.str.strip()

    subjects = ["English", "Tamil", "Maths", "Science", "Social"]

    required_cols = ["RollNumber", "Name"] + subjects

    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        print("Missing columns:", missing_cols)
        return None

    df["Total"] = df[subjects].sum(axis=1)
    df["Percentage"] = df["Total"] / len(subjects)

    def assign_grade(pct):
        if pct >= 90:
            return "O"
        elif pct >= 80:
            return "A+"
        elif pct >= 70:
            return "A"
        elif pct >= 60:
            return "B+"
        elif pct >= 50:
            return "B"
        elif pct >= 40:
            return "C"
        else:
            return "RA"

    df["Grade"] = df["Percentage"].apply(assign_grade)


    df["Result"] = df[subjects].apply(
        lambda row: "Pass" if (row >= 40).all() else "RA",
        axis=1
    )

    return df


def generate_descriptive_stats(df):
    """Computes academic metrics."""

    subjects = ["English", "Tamil", "Maths", "Science", "Social"]

    print("\n" + "=" * 60)
    print("        STUDENT PERFORMANCE ANALYTICS REPORT")
    print("=" * 60)

    print("\nProcessed Data Overview:\n")
    print(
        df[
            [
                "RollNumber",
                "Name",
                "Total",
                "Percentage",
                "Grade",
                "Result",
            ]
        ].to_string(index=False)
    )

    print("\nSubject-Wise Class Averages:")

    for sub in subjects:
        avg_score = df[sub].mean()
        print(f"{sub:<10}: {avg_score:.2f}")

    topper = df.loc[df["Total"].idxmax()]

    print("\n" + "-" * 60)
    print(
        f"Class Topper : {topper['Name']} "
        f"(Roll No: {topper['RollNumber']})"
    )
    print(
        f"Total Marks  : {topper['Total']} | "
        f"Percentage : {topper['Percentage']:.2f}%"
    )
    print("-" * 60)


def visualize_performance_analytics(df):
    """Generates charts for performance analytics."""

    subjects = ["English", "Tamil", "Maths", "Science", "Social"]

    
    plt.figure(figsize=(12, 6))

    x = np.arange(len(df))
    width = 0.15

    for i, sub in enumerate(subjects):
        plt.bar(
            x + i * width,
            df[sub],
            width,
            label=sub
        )

    plt.xticks(
        x + width * (len(subjects) - 1) / 2,
        df["Name"],
        rotation=30
    )

    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.title("Subject-Wise Student Score Comparison")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

    
    plt.figure(figsize=(7, 7))

    grade_counts = df["Grade"].value_counts()

    plt.pie(
        grade_counts,
        labels=grade_counts.index,
        autopct="%1.1f%%",
        startangle=140
    )

    plt.title("Grade Distribution")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    student_df = load_and_process_data()

    if student_df is not None:
        generate_descriptive_stats(student_df)
        visualize_performance_analytics(student_df)

        print("\nAvailable Columns:")
        print(student_df.columns.tolist())
