from fpdf import FPDF
from fpdf.enums import XPos, YPos

def pdf_generation(file_name, title, date, agenda):
	class PDF(FPDF):
		def header(self):
			if (pdf.page_no() == 1):
				# self.image('summeet_package\static\img\SumMeet-logos_black.png', 3, 2, 40)
				self.image('summeet_package\static\img\SumMeet-6.png', 8, 2, 40)
				# self.image('summeet_package\static\img\SumMeet-logos.jpeg', 10, 8, 35)

				# font
				self.set_font('helvetica', 'B', 20)
				# Padding
				self.cell(70)
				# Title
				self.cell(70, 10, 'Minutes Of Meeting', border=True,
						new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
				# Line break
				self.set_font('helvetica', 'BI', 11)
				self.ln(20)
				self.cell(30,20,'Title:     '+title)
				self.ln(10)
				self.cell(30,20,'Date:     '+date)
				self.ln(15)
				# self.multi_cell(30,20,'Agenda:\t\t\t\t\t'+agenda)
				self.multi_cell(200, 10, 'Agenda:     '+agenda)
				self.ln(10)

		# Page footer
		def footer(self):
			# Set position of the footer
			self.set_y(-15)
			# set font
			self.set_font('helvetica', 'I', 8)
			# Page number
			self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

			


				# Create a PDF object
	pdf = PDF('P', 'mm', 'Letter')
	# get total page numbers
	pdf.alias_nb_pages()

	# Set auto page break
	pdf.set_auto_page_break(auto=True, margin=15)

	# Add Page
	pdf.add_page()
	# pdf.page_no()
	# specify font
	pdf.set_font('helvetica', 'BIU', 16)

	pdf.set_font('times', '', 12)

	file = open("summeet_package/summarized_files/"+file_name+".txt", "r")
	# insert the texts in pdf
	for g in file:
		pdf.multi_cell(200, 10, txt=g, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

	pdf.output('summeet_package/generated_pdfs/'+file_name+'.pdf')
