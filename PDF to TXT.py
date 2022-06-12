from PyPDF2 import PdfFileReader,PdfFileWriter

file_path = "sample.pdf"
pdf = PdfFileReader(file_path)
file_name = file_path.strip('.pdf')+'.txt'

with open(file_name, 'w') as file: 
    for page_num in range(pdf.numPages):  
        pageObj = pdf.getPage(page_num)
        try:
            txt = pageObj.extract_text()
        except:
            pass
        else:
            file.write('\n--------------- Page {0} ----------------'.format(page_num+1))
            file.write('\n')
            file.write(txt)
    print("PDF with",pdf.numPages,"pages converted to txt and saved as", file_name)      
    print(pdf.getDocumentInfo)  
    file.close()