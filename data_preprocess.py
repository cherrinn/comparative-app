import csv

feature= []
target = []
with open("data/matched_scope_dataset.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)    #header skipe
    for row in reader:
        feature.append([float(row[0]), float(row[1])])
        target.append(row[2])
print("read finish the file!")

#--------------------------------------------------------------------------------------------------------------------------------#
grid_lon = []
grid_lat = []

def creatGrid(minLon, maxLon, minLat, maxLat, gridSize):
    if(grid_lon):
        grid_lon.clear()
    if(grid_lat):
        grid_lat.clear()
    while minLon <= maxLon:
        grid_lon.append(minLon)
        minLon += gridSize
    grid_lon.append(minLon)

    while minLat <= maxLat:
        grid_lat.append(minLat)
        minLat += gridSize
    grid_lat.append(minLat)

    print("create grid finish!")

#--------------------------------------------------------------------------------------------------------------------------------#
dict_xTrain = {}
dict_xTest = {}
dict_yTrain = {}
dict_yTest = {}

def findGrid(feature_train, target_train, feature_test, target_test):
    posLon = 0
    posLat = 0
    posLon_t = 0
    posLat_t = 0

    if(dict_xTrain):
        dict_xTrain.clear()
    if(dict_xTest):
        dict_xTest.clear()
    if(dict_yTrain):
        dict_yTrain.clear()
    if(dict_yTest):
        dict_yTest.clear()
    
    for latLon,t in zip(feature_train, target_train):
        for i, gLon in enumerate(zip(grid_lon, grid_lon[1:])):
            if(latLon[0] > gLon[0] and latLon[0] < gLon[1]):
                posLon = i+1
        for j, gLat in enumerate(zip(grid_lat, grid_lat[1:])):
            if(latLon[1] > gLat[0] and latLon[1] < gLat[1]):
                posLat = j+1

        dict_xTrain.setdefault((str(posLon)+"_"+str(posLat)),[]).append(latLon)
        dict_yTrain.setdefault((str(posLon)+"_"+str(posLat)),[]).append(t)

    
    for latLon,t in zip(feature_test, target_test):
        for i, gLon in enumerate(zip(grid_lon, grid_lon[1:])):
            if(latLon[0] > gLon[0] and latLon[0] < gLon[1]):
                posLon_t = i+1
        for j, gLat in enumerate(zip(grid_lat, grid_lat[1:])):
            if(latLon[1] > gLat[0] and latLon[1] < gLat[1]):
                posLat_t = j+1

        dict_xTest.setdefault((str(posLon_t)+"_"+str(posLat_t)),[]).append(latLon)
        dict_yTest.setdefault((str(posLon_t)+"_"+str(posLat_t)),[]).append(t)

    print("find grid finish!!")
