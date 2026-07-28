from pypdf import PdfReader

reader = PdfReader("resume.pdf")

print("Total Pages:", len(reader.pages))

for i, page in enumerate(reader.pages):
    text = page.extract_text()

    print(f"\n----- Page {i+1} -----")
    print(repr(text))