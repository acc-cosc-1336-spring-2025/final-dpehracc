#add import

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.question_a.question_a import get_most_likely_ancestor_consensus

def main():
    while True:
        print("\nDNA Substring Finder")
        dna_string1 = input("Enter a DNA string (9-16 characters): ").upper()
        if len(dna_string1) <= 8 or len(dna_string1) > 16:
            print("Invalid. Must be over 8 but up to 16 characters.")
            continue

        dna_string2 = input("Enter a DNA substring (4 characters): ").upper()
        if len(dna_string2) != 4:
            print("Invalid. Must be exactly 4 characters.")
            continue

        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        print("Substring found at positions: ", *result)

        again = input("Try again? (y/n)")
        if again.lower() != 'y':
            break
        if __name__ == "__main__":
            main()