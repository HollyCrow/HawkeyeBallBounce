import numpy as np

from Bounce import Bounce
import csv

# TODO: This needs to be rewritten FAR more robustly. The actual CSVs are a complete mess and that needs to be accounted for.
# To parse a csv line into a Bounce object. "row" is a csv row, NOT A STRING!
def readLine(row):
    # print(row)
    bounce = Bounce()
    bounce.bowlerReleaseSpeed = float(row[5])
    bounce.bouncePos = np.array([float(row[6]), float(row[7])])
    bounce.stumpsPos = np.array([float(row[8]), float(row[9])])
    bounce.swing = float(row[10])
    bounce.deviation = float(row[11])
    bounce.shotLandingPos = np.array([float(row[13]), float(row[14])])
    bounce.bounceVelocity = float(row[17])
    bounce.outOfBounceAngle = float(row[20])
    bounce.dropAngle = float(row[21])
    bounce.angleLeavingBowlersHand = float(row[25])
    bounce.bowlerReleasePos = np.array([float(row[28]), float(row[29])])
    bounce.acceleration = np.array([float(row[30]), float(row[31])])

    return bounce

def readData(filename="data.csv"):
    bounces = []
    with open(filename, newline="") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",", quotechar="|")
        for row in csvReader:
            bounces.append(readLine(row))
    return bounces
