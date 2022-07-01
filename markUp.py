import difflib


def markUpDifferences(string_a, string_b):
    """

    :param string_a: String one to compare
    :param string_b: String two to compare :return: String A, String B after
    marking both strings with <insert>,<replace> and <delete> tags by comparing the differences between the two
    strings.

    Any text that is present in string_a but not string_b is marked with a <delete> markup tag.
    Any text that is present in string_b but not string_a is marked with a <insert> markup tag.
    Any text that is neither present in string_a but nor string_b is marked with a <replace> markup tag.
    """
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



def mark_red(string):
    """

    :param string: String to be marked
    :return: returns a String with markup tags

    Function appends <delete></delete> markup tags to the input strings as prefix and suffix to return a marked string.
    """
    return f'<delete>{string}</delete>'


def mark_green(string):
    """

    :param string: String to be marked
    :return: returns a String with markup tags

    Function appends <insert></insert> markup tags to the input strings as prefix and suffix to return a marked string.
    """
    return f'<insert>{string}</insert>'


def mark_yellow(string):
    """

    :param string: String to be marked
    :return: returns a String with markup tags

    Function appends <replace></replace> markup tags to the input strings as prefix and suffix to return a marked string.
    """
    return f'<replace>{string}</replace>'

