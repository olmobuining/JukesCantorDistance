from jukesCantor import compareSequences
from fileParser import getSequences
from fileParser import generateReadableMatrix

sequences = getSequences("data.fas")

comparedSequences = compareSequences(sequences)

generateReadableMatrix(comparedSequences)
