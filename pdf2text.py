from PyPDF2 import PdfReader
import os

pdf_file_path = r"G:\My Drive\AMRC Projects\Griding and linishsing automation\papers\Predicting_Surface_Roughness_in_Grinding.pdf"

reader = PdfReader(pdf_file_path)
number_of_pages = len(reader.pages)

# get the name of the file and rename it with a txt extention for the saving name
file_name = os.path.basename(pdf_file_path).split('.')[0] + '.txt'

path2save = 'text_output'

# read all pages and save as a single txt file
with open(os.path.join(path2save, file_name), 'w', encoding='utf-8') as f:
    for i in range(number_of_pages):
        f.write(reader.pages[i].extract_text())
        f.write("\n")

