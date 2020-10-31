import pyttsx3
import PyPDF2
#the pdf name
book = open('py.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
#print the number of pages in the pdf
print(pages)
speaker = pyttsx3.init()
#if you wanna choose from where to start the reading
page = pdfReader.getPage(14) #reading page i+1
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
