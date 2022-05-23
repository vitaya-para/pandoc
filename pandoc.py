from panflute import *
import sys

headers = []

def duplicate(elem, doc):
    if type(elem) == Header:
        if stringify(elem) in headers:
            sys.stderr.write("WARNING: Duplicate elem: " + stringify(elem))
        else:
            headers.append(stringify(elem))


def uppingHeaders(elem, doc):
    if type(elem) == Header and elem.level <= 3:
        return Header(Str(stringify(elem).upper()), level=elem.level)


def replace(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))


if __name__ == "__main__":
    run_filters([duplicate, uppingHeaders], prepare=replace)
