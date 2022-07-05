import difflib
from markUp import markUpDifferences
from pdfParser import pdfparser
import fuzzyCompare
import pandas as pd


def diffReport(path_file_a, path_file_b, path_file_output='', html_return=True, partial_ratio="tokenSortRatio"):
    """

    :param path_file_a: Path for the File A to be compared.
    :param path_file_b: Path for the File B to be compared.
    :param path_file_output: Path of the directory where the output HTML file needs to be saved. (Default: 'Output/')
    :param html_return: Boolean to select if the function returns HTML of the report. (True by default)
    :param partial_ratio: Partial Ratio Type, Accepted Values are ("Ratio", "qRatio", "wRatio", "ratio_2", "tokenSetRatio", "tokenSortRatio", "partialTokenSortRatio", "default")
    :return: HTML for the report if html_return is set to True.  If set to false, it will return the DataFrame.

    Function takes two PDF file paths as input, and generates a difference report with the lines that are different
    in the two files, and also highlighting the differences in an HTML table with colors to represent content that
    was Added, Removed or changed.

    Any text that is present in File_a but not File_b is marked in Red.
    Any text that is present in File_b but not File_a is marked in Green.
    Any text that is neither present in string_a but nor string_b is marked in Yellow.
    """

    text_extract_a = pdfparser(path_file_a)  # Extract contents of PDF as string
    text_extract_b = pdfparser(path_file_b)  # Extract contents of PDF as string

    #f = open('Temp/Text_Input1.txt', 'w')
    #f.write(text_extract_a)
    #f.close()
    #f = open('Temp/Text_Input2.txt', 'w')
    #f.write(text_extract_b)
    #f.close()

    # text_lines_a = open('Temp/Text_Input1.txt').readlines()
    # text_lines_b = open('Temp/Text_Input2.txt').readlines()

    text_lines_a = text_extract_a.split('\n')
    text_lines_b = text_extract_b.split('\n')

    junk = ['', ' ', '   ', '\t', '                                                                                                                 ']
    text_lines_a = [x for x in text_lines_a if x not in junk]
    text_lines_b = [x for x in text_lines_b if x not in junk]

    df = pd.DataFrame(columns=['File1', 'File2', 'Ratio', 'Partial Ratio'])
    count = 0
    for (i, j) in zip(text_lines_a, text_lines_b):
        a = i
        b = difflib.get_close_matches(a, text_lines_b, n=1)
        if b:
            b = b[0]
        else:
            b = ''
        ratio = fuzzyCompare.ratio(a, b)
        ratio_2 = fuzzyCompare.ratio(a, b, partial_ratio)
        if a != b:
            a, b = markUpDifferences(a, b)
            df.loc[count] = [a, b, ratio, ratio_2]
        count += 1
    df.reset_index(drop=True)

    # path_file_output
    if html_return:
        return html_output(df, path_file_output)

    else:
        return df


def html_output(df, path_file_output):
    """

    :param df: Data Frame to be displayed as an HTM Table
    :param path_file_output: Path of the directory where the output HTML file needs to be saved. (Default: 'Output/')
    :return: Returns the HTML for the table generated.

    The function accepts the Data frame as an argument to iterate through the rows and generate an HTML table with
    the contents of the dataframe and linking it with the CSS file form the Resources folder.

    """
    diff_report = open(path_file_output + "diffReport.html", 'w')
    diff_report.write("<html>\n")
    diff_report.close()

    #css_file = open("Resources/table.css", 'r')
    #css = css_file.read()
    #css_file.close()
    #css_file = open(path_file_output + "table.css", 'w')
    #css_file.write(css)

    iterreport = open(path_file_output + "diffReport.html", 'a')
    iterreport.write('<head>\n<style>\nbody{font:1.2em normal Arial,sans-serif;color:#34495E;}replace {'
                     'background-color: yellow;color: black;}insert {background-color: lightgreen;color: '
                     'black;}delete {background-color: pink;color: black;}h1{'
                     'text-align:center;text-transform:uppercase;letter-spacing:-2px;font-size:2.5em;margin:20px '
                     '0;}.container{width:90%;margin:auto;}table{border-collapse:collapse;width:100%;}.blue{'
                     'border:2px solid #1ABC9C;}.blue thead{background:#1ABC9C;}thead{color:white;}th,'
                     'td{text-align:center;padding:5px 0;}tbody tr:nth-child(even){background:#ECF0F1;}tbody '
                     'tr:hover{background:#BDC3C7;color:#FFFFFF;}.fixed{'
                     'top:0;position:fixed;width:auto;display:none;border:none;}.scrollMore{margin-top:600px;}.up{'
                     'cursor:pointer;}\n</style></head>')
    iterreport.write("<body>")
    iterreport.write('<table class="blue" border = 1>\n')
    iterreport.write("<tbody>\n")
    iterreport.write('\t<tr style = "background-color : #1ABC9C">\n')
    iterreport.write(f'\t\t<th>Line Number</th>\n')
    iterreport.write(f'\t\t<td>File 1</td>\n')
    iterreport.write(f'\t\t<td>File 2</td>\n')
    iterreport.write(f'\t\t<td>Ratio</td>\n')
    iterreport.write(f'\t\t<td>Partial Ratio</td>\n')

    iterreport.write("\t</tr>\n")
    for index, row in df.iterrows():
        iterreport.write("\t<tr>\n")
        iterreport.write(f'\t\t<th>{index}</th>\n')
        iterreport.write(f'\t\t<td>{str(row["File1"]).strip()}</td>\n')
        iterreport.write(f'\t\t<td>{str(row["File2"]).strip()}</td>\n')
        iterreport.write(f'\t\t<td>{str(row["Ratio"]).strip()}</td>\n')
        iterreport.write(f'\t\t<td>{str(row["Partial Ratio"]).strip()}</td>\n')
        iterreport.write("\t</tr>\n")
    iterreport.write("</tbody>\n")
    iterreport.write("</table>\n")
    iterreport.write("</body>\n")
    iterreport.write("</html>\n")
    iterreport.close()

    diff_report = open(path_file_output + "diffReport.html", 'r')
    ret = diff_report.read()
    diff_report.close()

    return ret


if __name__ == '__main__':
    x = diffReport("Example/Input/SampleContract1.pdf", "Example/Input/SampleContract2.pdf", html_return=True)

    # print(x)
