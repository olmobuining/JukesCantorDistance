import math

def jukesCantor(sequenceOne, sequenceTwo):
    difference = 0
    length = 0

    for i in range(min(len(sequenceOne), len(sequenceTwo))):
        if sequenceOne[i] != '-' and sequenceTwo[i] != '-' and sequenceOne[i] != 'N' and sequenceTwo[i] != 'N':
            length += 1
            if sequenceOne[i] != sequenceTwo[i]:
                difference += 1

    # In case there is no sequence alignment
    if float(length) == 0:
        return 0

    percentage = float(difference) / float(length)
    jukesCantorResult = float(-3.0/4.0 * math.log(1 - (4.0/3.0 * percentage)))
    if jukesCantorResult*100 > 4 or jukesCantorResult == 0:
        return 0
    
    return jukesCantorResult


def compareSequences(sequences):
    matrix = [[sequences for x in range(len(sequences))] for x in range(len(sequences))]
    for index in range(len(sequences)):
        for compareToIndex in range(len(sequences)):
            matrix[index][compareToIndex] = jukesCantor(sequences[index], sequences[compareToIndex])

    return matrix

