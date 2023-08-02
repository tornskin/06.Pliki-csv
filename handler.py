import csv
import json
import pickle
from typing import List


class FileHandler:

    def __init__(self, input_file, output_file, changes_in_file):
        self.input_file = input_file
        self.output_file = output_file
        self.changes_in_file: List[str] = changes_in_file
        self.matrix = []

    def read_data_from_file(self):
        raise NotImplementedError("read_data_from_file method must be implemented in the subclass.")

    def change_data_in_our_matrix(self):
        for incoming_change in self.changes_in_file:
            try:
                data_to_change = incoming_change.split(",")
                x_value = int(data_to_change[0])
                y_value = int(data_to_change[1])

                # Extend rows to required length
                if x_value >= len(self.matrix):
                    for i in range(len(self.matrix), x_value + 1):
                        self.matrix.append([])

                # Extend row to required length
                if y_value >= len(self.matrix[x_value]):
                    for i in range(len(self.matrix[x_value]), y_value + 1):
                        self.matrix[x_value].append("")

                self.matrix[x_value][y_value] = data_to_change[2]

            except ValueError:
                print("Podano niepoprawne dane wejściowe:", incoming_change)
            except IndexError:
                print("Podane współrzędne są poza zakresem macierzy:", incoming_change)

    def write_data_to_file(self):
        raise NotImplementedError("write_data_to_file method must be implemented in the subclass.")

    def run_program(self):
        self.read_data_from_file()
        self.change_data_in_our_matrix()
        self.write_data_to_file()


class CSVHandler(FileHandler):

    def read_data_from_file(self):
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for line in reader:
                self.matrix.append(line)

    def write_data_to_file(self):
        with open(self.output_file, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.matrix)


class JSONHandler(FileHandler):

    def read_data_from_file(self):
        with open(self.input_file) as file:
            data = json.load(file)
            if "matrix" in data:
                self.matrix = data["matrix"]
            else:
                print("Nieobsługiwany format danych w pliku JSON.")

    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            json.dump({"matrix": self.matrix}, file)


class TXTHandler(FileHandler):

    def read_data_from_file(self):
        with open(self.input_file) as file:
            for line in file:
                row = line.strip().split(',')
                self.matrix.append(row)

    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            for row in self.matrix:
                file.write(','.join(row) + '\n')


class PickleHandler(FileHandler):

    def read_data_from_file(self):
        with open(self.input_file, 'rb') as file:
            self.matrix = pickle.load(file)

    def write_data_to_file(self):
        with open(self.output_file, 'wb') as file:
            pickle.dump(self.matrix, file)
