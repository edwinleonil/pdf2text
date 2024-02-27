from PyPDF2 import PdfReader
import os

reader = PdfReader(r"G:\My Drive\AMRC Projects\Griding and linishsing automation\Development_of_artificial_neural_network.pdf")
number_of_pages = len(reader.pages)
path2save = 'text_output'
file_name = 'Development_of_artificial_neural_network.txt'
# read all pages and save as a single txt file
with open(os.path.join(path2save, file_name), 'w', encoding='utf-8') as f:
    for i in range(number_of_pages):
        f.write(reader.pages[i].extract_text())
        f.write("\n")

