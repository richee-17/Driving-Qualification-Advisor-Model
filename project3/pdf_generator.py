
from fpdf import FPDF
import datetime
from io import BytesIO

def generate_pdf(input_data, labels, prediction_text):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Driving Qualification Report", ln=True, align="C")

    # Timestamp
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
    pdf.ln(10)

    # Result
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, f"Prediction: {prediction_text}", ln=True)
    pdf.ln(5)

    # Inputs
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "User Inputs:", ln=True)
    pdf.set_font("Arial", "", 11)
    for label, value in zip(labels, input_data[0]):
        pdf.cell(200, 8, f"{label}: {value}", ln=True)

    # Create binary PDF data
    pdf_bytes = BytesIO()
    pdf_output = pdf.output(dest='S').encode('latin-1')
    pdf_bytes.write(pdf_output)
    pdf_bytes.seek(0)
    return pdf_bytes
