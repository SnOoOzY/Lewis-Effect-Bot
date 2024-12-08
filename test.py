import csv
<<<<<<< Updated upstream
<<<<<<< Updated upstream
import math
import random
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

userStats = []
global userName
global userPointsIn

<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
fieldNames = ['Name', 'Score']

>>>>>>> Stashed changes
=======
fieldNames = ['Name', 'Score']

>>>>>>> Stashed changes
userName = input('Gimmeurname: ')
userPointsIn = int(input('Points:'))



def loadPoints():
    with open('stats.csv', 'r', newline='') as csvFile:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        reader = csv.DictReader(csvFile)
        for row in reader:
            userStats.append(row)

    
=======
=======
>>>>>>> Stashed changes
        reader = csv.DictReader(csvFile, fieldnames=fieldNames)
        next(reader)
        for row in reader:
            storedScore = int(row['Score'])
            storedName = row['Name']




<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
def savePoints():
    with open('stats.csv', 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames = ['Name', 'Score'])
        writer.writeheader()
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        writer.write({'Name': userName, 'Score': userPointsIn})
=======
=======
>>>>>>> Stashed changes
        writer.writerow({'Name': userName, 'Score': userPointsIn})



<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes


loadPoints()
savePoints()
print(userStats)