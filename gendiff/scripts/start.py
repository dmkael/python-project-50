import argparse
from gendiff.gendiff import generate_diff
import sys


def main():
    # Вся информация обратной трассировки подавляется.
    # Выводятся только тип и значение исключения.
    # Закомментируйте sys.tracebacklimit, чтобы отключить подавление.
    sys.tracebacklimit = 0
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference in the second file compared to the first."
    )
    parser.add_argument("<filepath1>", help='path to the first file')
    parser.add_argument("<filepath2>", help='path to the second file')
    parser.add_argument('-f', '--format', default='stylish', help='output format (default: "stylish")')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + '0.1.0')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    if diff:
        print(diff)


if __name__ == "__main__":
    main()
