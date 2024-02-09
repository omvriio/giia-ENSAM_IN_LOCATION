def clean(tuples_array):
    result= []
    length= (len(tuples_array))
    for i in range(length):
        if tuples_array[i][1]>= 5: #number to discuss (if its greater than number then the object is considered existing in the area) f(error) 
            result.append(tuples_array[i][0])
    return result


def check(clean_array, landmark):
    result = False
    for i in range(len(clean_array)):
        if landmark == clean_array[i]:
            result = True
    return result
        

def localisate(tuples_array):
    clean_array= clean(tuples_array)
    print("Cleaned array: ", clean_array)
    X = clean_array
    localisation=0
    if check(X,"Frontdoor") : localisation = 1
    if check(X,"Backdoor") and check(X,"rogar"): localisation = 2
    if check(X,"Backdoor") and check(X,"Reception"): localisation = 2
    if check(X,"Reception") and check(X,"vase"): localisation = 3
    if check(X,"Pointeuse"): localisation = 3
    if check(X,"tdjouj"): localisation= 4
    if check(X,"Landmark zr9a"): localisation =  5
    if check(X,"Landmark1") : localisation =  6
    if check(X,"Landmark2") : localisation = 7
    if check(X,"first cabine"): localisation = 8
    if check(X,"machine"): localisation = 9
    if check(X,"AEE"): localisation = 10
    if check(X,"AEE"): localisation = 11
    if check(X,"mathinfo"): localisation= 12
    if check(X,"Blackbox"): localisation= 13
    if check(X,"Pointeuse black"): localisation= 13
    if check(X,"graffiti"): localisation= 14
    if check(X,"panneauxsol2"): localisation= 15
    if check(X,"machinebib"): localisation= 16
    if check(X,"bib"): localisation= 17
    if check(X,"pointeuseidara"): localisation= 18
    if check(X,"forum"): localisation = 19
    if check(X, "idara"): localisation= 20
    if check(X,"landmarkidara"): localisation= 21
    if check(X,"vaseforum"): localisation= 22
    if check(X, "ensam map"): localisation= 23
    if check(X, "tlfaza_idara"): localisation= 23
    if check (X, "landmark_O"): localisation= 24
    if check(X, "7it"): localisation= 25
    if check(X,"rogar") : localisation = 26
    return localisation


def remove_occurrences(input_array): #a function that returns the classes detected with their occurences 
    occurrence_dict = {}
    output_array = []
    for item in input_array:
        if item not in occurrence_dict:
            occurrence_dict[item] = 1
        else:
            occurrence_dict[item] += 1
    for key, value in occurrence_dict.items():
        output_array.append((key, value))
    return output_array




