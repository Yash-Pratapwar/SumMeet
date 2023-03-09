# Python program to create
# a pdf file


from fpdf import FPDF


# save FPDF() class into a
# variable pdf
pdf = FPDF( 'P', 'mm', 'A4' )

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# create a cell
pdf.cell(175, 10, txt = "SumMeet",
		ln = 1, align = 'R')

# add another cell
pdf.cell(200, 10, txt = "Meeting Minutes",
		ln = 1, align = 'L')
pdf.line(x1=10, y1=2, x2=-10, y2=2)
# save the pdf with name .pdf
pdf.output("GFG.pdf")
