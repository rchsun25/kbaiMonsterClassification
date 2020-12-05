class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, samples, new_monster):
        #Add your code here!
        #
        #The first parameter to this method will be a labeled list of samples in the form of
        #a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        #the parameters of a particular monster. The second item in each 2-tuple will be a
        #boolean indicating whether this is an example of this species or not.
        #
        #The second parameter will be a dictionary representing a newly observed monster.
        #
        #Your function should return True or False as a guess as to whether or not this new
        #monster is an instance of the same species as that represented by the list.


        #gonna try to do this Version Spaces Style

        specificVersion = {
            'size': [],
            'color': [],
            'covering': [],
            'foot-type': [],
            'leg-count': [],
            'arm-count': [],
            'eye-count': [],
            'horn-count': [],
            'lays-eggs': [],
            'has-wings': [],
            'has-gills': [],
            'has-tail': []
        }
        generalVersion = {
            'size': ['tiny', 'small', 'medium', 'large', 'huge'],
            'color': ['black', 'white', 'brown', 'gray', 'red', 'yellow', 'blue', 'green', 'orange', 'purple'],
            'covering': ['fur', 'feathers', 'scales', 'skin'],
            'foot-type': ['paw', 'hoof', 'talon', 'foot', 'none'],
            'leg-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'arm-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'eye-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'horn-count': [0, 1, 2],
            'lays-eggs': [True, False],
            'has-wings': [True, False],
            'has-gills': [True, False],
            'has-tail': [True, False]
        }

        tree = {}
        #better to do decision tree style

       
        tempCheckList = []
        for color in generalVersion['color']:
            tempCheckList.clear()
            #0 is negative only
            #1 is positive only
            #2 is both/undecided
            #status = 2
            for monster in samples: #monster[0] is data and monster[1] is T/F
                if monster[0]['color'] == color:
                    tempCheckList.append(monster[1])
            if True in tempCheckList and False not in tempCheckList: #positive only
                tree[color] = {'status':1}
            elif False in tempCheckList and True not in tempCheckList: #negative only
                tree[color] = {'status':0}
            elif True in tempCheckList and False in tempCheckList: #undetermined
                tree[color] = {'status':2}
            
                

                for size in generalVersion['size']:
                    tempCheckList.clear()
                    for monster in samples: #monster[0] is data and monster[1] is T/F
                        if monster[0]['size'] == size:
                            tempCheckList.append(monster[1])
                    if True in tempCheckList and False not in tempCheckList: #positive only
                        tree[color][size] = {'status':1}
                    elif False in tempCheckList and True not in tempCheckList: #negative only
                        tree[color][size] = {'status':0}
                    elif True in tempCheckList and False in tempCheckList: #undetermined
                        tree[color][size] = {'status':2}
                
                        

                        for footType in generalVersion['foot-type']:
                            tempCheckList.clear()
                            for monster in samples: #monster[0] is data and monster[1] is T/F
                                if monster[0]['foot-type'] == footType:
                                    tempCheckList.append(monster[1])
                            if True in tempCheckList and False not in tempCheckList: #positive only
                                tree[color][size][footType] = {'status':1}
                            elif False in tempCheckList and True not in tempCheckList: #negative only
                                tree[color][size][footType] = {'status':0}
                            elif True in tempCheckList and False in tempCheckList: #undetermined
                                tree[color][size][footType] = {'status':2}

                                for covering in generalVersion['covering']:
                                    tempCheckList.clear()
                                    for monster in samples: #monster[0] is data and monster[1] is T/F
                                        if monster[0]['covering'] == covering:
                                            tempCheckList.append(monster[1])
                                    if True in tempCheckList and False not in tempCheckList: #positive only
                                        tree[color][size][footType][covering] = {'status':1}
                                    elif False in tempCheckList and True not in tempCheckList: #negative only
                                        tree[color][size][footType][covering] = {'status':0}
                                    elif True in tempCheckList and False in tempCheckList: #undetermined
                                        tree[color][size][footType][covering] = {'status':2}

                                        for legCount in generalVersion['leg-count']:
                                            tempCheckList.clear()
                                            legCountString = str(legCount)
                                            for monster in samples: #monster[0] is data and monster[1] is T/F
                                                if monster[0]['leg-count'] == legCount:
                                                    tempCheckList.append(monster[1])
                                            if True in tempCheckList and False not in tempCheckList: #positive only
                                                tree[color][size][footType][covering][legCountString] = {'status':1}
                                            elif False in tempCheckList and True not in tempCheckList: #negative only
                                                tree[color][size][footType][covering][legCountString] = {'status':0}
                                            elif True in tempCheckList and False in tempCheckList: #undetermined
                                                tree[color][size][footType][covering][legCountString] = {'status':2}

                                                for armCount in generalVersion['arm-count']:
                                                    tempCheckList.clear()
                                                    armCountString = str(armCount)
                                                    for monster in samples: #monster[0] is data and monster[1] is T/F
                                                        if monster[0]['arm-count'] == armCount:
                                                            tempCheckList.append(monster[1])
                                                    if True in tempCheckList and False not in tempCheckList: #positive only
                                                        tree[color][size][footType][covering][legCountString][armCountString] = {'status':1}
                                                    elif False in tempCheckList and True not in tempCheckList: #negative only
                                                        tree[color][size][footType][covering][legCountString][armCountString] = {'status':0}
                                                    elif True in tempCheckList and False in tempCheckList: #undetermined
                                                        tree[color][size][footType][covering][legCountString][armCountString] = {'status':2}

                                                        for eyeCount in generalVersion['eye-count']:
                                                            tempCheckList.clear()
                                                            eyeCountString = str(eyeCount)
                                                            for monster in samples: #monster[0] is data and monster[1] is T/F
                                                                if monster[0]['eye-count'] == eyeCount:
                                                                    tempCheckList.append(monster[1])
                                                            if True in tempCheckList and False not in tempCheckList: #positive only
                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString] = {'status':1}
                                                            elif False in tempCheckList and True not in tempCheckList: #negative only
                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString] = {'status':0}
                                                            elif True in tempCheckList and False in tempCheckList: #undetermined
                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString] = {'status':2}

                                                                for hornCount in generalVersion['horn-count']:
                                                                    tempCheckList.clear()
                                                                    hornCountString = str(hornCount)
                                                                    for monster in samples: #monster[0] is data and monster[1] is T/F
                                                                        if monster[0]['horn-count'] == hornCount:
                                                                            tempCheckList.append(monster[1])
                                                                    if True in tempCheckList and False not in tempCheckList: #positive only
                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString] = {'status':1}
                                                                    elif False in tempCheckList and True not in tempCheckList: #negative only
                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString] = {'status':0}
                                                                    elif True in tempCheckList and False in tempCheckList: #undetermined
                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString] = {'status':2}

                                                                        for laysEggs in generalVersion['lays-eggs']:
                                                                            tempCheckList.clear()
                                                                            laysEggsString = str(laysEggs)
                                                                            for monster in samples: #monster[0] is data and monster[1] is T/F
                                                                                if monster[0]['lays-eggs'] == laysEggs:
                                                                                    tempCheckList.append(monster[1])
                                                                            if True in tempCheckList and False not in tempCheckList: #positive only
                                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString] = {'status':1}
                                                                            elif False in tempCheckList and True not in tempCheckList: #negative only
                                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString] = {'status':0}
                                                                            elif True in tempCheckList and False in tempCheckList: #undetermined
                                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString] = {'status':2}

                                                                                for hasWings in generalVersion['has-wings']:
                                                                                    tempCheckList.clear()
                                                                                    hasWingsString = str(hasWings)
                                                                                    for monster in samples: #monster[0] is data and monster[1] is T/F
                                                                                        if monster[0]['has-wings'] == hasWings:
                                                                                            tempCheckList.append(monster[1])
                                                                                    if True in tempCheckList and False not in tempCheckList: #positive only
                                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString] = {'status':1}
                                                                                    elif False in tempCheckList and True not in tempCheckList: #negative only
                                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString] = {'status':0}
                                                                                    elif True in tempCheckList and False in tempCheckList: #undetermined
                                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString] = {'status':2}

                                                                                        for hasGills in generalVersion['has-gills']:
                                                                                            tempCheckList.clear()
                                                                                            hasGillsString = str(hasGills)
                                                                                            for monster in samples: #monster[0] is data and monster[1] is T/F
                                                                                                if monster[0]['has-gills'] == hasGills:
                                                                                                    tempCheckList.append(monster[1])
                                                                                            if True in tempCheckList and False not in tempCheckList: #positive only
                                                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString][hasGillsString] = {'status':1}
                                                                                            elif False in tempCheckList and True not in tempCheckList: #negative only
                                                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString][hasGillsString] = {'status':0}
                                                                                            elif True in tempCheckList and False in tempCheckList: #undetermined
                                                                                                tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString][hasGillsString] = {'status':2}
                                                                                                
                                                                                                for hasTail in generalVersion['has-tail']:
                                                                                                    tempCheckList.clear()
                                                                                                    hasTailString = str(hasTail)
                                                                                                    for monster in samples: #monster[0] is data and monster[1] is T/F
                                                                                                        if monster[0]['has-gills'] == hasTail:
                                                                                                            tempCheckList.append(monster[1])
                                                                                                    if True in tempCheckList and False not in tempCheckList: #positive only
                                                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString][hasGillsString][hasTailString] = {'status':1}
                                                                                                    elif False in tempCheckList and True not in tempCheckList: #negative only
                                                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString][hasGillsString][hasTailString] = {'status':0}
                                                                                                    elif True in tempCheckList and False in tempCheckList: #undetermined
                                                                                                        tree[color][size][footType][covering][legCountString][armCountString][eyeCountString][hornCountString][laysEggsString][hasWingsString][hasGillsString][hasTailString] = {'status':2}


        for color in tree:
            if color == 'status':
                continue
            if tree[color]['status'] == 1:
                if new_monster['color'] == color:
                    return True
            elif tree[color]['status']== 0:
                if new_monster['color'] == color:
                    return False
            else: # status = 2, undetermined

                for size in tree[color]:
                    if size == 'status':
                        continue
                    if tree[color][size]['status'] == 1:
                        if new_monster['size'] == size:
                            return True
                    elif tree[color][size]['status']== 0:
                        if new_monster['size'] == size:
                            return False
                    else: # status = 2, undetermined

                        for footType in tree[color][size]:
                            if footType == 'status':
                                continue
                            if tree[color][size][footType]['status'] == 1:
                                if new_monster['foot-type'] == footType:
                                    return True
                            elif tree[color][size][footType]['status']== 0:
                                if new_monster['foot-type'] == footType:
                                    return False
                            else: # status = 2, undetermined

                                for covering in tree[color][size][footType]:
                                    if covering == 'status':
                                        continue
                                    if tree[color][size][footType][covering]['status'] == 1:
                                        if new_monster['covering'] == covering:
                                            return True
                                    elif tree[color][size][footType][covering]['status']== 0:
                                        if new_monster['covering'] == covering:
                                            return False
                                    else: # status = 2, undetermined

                                        for legCount in tree[color][size][footType][covering]:
                                            if legCount == 'status':
                                                continue
                                            if tree[color][size][footType][covering][legCount]['status'] == 1:
                                                if new_monster['leg-count'] == int(legCount):
                                                    return True
                                            elif tree[color][size][footType][covering][legCount]['status']== 0:
                                                if new_monster['leg-count'] == int(legCount):
                                                    return False
                                            else: # status = 2, undetermined

                                                for armCount in tree[color][size][footType][covering][legCount]:
                                                    if armCount == 'status':
                                                        continue
                                                    if tree[color][size][footType][covering][legCount][armCount]['status'] == 1:
                                                        if new_monster['arm-count'] == int(armCount):
                                                            return True
                                                    elif tree[color][size][footType][covering][legCount][armCount]['status']== 0:
                                                        if new_monster['arm-count'] == int(armCount):
                                                            return False
                                                    else: # status = 2, undetermined

                                                        for eyeCount in tree[color][size][footType][covering][legCount][armCount]:
                                                            if eyeCount == 'status':
                                                                continue
                                                            if tree[color][size][footType][covering][legCount][armCount][eyeCount]['status'] == 1:
                                                                if new_monster['eye-count'] == int(eyeCount):
                                                                    return True
                                                            elif tree[color][size][footType][covering][legCount][armCount][eyeCount]['status']== 0:
                                                                if new_monster['eye-count'] == int(eyeCount):
                                                                    return False

                                                            else: # status = 2, undetermined

                                                                for hornCount in tree[color][size][footType][covering][legCount][armCount][eyeCount]:
                                                                    if hornCount == 'status':
                                                                        continue
                                                                    if tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount]['status'] == 1:
                                                                        if new_monster['horn-count'] == int(hornCount):
                                                                            return True
                                                                    elif tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount]['status']== 0:
                                                                        if new_monster['horn-count'] == int(hornCount):
                                                                            return False

                                                                    else: # status = 2, undetermined

                                                                        for laysEggs in tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount]:
                                                                            if laysEggs == 'status':
                                                                                continue
                                                                            if tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs]['status'] == 1:
                                                                                if new_monster['lays-eggs'] == (laysEggs=='True'):
                                                                                    return True
                                                                            elif tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs]['status']== 0:
                                                                                if new_monster['lays-eggs'] == (laysEggs=='True'):
                                                                                    return False

                                                                            else: # status = 2, undetermined

                                                                                for hasWings in tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs]:
                                                                                    if hasWings == 'status':
                                                                                        continue
                                                                                    if tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs][hasWings]['status'] == 1:
                                                                                        if new_monster['has-wings'] == (hasWings=='True'):
                                                                                            return True
                                                                                    elif tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs][hasWings]['status']== 0:
                                                                                        if new_monster['has-wings'] == (hasWings=='True'):
                                                                                            return False

                                                                                    else: # status = 2, undetermined

                                                                                        for hasGills in tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs][hasWings]:
                                                                                            if hasGills == 'status':
                                                                                                continue
                                                                                            if tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs][hasWings][hasGills]['status'] == 1:
                                                                                                if new_monster['has-gills'] == (hasGills=='True'):
                                                                                                    return True
                                                                                            elif tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs][hasWings][hasGills]['status']== 0:
                                                                                                if new_monster['has-gills'] == (hasGills=='True'):
                                                                                                    return False

                                                                                            else: # status = 2, undetermined

                                                                                                for hasTail in tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs][hasWings][hasGills]:
                                                                                                    if hasTail == 'status':
                                                                                                        continue
                                                                                                    if tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs][hasWings][hasGills][hasTail]['status'] == 1:
                                                                                                        if new_monster['has-tail'] == (hasTail=='True'):
                                                                                                            return True
                                                                                                    elif tree[color][size][footType][covering][legCount][armCount][eyeCount][hornCount][laysEggs][hasWings][hasGills][hasTail]['status']== 0:
                                                                                                        if new_monster['has-tail'] == (hasTail=='True'):
                                                                                                            return False

                                                    
                        



        




    # size: tiny, small, medium, large, huge
    # color: black, white, brown, gray, red, yellow, blue, green, orange, purple
    # covering: fur, feathers, scales, skin
    # foot-type: paw, hoof, talon, foot, none
    # leg-count: 0, 1, 2, 3, 4, 5, 6, 7, 8
    # arm-count: 0, 1, 2, 3, 4, 5, 6, 7, 8
    # eye-count: 0, 1, 2, 3, 4, 5, 6, 7, 8
    # horn-count: 0, 1, 2
    # lays-eggs: true, false
    # has-wings: true, false
    # has-gills: true, false
    # has-tail: true, false

        return False