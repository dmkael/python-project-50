import argparse
from gendiff.gendiff import generate_diff
import sys


def main():
    # Вся информация обратной трассировки подавляется.
    # Выводятся только тип и значение исключения.
    # Закомментируйте sys.tracebacklimit, чтобы отключить подавление.
    sys.tracebacklimit = 0
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        usage='%(prog)s [options] <first_file> <second_file>'
    )
    parser.add_argument("<first_file>", help=argparse.SUPPRESS)
    parser.add_argument("<second_file>", help=argparse.SUPPRESS)
    parser.add_argument('-f', '--format',
                        metavar='<style>',
                        default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='format with style: %(choices)s')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    if diff:
        print(diff)


if __name__ == "__main__":
    main()
