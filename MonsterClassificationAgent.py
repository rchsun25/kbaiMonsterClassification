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