import difflib
from pdfParser import pdfparser
import fuzzyCompare
import pandas as pd


def diffReport(path_file_a, path_file_b, path_file_output = 'Output/diffReport.html', output_file=True):
    text_extract_a = pdfparser(path_file_a)
    text_extract_b = pdfparser(path_file_b)

    f = open('Temp/Text_Input1.txt', 'w')
    f.write(text_extract_a)
    f.close()
    f = open('Temp/Text_Input2.txt', 'w')
    f.write(text_extract_b)
    f.close()

    text_lines_a = open('Temp/Text_Input1.txt').readlines()
    text_lines_b = open('Temp/Text_Input2.txt').readlines()

    df = pd.DataFrame(columns=['File1', 'File2', 'Ratio'])
    count = 0
    for (i, j) in zip(text_lines_a, text_lines_b):
        res = fuzzyCompare.ratio(i, j, "partialTokenSortRatio")
        if res < 100:
            df.loc[count] = [i, j, res]
        count += 1
    df.reset_index(drop=True)

    # path_file_output
    diff_report = open(path_file_output, 'w')
    diff_report.write("<html>\n")
    diff_report.close()

    iterreport = open("Output/DfIter.html", 'a')
    iterreport.write('<head>\n<link rel="stylesheet" href="table.css"></head>')
    iterreport.write("<body>")
    iterreport.write('<table class="blue" border = 1>\n')
    iterreport.write("<tbody>\n")
    iterreport.write('\t<tr style = "background-color : #1ABC9C">\n')
    iterreport.write(f'\t\t<th>Line Number</th>\n')
    iterreport.write(f'\t\t<td>File 1</td>\n')
    iterreport.write(f'\t\t<td>File 2</td>\n')
    iterreport.write(f'\t\t<td>Ratio</td>\n')
    iterreport.write("\t</tr>\n")
    for index, row in df.iterrows():
        if index == 11:
            row["File1"] = f'{row["File1"][:5]}<mark>{row["File1"][5:10]}</mark>{row["File1"][10:]}'
        iterreport.write("\t<tr>\n")
        iterreport.write(f'\t\t<th>{index}</th>\n')
        iterreport.write(f'\t\t<td>{str(row["File1"]).strip()}</td>\n')
        iterreport.write(f'\t\t<td>{str(row["File2"]).strip()}</td>\n')
        iterreport.write(f'\t\t<td>{str(row["Ratio"]).strip()}</td>\n')
        iterreport.write("\t</tr>\n")
    iterreport.write("</tbody>\n")
    iterreport.write("</table>\n")
    iterreport.write("</body>")
    iterreport.write("</html>\n")
    iterreport.close()

