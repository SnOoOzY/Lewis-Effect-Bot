import csv
import math
import random

userStats = []
global userName
global userPointsIn

userName = input('Gimmeurname: ')
userPointsIn = int(input('Points:'))



def loadPoints():
    with open('stats.csv', 'r', newline='') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            userStats.append(row)

    
def savePoints():
    with open('stats.csv', 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames = ['Name', 'Score'])
        writer.writeheader()
        writer.write({'Name': userName, 'Score': userPointsIn})


loadPoints()
savePoints()
print(userStats)