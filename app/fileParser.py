import re

def getSequences(filePath):
    file = open(filePath, "r")

    sequences = []

    sequenceLines = file.readlines()
    for sequenceLine in sequenceLines:
        if len(sequenceLine.strip()) != "":
            if sequenceLine[0] != ">":
                sequences.append(sequenceLine.strip())

    return sequences

def generateReadableMatrix(data):
    index = 0
    innerIndex = 0
    line = ""
    f = open('result.html', 'w')
    f.write('<table><tr><th>Sequence Index</th>')
    for number in range(len(data)):
        f.write("<th>#" + str(number+1) + "</th>")
    f.write('</tr>')
    for row in data:
        line += "<tr><th>#" +str(index+1) + "</th>"
        for column in row:
            line += "<td>" + str(column) + "</td>"
            innerIndex += 1
        index += 1
        f.write(line + "</tr>")
        line = ""

    f.write('</table>')
    f.close()