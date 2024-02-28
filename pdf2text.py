from PyPDF2 import PdfReader
import os

pdf_file_path = r"G:\Shared drives\Quantum Computing - IMG\Research\A Study on the basics of Quantum Computing.pdf"

reader = PdfReader(pdf_file_path)
number_of_pages = len(reader.pages)

# get the name of the file and rename it with a txt extention for the saving name
file_name = os.path.basename(pdf_file_path).split('.')[0] + '.txt'

path2save = 'text_output'

# read all pages and save as a single txt file
with open(os.path.join(path2save, file_name), 'w', encoding='utf-8') as f:
    for page in reader.pages:
        text = page.extract_text()
        if text.strip():  # Check if the extracted text is not empty or contains only whitespace
            lines = text.strip().split("\n")  # Split the text into lines
            for line in lines:
                if line.strip().isdigit():  # Check if the line contains only digits (page number)
                    continue  # Skip writing the line if it is a page number
                f.write(line.strip() + " ")  # Write the stripped line to the file with a space
                f.write("\n")

print(f"Text extracted from {number_of_pages} pages and saved as {file_name} in {path2save}")


# load the text file 
with open(os.path.join(path2save, file_name), 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # remove the empty lines 
    lines = [line.strip() for line in lines if line.strip()]
    # add empty line before each line that starts with a number
    updated_lines = []
    for line in lines:
        if line.strip().isdigit():  # Check if the line contains only digits (page number)
            updated_lines.append("")  # Add empty line before the line
        updated_lines.append(line)  # Keep the line as it is
    # save the updated text file
    with open(os.path.join(path2save, file_name), 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
print(f"Empty line added before each line that starts with a number in {file_name} in {path2save}")
