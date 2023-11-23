import json


def make_json(diff):
    result = json.dumps(diff, indent=4)
    result = result.replace("+add#", 'added >> ')
    result = result.replace("-rem#", 'removed >> ')
    result = result.replace("-mod#", 'modified from >> ')
    result = result.replace("+mod#", 'modified to >> ')
    result = result.replace("=eql#", '')
    return result
