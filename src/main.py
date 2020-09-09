import markdown
# import pdfkit
import pdfcrowd

# open the File : Graph.matrix and read it in VM
MF = open("Graph.matrix","r")
VM = MF.read()
MF.close()
# print(VM.split()[0][6])
# while VM.split()[i] != ']'


countV = 0 #count number of vertex
AV = ord('A') #name of the first vertex

GF = open("Graph.md",'w')
# GF.write('""""')

# GF.write("~~~mermaid\n")
GF.write("```mermaid\n") #start of the md file
GF.write("graph LR\n")

for E in VM.split():
    # vertices management
    GF.write(chr(AV) + '(('+ str(countV) + '))\n')
    AV += 1
    countV += 1


print(countV)

countV = 0
AV = ord('A') # Actual Vertex (start at A)

# edges management
for E in VM.split():
    VERT = ""
    countE = 0
    for c in E: #extraction of vertices values
    #parsing the string
        if c == '[':
            print('start')
        elif c == ',' :
            print("VERT == 0 ",VERT=="0")
            if VERT != "0":
                GF.write(chr(AV)+" -->|"+ VERT+ "| "+chr(ord('A')+countE)+"\n")
                VERT ="" #init VERT for the next edge value
                countE += 1;
            else:
                VERT ="" #init VERT for the next edge value
                countE += 1;
        elif  c == ']':
            print("end "+chr(AV)+" VERT == 0 ",VERT=="0")
            print("next vertex ")
            if VERT != "0":
                GF.write(chr(AV)+" -->|"+ VERT+ "| "+chr(ord('A')+countE)+"\n")
                VERT ="" #init VERT for the next edge value
                countE += 1;
            else:
                VERT ="" #init VERT for the next edge value
                countE += 1;
        else:#
            VERT += c # we add char c in VERT
    AV += 1
    countV += 1
print(countV)
GF.write("```")
# GF.write("~~~")
# GF.write('""""')
GF.close()


# convertion from md to html then pdf
PDF = open("Graph.md","r")
PDFr = PDF.read()
html = markdown.markdown(PDFr, extensions = ['md_mermaid'])
ToPDF = open('Graph.html','w')
ToPDF.write(html)
ToPDF.write('<script type="text/javascript" src="mermaid.min.js"></script>')
# pdfkit.from_file('Graph.html', 'Graph.pdf')
client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

client.convertFileToFile('Graph.html', 'Graph.pdf')
