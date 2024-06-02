import base64

def pdf_to_base64(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read()).decode('utf-8')
    return encoded_string

if __name__ == "__main__":
    pdf_path = "A01_Sicherheitsleitlinie.pdf"
    encoded_pdf = pdf_to_base64(pdf_path)
    print(encoded_pdf)
