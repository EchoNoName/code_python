import random
def createMap():
    '''Generates a Map with 15 floors with unique events for each room generated, the rooms are also connected with no crossing paths, the map is a 15 x 7 grid of dots that are connected with unused dots being removes, the x locations ranges from [0, 6] while the floors have a y value ranging from [1, 15]

    args: none

    returns:
        map: A dictonary that contains a dictonary with the main key representing the floor and the secondary key representing the room and the value being the type of room
        path: A dictonary that has a key representing the location of a room (floor, room) and the value is a list of all the rooms it is connected to
        mapDisplay: A visualization of the map made of 28 strings
    '''
    map = {
        1: {},
        2: {},
        3: {},
        4: {},
        5: {},
        6: {},
        7: {},
        8: {},
        9: {},
        10: {},
        11: {},
        12: {},
        13: {},
        14: {},
        15: {},
    }
    # Initialized the Map
    # The map is a dictionary with keys that represent the floor with a another dictonary as its value with the keys representing the room number and the value representing the room type
    # room type: 0 = placeholder, 1 = normal combat, 2 = event, 3 = elite combat, 4 = shop, 5 = chest, 6 = campfire
    def compPathGen(map):
        '''Generates the complete paths that determains which rooms are connected with which

        args: 
            map: dictionary with keys that represent the floor with a another dictonary as its value with the keys representing the room number and the value representing the room type
        
        returns:
            map: Same map but with filled nested dictonaries of where all the rooms are located
        '''
        path = {}
        def nonOverlapPath(path, room, floor):
            '''Generates a value that makes sure the path that either foes left, straight or right doesn't crosses over with any existing paths
            
            args: 
                path: All current generated paths represented by a dictonary with a tuple (floor, room x value) as the key and a list [room1, room2...] of lists [floor, room x value] representing all the rooms it connects to
                room: The current room location ranging from 0 - 6
                floor: The current floor ranging from 1 - 14
            
            returns:
                connection: The variation is the x value that determains whether the path goes left, straight or right
            '''
            while True:
                if room == 0:
                    connection = random.randint(0, 1)
                elif room == 6:
                    connection = random.randint(-1, 0)
                else:
                    connection = random.randint(-1, 1)
                if connection == 0:
                    break
                else:
                    if (floor, room + connection) not in path:
                        break
                    else:
                        if [floor + 1, room] not in path[floor, room + connection]:
                            break
            return connection
        start = [0, 1, 2, 3, 4, 5, 6]
        for i in range(0, 6):
            floor = 1
            if i < 2:
                room = random.choice(start)
                start.remove(room)
            else:
                room = random.randint(0, 6)
            while floor < 15:
                connection = nonOverlapPath(path, room, floor)
                if room not in map[floor]:
                    if floor == 1:
                        map[floor][room] = 1
                    elif floor == 9:
                        map[floor][room] = 5
                    elif floor == 15:
                        map[floor][room] = 6
                    else:
                        map[floor][room] = 0
                if (room + connection) not in map[floor + 1]:
                    if floor + 1 == 9:
                        map[floor + 1][room + connection] = 5
                    elif floor + 1 == 15:
                        map[floor + 1][room + connection] = 6
                    else:
                        map[floor + 1][room + connection] = 0
                if (floor, room) in path:
                    if [floor + 1, room + connection] not in path[floor, room]:
                        path[floor, room].append([floor + 1, room + connection])
                else: 
                    path[floor, room] = []
                    path[floor, room].append([floor + 1, room + connection])
                floor += 1
                room = room + connection
        return path, map
    path, map = compPathGen(map)
    for floor in range(2, 9):
        for room in map[floor].keys():
            i = random.randint(1, 100)
            if i <= 45:
                map[floor][room] = 1
            elif i <= 67:
                map[floor][room] = 2
            elif i <= 83:
                map[floor][room] = 3
            elif i <= 95:
                map[floor][room] = 6
            else:
                map[floor][room] = 4
    for floor in range(10, 15):
        for room in map[floor].keys():
            i = random.randint(1, 100)
            if i <= 45:
                map[floor][room] = 1
            elif i <= 67:
                map[floor][room] = 2
            elif i <= 83:
                map[floor][room] = 3
            elif i <= 95:
                map[floor][room] = 6
            else:
                map[floor][room] = 4

    def nonValidMapFix(map):
        floor = 14
        for room in map[floor].keys():
            if map[floor][room] == 6:
                i = random.randint(1, 100)
            if i <= 45:
                map[floor][room] = 1
            elif i <= 67:
                map[floor][room] = 2
            elif i <= 83:
                map[floor][room] = 3
            elif i <= 95:
                map[floor][room] = 6
            else:
                map[floor][room] = 4
    
    i = 0
    mapDisplay = []
    pathDisplay = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    for start, end in path.items():
            startFloor, startRoom = start
            i = startFloor - 1
            for connected in end:
                endRoom = connected[1]
                if startRoom == endRoom:
                    pathDisplay[i][startRoom * 2] = '|'
                elif endRoom < startRoom:
                    pathDisplay[i][startRoom * 2 - 1] = '\\'
                else:
                    pathDisplay[i][startRoom * 2 + 1] = '/'
    for floor, room in map.items():
        floorDisplay = ''
        for i in range(0, 7):
            if i not in room:
                floorDisplay += '  '
            else:
                floorDisplay += f'{room[i]} '
        mapDisplay.append(floorDisplay)
        if floor < 15:
            mapDisplay.append(''.join(pathDisplay[floor - 1]))



    return map, path, mapDisplay
map, path, mapDisplay = createMap()
print(map)
for i in reversed(mapDisplay):
    print(i)