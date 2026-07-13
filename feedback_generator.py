from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_feedback_pdf(name, score, matched, missing):
    """Generate personalized feedback certificate for each candidate."""
    fname = f"{name}_feedback.pdf"
    c = canvas.Canvas(fname, pagesize=A4)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(70, 780, "SMART ATS FEEDBACK CERTIFICATE")
    c.setFont("Helvetica", 12)
    c.drawString(70, 740, f"Candidate: {name}")
    c.drawString(70, 720, f"JD Match Score: {score}%")
    c.drawString(70, 700, "Strengths:")
    c.setFont("Helvetica", 11)
    c.drawString(90, 680, matched if matched else "None listed")
    c.setFont("Helvetica", 12)
    c.drawString(70, 660, "Areas to Improve:")
    c.setFont("Helvetica", 11)
    c.drawString(90, 640, missing if missing else "None listed")
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(70, 600, "Thank you for using Smart ATS 2.0 — Empowering AI-driven hiring.")
    c.showPage(); c.save()
    return fname