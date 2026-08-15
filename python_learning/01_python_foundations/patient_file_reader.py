# The function will read content line by line from a file.
def display_report_line_by_line():
    line_num = 1
    with open('QE-DevTestOps-Journey\\python_learning\\01_python_foundations\\patient_report.txt', 'r') as file:
        for line in file:
            print(f"Line {line_num}: {line}")
            line_num += 1

def main():
    display_report_line_by_line()

if __name__ == "__main__":
    main()
    