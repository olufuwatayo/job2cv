# fetch the job
import requests
from bs4 import BeautifulSoup
import pdfkit
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
import html
i = 1
while i < 2:
    url = input("enter job url:") #"https://careers.chop.edu/job/Philadelphia-D3b-DevOps-Engineer-PA-19146/641374900" #input("enter the job url here:")
    page = requests.get(url,verify=False)
    #get content after a string (experience or skil)
    soup = BeautifulSoup(page.text, 'html.parser')
    #parse it and assign it to content
    content  = (soup.get_text())
    contentencode = html.unescape(content)
    f = open("jd.txt", "a")
    f.write(contentencode)
    f.close()
    # Remove extra spaces from resume
    fin = open("jd.txt", "rt")  
    fout = open("jdmodified.txt", "wt")
    for line in fin:
        fout.write(' '.join(line.split()))
    fin.close()
    fout.close()

    pdf = FPDF() 
    pdf.add_page() 
    pdf.set_text_color(255,255,255)
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 0.1)
    f = open("jdmodified.txt", "r")
    #f = contentencode
    for x in f:
        pdf.write(1, x)
    #pdf.ln(1)  

    pdf.output("jd.pdf")   
    #Merge both pdf together
    pdfs = ['oye1.pdf', 'jd.pdf']
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("oye-resume.pdf")
    merger.close()
