### Hexlet tests and linter status:
[![Actions Status](https://github.com/dmkael/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dmkael/python-project-50/actions)
[![.github/workflows/my_check.yml](https://github.com/dmkael/python-project-50/actions/workflows/my_check.yml/badge.svg)](https://github.com/dmkael/python-project-50/actions/workflows/my_check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e305410ffe47028932e3/maintainability)](https://codeclimate.com/github/dmkael/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e305410ffe47028932e3/test_coverage)](https://codeclimate.com/github/dmkael/python-project-50/test_coverage)
### Generate difference
##### (Course project 2)

A small Python tool to define the difference between 2 files and show the difference for the 2nd file relative to the 1st. \
To use it just type <strong>gendiff <path_to_file_1> <path_to_file_2></strong> and the difference will shown on screen\
Supported input file types: <strong>.json, .yaml, .yml.</strong>\
Supported output format options: <strong>stylish, plain, json.</strong>\
The default output format is <strong>'stylish'</strong> but you can define another output with the optional key <strong>'-f / --format'</strong>\
To use another format just add option <strong>-f</strong> [or] <strong>--format <output_format_option></strong>

<details>
  <summary>System requirements</summary>
Python 3.9 or above

</details>

<details>
  <summary>How to install</summary>
To install the package run the command:

```python3 -m pip install --user git+https://github.com/dmkael/python-project-50.git```

</details>

<details>
  <summary>Demonstration</summary>
  
[![asciicast](https://asciinema.org/a/NyXwtY0BGPYeO4huIabb3mMpN.svg)](https://asciinema.org/a/NyXwtY0BGPYeO4huIabb3mMpN)

</details>

<details>
  <summary>How to uninstall</summary>
  
To uninstall the package run the command: 

```python3 -m pip uninstall gendiff-code```

</details>
