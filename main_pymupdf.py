import pymupdf

file = "sample.pdf"

with pymupdf.open(file) as doc:
    with open("output.txt", "w", encoding="utf-8") as out_file:
        for page in doc[:2]:
            text = page.get_text("blocks")
            # print(text)
            for block in text:
                out_file.write(block[4])
