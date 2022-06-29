import difflib


def mark_red(string):
    return f'<delete>{string}</delete>'


def mark_green(string):
    return f'<insert>{string}</insert>'


def mark_yellow(string):
    return f'<replace>{string}</replace>'


def markUpDifferences(string_a, string_b):
    s = difflib.SequenceMatcher(None, string_a, string_b)
    a_mark = [0] * len(string_a)  # Array to mark each index of StringA as either Delete, Insert, Replace or no change
    b_mark = [0] * len(string_b)  # Array to mark each index of StringB as either Delete, Insert, Replace or no change

    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == "delete":
            for n in range(i1, i2):
                a_mark[n] = "-"
        if tag == "insert":
            for n in range(j1, j2):
                b_mark[n] = "+"
        if tag == "replace":
            for n in range(i1, i2):
                a_mark[n] = "?"
            for n in range(j1, j2):
                b_mark[n] = "?"

    a_new = ''
    b_new = ''

    for n in range(len(a_mark)):
        if a_mark[n] == 0:
            a_new += (string_a[n])
        elif a_mark[n] == '-':
            a_new += (mark_red(string_a[n]))
        elif a_mark[n] == '?':
            a_new += (mark_yellow(string_a[n]))
        elif a_mark[n] == '+':
            a_new += (mark_green(string_a[n]))

    a_new = a_new.replace("</delete><delete>", "")
    a_new = a_new.replace("</replace><replace>", "")
    a_new = a_new.replace("</insert><insert>", "")

    for n in range(len(b_mark)):
        if b_mark[n] == 0:
            b_new += (string_b[n])
        elif b_mark[n] == '-':
            b_new += (mark_red(string_b[n]))
        elif b_mark[n] == '?':
            b_new += (mark_yellow(string_b[n]))
        elif b_mark[n] == '+':
            b_new += (mark_green(string_b[n]))

    b_new = b_new.replace("</delete><delete>", "")
    b_new = b_new.replace("</replace><replace>", "")
    b_new = b_new.replace("</insert><insert>", "")

    return a_new, b_new
