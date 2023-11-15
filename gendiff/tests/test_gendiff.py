from gendiff.gendiff import generate_diff


def test_gendiff():
    assert generate_diff("gendiff/tests/fixtures/file1.json",
                         "gendiff/tests/fixtures/file2.json") == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - random: _
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff("gendiff/tests/fixtures/file1.json",
                         "gendiff/tests/fixtures/file3.json") == """{
  - follow: false
  + follow: true
  - host: hexlet.io
  + host: hexlet.ru
  + not_random: 100
    proxy: 123.234.53.22
  - random: _
  - timeout: 50
  + timeout: 0
}"""
    assert (generate_diff("gendiff/tests/fixtures/file1.json",
                          "gendiff/tests/fixtures/file4.txt")
            == "Files types are different or file(s) are empty")
    assert generate_diff("gendiff/tests/fixtures/example1.yaml",
                         "gendiff/tests/fixtures/example2.yml") == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
