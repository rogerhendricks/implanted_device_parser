from PyPDF2 import PdfFileReader
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

        page_1 = pdf.getPage(1)
        print(page_1)
        print('Page type: {}'.format(str(type(page_1))))
        text = page_1.extractText()
        print(text)

        page_2 = pdf.getPage(2)
        print(page_2)
        print('Page type: {}'.format(str(type(page_2))))
        text2 = page_2.extractText()
        print(text2)
    print(info)
    print(number_of_pages)
if __name__ == '__main__':
    # path = r'moving over\examples\medtronic\COWIE_Melissa_19751122_NA_20200625000500_ER_1.pdf'
    path = r'C:\Users\20019301\Desktop\xml_report\moving over\examples\medtronic\XERRI_Joseph_19461004_NA_20200624110010_CPR_1.pdf'
    get_info(path)