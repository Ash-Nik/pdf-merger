from PyPDF2 import PdfWriter, PdfFileReader
import os


def arrange(c):
    l = []
    for i in range(1, c + 1):  # Start from 1, not 0
        x = int(input(f"Write the sequence of {i} pdf = "))
        l.append(x - 1)
    return l


folder_path = "PDFS"
output_filename = "merged-pdf.pdf"

file2 = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]
c = len(file2)

print(f"Total files present in the folder = {c}")

print("Do you want to change the sequence of the pdf? (Y/N)")
choice = input("Enter your choice: ").upper()

merger = PdfWriter()

if choice == 'Y':
    print(f"Your folder contains {c} files. Enter the position of each PDF, e.g., 1, 6, 3, 5, ...")
    l = arrange(c)
    print("User input sequence:", l)

    l3 = []
    for i in l:
        l3.append(file2[i])
    print("Selected PDF files:", l3)

    for pdf in l3:
        merger.append(os.path.join(folder_path, pdf))

else:
    for pdf in file2:
        merger.append(os.path.join(folder_path, pdf))

merger.write(output_filename)
merger.close()

print(f"Merged PDF saved as {output_filename}")
