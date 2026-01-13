from pdfminer.high_level import extract_text

text = extract_text("sample.pdf")
# print(text)
with open("output.txt", "w", encoding="utf-8") as out_file:
    out_file.write(text)