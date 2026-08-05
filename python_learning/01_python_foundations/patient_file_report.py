# The function to write sample data into a file. It will create a file if not exists.
def write_report():
    with open("C:\\Users\\datha\\Consistancy\\QE-DevTestOps-Journey\\python_learning\\01_python_foundations\\patient_report.txt", "w") as file:
        file.write("Patient Report\n")
        file.write("-----------------\n")
        file.write("Total Patients : 250\n")
        file.write("Active Patients : 180\n")

# The function will read the data present in the file and return the same.
def read_report():
    with open("C:\\Users\\datha\\Consistancy\\QE-DevTestOps-Journey\\python_learning\\01_python_foundations\\patient_report.txt", "r") as file:
        content = file.read()
        return content

def main():
    write_report()
    content = read_report()
    if not content:
        print("No content available in the file")
    else:
        print(content)

if __name__ == "__main__":
    main()

