from PyPDF2 import PdfReader

# Buka file PDF dan baca semua halaman
with open("NamaFilePdf.pdf", "rb") as pdfFileObj:
    reader = PdfReader(pdfFileObj)
    all_text = ""

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        all_text += f"\n\n--- Halaman {i+1} ---\n{text if text else '[Halaman kosong atau tidak bisa diekstrak]'}"

# Tampilkan hasilnya di terminal
print(all_text)

with open("hasil_ekstrak.txt", "w", encoding="utf-8") as output:
    output.write(all_text)
