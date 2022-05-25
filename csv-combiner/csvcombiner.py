import argparse
import sys
from csv import reader
from csv import writer
import os.path


def csv_combine(paths) -> None:
    first_file = True
    csv_writer = writer(sys.stdout)

    for path in paths:
        if first_file:
            headers = grab_headers(path)
            csv_writer.writerow(headers)
            first_file = False
        file_name = os.path.basename(path)
        with open(path, "r") as input_file:
            csv_reader = reader(input_file)
            next(csv_reader)
            for row in csv_reader:
                row.append(file_name)
                csv_writer.writerow(row)


def grab_headers(path) -> list:
    with open(path, "r") as input_file:
        csv_reader = reader(input_file)
        row = next(csv_reader)
        row.append("file_name")
        return row


def correct_arguments(args) -> None:
    for path in args:
        if not os.path.exists(path):
            raise FileNotFoundError(path + ' is not a valid file system path.')
        if not path.endswith('.csv'):
            raise TypeError(path + ' is not a .csv file.')


def main(csv_path):
    correct_arguments(csv_path)
    csv_combine(csv_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Combines two or more csv files')
    parser.add_argument('csv_path', nargs='+', help='files you want to combine')

    args = parser.parse_args()
    main(args.csv_path)
