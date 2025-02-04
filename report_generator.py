from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import logging
from datetime import datetime

class ReportGenerator:
    def __init__(self, output_filename="report.pdf"):
        self.output_filename = output_filename
        self.styles = getSampleStyleSheet()
        self.elements = []
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def add_title(self, title):
        self.logger.info(f"Adding title: {title}")
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30
        )
        self.elements.append(Paragraph(title, title_style))
        self.elements.append(Spacer(1, 12))

    def add_header(self, text):
        self.elements.append(Paragraph(text, self.styles['Heading2']))
        self.elements.append(Spacer(1, 12))

    def add_paragraph(self, text):
        self.elements.append(Paragraph(text, self.styles['Normal']))
        self.elements.append(Spacer(1, 12))

    def add_table(self, data, col_widths=None):
        self.logger.info("Adding table to report")
        if not data:
            self.logger.warning("Empty data provided for table")
            return

        if not col_widths:
            col_widths = [2*inch] * len(data[0])

        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        self.elements.append(table)
        self.elements.append(Spacer(1, 20))

    def generate_pdf(self):
        self.logger.info(f"Generating PDF: {self.output_filename}")
        try:
            doc = SimpleDocTemplate(
                self.output_filename,
                pagesize=letter,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            # Add timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.add_paragraph(f"Generated on: {timestamp}")
            
            # Build the document
            doc.build(self.elements)
            self.logger.info("PDF generation completed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error generating PDF: {str(e)}")
            raise
