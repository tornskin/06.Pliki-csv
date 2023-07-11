import csv
import sys

from handler import FileHandler

def read_data_from_file(file):
    matrix = []
    with open(file) as file:
        reader = csv.reader(file)
        for line in reader:
            matrix.append(line)
    return matrix

def change_data_in_our_matrix(matrix, incoming_data):
    data_to_change = incoming_data.split(",")
    x_value = int(data_to_change[0])
    y_value = int(data_to_change[1])
    matrix[x_value][y_value] = data_to_change[2]

def write_data_to_file(file, matrix):
    with open(file, mode="w") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)

FileHandler(
    input_file=sys.argv[1],
    output_file=sys.argv[2],
    changes_in_file=sys.argv[3:]
).run_program()
