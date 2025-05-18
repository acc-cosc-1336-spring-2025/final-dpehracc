import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

#add import
from src.question_c.question_c import get_stock_list

def main():
    while True:
        print("\n1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_list = get_stock_list()
            print("\nCompany       Symbol")
            for stock in stock_list:
                print(f"{stock.get_company_name():<13} {stock.get_symbol()}")
        elif choice == "2":
            print("OK")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
     main()