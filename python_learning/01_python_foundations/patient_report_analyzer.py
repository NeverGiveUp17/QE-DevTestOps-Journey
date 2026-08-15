"""
#The function will search for word and return the line number if found
def search_word_in_report(word_to_search):    
    with open('QE-DevTestOps-Journey\\python_learning\\01_python_foundations\\patient_report.txt', 'r') as file:
        for line_num, line in enumerate(file, start=1):
            if word_to_search in line.lower():
                return line_num                
        return 0        
"""     
# The function will search a word in report and return all the line numbers if word matches exactly:
def search_word_in_report(word_to_search):
    line_nums = []
    with open('QE-DevTestOps-Journey\\python_learning\\01_python_foundations\\patient_report.txt', 'r') as file:
        for line_num, line in enumerate(file, start=1):
            if word_to_search in line.lower().split():
                line_nums.append(line_num)
        return line_nums
import string
def clean_word(word):
    clean_word = word.strip(string.punctuation)

def main():
    word_to_search = input("Enter the word to search:").strip().lower()
    line_nums = search_word_in_report(word_to_search)
    if line_nums:
        for line_number in line_nums:
            print(f"{word_to_search} -> Line: {line_number}")
    else:
        print(f"{word_to_search} is not found")

if __name__ == "__main__":
    main()