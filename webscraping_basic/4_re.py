import re

p = re.compile("ca.e")
# . (ca.e): 하나의 문자 > care, cafe, acse
# ^ (^de) : 문자열의 시작 > desk, dete, delp
# $ (se$) : 문자열의 끝 > case, oise, djse


def print_match(m):
    if m:
        print("m.group():", m.group())
        print("m.string:", m.string)
        print("m.start:", m.start())
        print("m.end:", m.end())
        print("m.span():", m.span())
    else:
        print("노매칭")


# m = p.match("case")
# print_match(m)

# m = p.search("good care")
# print_match(m)

# lst = p.findall("good care cafe")
# print(lst)
