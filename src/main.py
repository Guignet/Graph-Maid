# open the File : Graph.matrix and convert into a matrix (Vector)
MF = open("Graph.matrix","r")
# print(MF.read())
VM = MF.read() # Matrix
MF.close()
# print(VM.split()[0][6])
# while VM.split()[i] != ']'


countV = 0
AV = ord('A')

GF = open("Graph.md",'w')
GF.write("```mermaid\n")

GF.write("graph LR\n")
for E in VM.split():
    # edge management
    GF.write(chr(AV) + '(('+ str(countV) + '))\n')
    AV += 1
    countV += 1


print(countV)



countV = 0
AV = ord('A') # Actual Vertex (start at A)

# vertex management
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
GF.close()
