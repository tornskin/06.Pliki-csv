import sys
import os
from handler import CSVHandler, JSONHandler, TXTHandler, PickleHandler

if len(sys.argv) < 4:
    print("Podano za mało argumentów.")
    print("Użyj: python zadanie.py input_file output_file changes_in_file")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
changes_in_file = sys.argv[3:]

if not os.path.exists(input_file):
    print("Podany plik wejściowy nie istnieje.")
    sys.exit(1)

file_extension = input_file.split('.')[-1].lower()

if file_extension == "csv":
    handler = CSVHandler(input_file, output_file, changes_in_file)
elif file_extension == "json":
    handler = JSONHandler(input_file, output_file, changes_in_file)
elif file_extension == "txt":
    handler = TXTHandler(input_file, output_file, changes_in_file)
elif file_extension == "pickle":
    handler = PickleHandler(input_file, output_file, changes_in_file)
else:
    print(f"Nieobsługiwany format pliku: {file_extension}")
    sys.exit(1)

try:
    handler.run_program()
except FileNotFoundError:
    print("Podany plik wejściowy nie istnieje.")
    sys.exit(1)
except ValueError as e:
    print(f"Podano niepoprawne dane wejściowe: {e}")
    sys.exit(1)
