import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

#add import
from src.question_b.question_b import stock_purchase_history

def main():
    while True:
        print("\n1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            print("OK")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()