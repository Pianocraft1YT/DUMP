from pypdf import PdfReader
import re as re
reader = PdfReader("check.pdf")
number_of_pages = len(reader.pages)
i = 0
while (i < number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    lines = text.split('\n')
    i+=1
    for line in lines:
        # 1. Find lines containing parentheses
        if "(" in line and ")" in line:
            print(f"Line with parentheses: {line}")