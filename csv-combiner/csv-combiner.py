import argparse
import sys
from csv import reader
from csv import writer
import os.path


def main():
    parser = argparse.ArgumentParser(description='Combines two or more csv files')
    parser.add_argument('csv', nargs='+', help='files you want to combine')

    args = parser.parse_args()
    csv_combine(args)


def csv_combine(paths) -> None:
    first_file = True
    csv_writer = writer(sys.stdout)
    for path in paths.csv:
        first_row = True
        if not path.endswith('.csv'):
            print("Only accepts csv files")
            return
        file_name = os.path.basename(path)
        with open(path, "rt") as input_file:
            csv_reader = reader(input_file)
            for row in csv_reader:
                if first_file:
                    row.append("File Name")
                    first_file = False
                    first_row = False
                else:
                    if first_row:
                        first_row = False
                        continue
                    row.append(file_name)

                csv_writer.writerow(row)


if __name__ == "__main__":
    main()
