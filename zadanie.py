import sys

from handler import FileHandler

if len(sys.argv) < 4:
    print("Podano za mało argumentów.")
    print("Użyj: python zadanie.py input_file output_file changes_in_file")
    sys.exit(1)

try:
    FileHandler(
        input_file=sys.argv[1],
        output_file=sys.argv[2],
        changes_in_file=sys.argv[3:]
    ).run_program()
except FileNotFoundError:
    print("Podany plik wejściowy nie istnieje.")
    sys.exit(1)
