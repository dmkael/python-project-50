### Hexlet tests and linter status:
[![Actions Status](https://github.com/dmkael/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dmkael/python-project-50/actions)
[![.github/workflows/my_check.yml](https://github.com/dmkael/python-project-50/actions/workflows/my_check.yml/badge.svg)](https://github.com/dmkael/python-project-50/actions/workflows/my_check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e305410ffe47028932e3/maintainability)](https://codeclimate.com/github/dmkael/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e305410ffe47028932e3/test_coverage)](https://codeclimate.com/github/dmkael/python-project-50/test_coverage)

---

### Generate difference
##### (Course project 2)

A small Python tool to define the difference between 2 files and show the difference for the 2nd file relative to the 1st. \
To use it just type **gendiff <path_to_file_1> <path_to_file_2>** and the difference will shown on screen.\
Supported input file types: **.json, .yaml, .yml.**\
Supported output format options: **stylish, plain, json.**\
The default output format is **stylish** but you can define supported output with the optional key.\
To use another output additionally type option key **-f** or **--format** and **<output_format_option>**

<details>
  <summary>System requirements</summary>
  
- Python 3.10 or above
- GIT

</details>

<details>
  <summary>How to install</summary>
To install the package:
  
- __Linux__:
  - for current user:

      ```python3 -m pip install --user git+https://github.com/dmkael/python-project-50.git```

  - for system (runs on built-in python):

      ```python3 -m pip install git+https://github.com/dmkael/python-project-50.git```
    

- __Windows__:
  - for current user:

      ```py -m pip install --user git+https://github.com/dmkael/python-project-50.git```
      
  - for system:

      ```py -m pip install git+https://github.com/dmkael/python-project-50.git```

  _NOTE: If the __gendiff__ command are not available in your shell after installation __for user__, you’ll need to add the directory to your PATH. More info here:_
  _[Installing to the user documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-to-the-user-site)_

</details>

<details>
  <summary>Demonstration</summary>
  
[![asciicast](https://asciinema.org/a/NyXwtY0BGPYeO4huIabb3mMpN.svg)](https://asciinema.org/a/NyXwtY0BGPYeO4huIabb3mMpN)

</details>

<details>
  <summary>How to uninstall</summary>
  
To uninstall the package run the command: 

- __Linux__:

    ```python3 -m pip uninstall hexlet-code```

- __Windows__:

    ```py -m pip uninstall hexlet-code```

</details>

<details>
  <summary>Miscellaneous</summary>

You can clone the repository and use some make commands defined in Makefile:
1. **make lint** - to run linter
2. **make test** - to run pytest
3. **make test-extended** - to run pytest with extended output
4. **make test-coverage-display** - to view test coverage

Read **Makefile** to view more available options

</details>
