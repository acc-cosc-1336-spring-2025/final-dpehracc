import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

#add import

from src.question_d.question_d import create_multiplication_table, display_multiplication_table

def main():
    while True:
        print("\nMultiplication Table Generator")
        table = create_multiplication_table()
        display_multiplication_table(table)

        again = input("Recreate table? y/n: ")
        if again.lower() != "y":
            break

if __name__ == "__main__":
    main()