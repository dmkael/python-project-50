import argparse
from gendiff.gendiff import generate_diff
from gendiff.diff_formatters import stylish, plain, json_output


def get_formatter(user_input):
    if user_input == 'plain':
        return plain
    if user_input == 'stylish':
        return stylish
    if user_input == 'json':
        return json_output


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', type=get_formatter, default='stylish')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    if diff:
        print(diff)


if __name__ == "__main__":
    main()
