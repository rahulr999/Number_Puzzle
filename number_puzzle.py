import copy
array = [[1,4,2],[6,3,5],[0,7,8]]
#array = [array[2],array[0],array[1]]
finish = 0
list_array = []
prev_array = []
for x in range(len(array)):
    for y in range(len(array)):
        if array[x][y] == 0:
            i=x
            j=y
            break
def heuristic_val(array):
    sol = [[0,1,2],[3,4,5],[6,7,8]]
    val = 0
    for i in range(len(array)):
        for j in range(len(array[1])):
            if array[i][j] != sol[i][j] and array[i][j] != 0:
                val += abs(array[i][j] - ((3*i)+j))
    return val
def heuristic_fun(list_array):
    global finish,prev_array
    while finish == 0 or len(list_array) > 0:
        array = list_array[0]
        del list_array[0]
        i = array[0][0]
        j = array[0][1]
        if i < 2:
            arr = copy.deepcopy(array[1])
            temp = arr[i][j]
            arr[i][j] = arr[i+1][j]
            arr[i+1][j] = temp
            if arr not in prev_array:
                prev_array.append(arr)
                list_array.append([[i+1,j],arr,array[2]+["Down"],heuristic_val(arr)+(len(array[2])+1)*3])
        if i > 0:
            arr = copy.deepcopy(array[1])
            temp = arr[i][j]
            arr[i][j] = arr[i-1][j]
            arr[i-1][j] = temp
            if arr not in prev_array:
                prev_array.append(arr)
                list_array.append([[i-1,j],arr,array[2]+["Up"],heuristic_val(arr)+(len(array[2])+1)*3])
        if j < 2:
            arr = copy.deepcopy(array[1])
            temp = arr[i][j]
            arr[i][j] = arr[i][j+1]
            arr[i][j+1] = temp
            if arr not in prev_array:
                prev_array.append(arr)
                list_array.append([[i,j+1],arr,array[2]+["Right"],heuristic_val(arr)+(len(array[2])+1)*3])
        if j > 0:
            arr = copy.deepcopy(array[1])
            temp = arr[i][j]
            arr[i][j] = arr[i][j-1]
            arr[i][j-1] = temp
            if arr not in prev_array:
                prev_array.append(arr)
                list_array.append([[i,j-1],arr,array[2]+["Left"],heuristic_val(arr)+(len(array[2])+1)*3])
        list_array.sort(key = lambda x: x[3])
        print(list_array[0])
        if heuristic_val(list_array[0][1]) == 0:
            finish = 1
            break
    return list_array[0][2]
def print_mat(array):
    for x in array:
        st = ""
        for y in x:
            if y == 0: st+="-"+" "
            else: st+=str(y)+" "
        print(st)
    print("\n")
move = heuristic_fun([[[i,j],array,[],9999]])
print_mat(array)

for mv in move:
    if mv == "Up":
        temp = array[i][j]
        array[i][j] = array[i-1][j]
        array[i-1][j] = temp
        i = i-1
    if mv == "Down":
        temp = array[i][j]
        array[i][j] = array[i+1][j]
        array[i+1][j] = temp
        i = i+1
    if mv == "Left":
        temp = array[i][j]
        array[i][j] = array[i][j-1]
        array[i][j-1] = temp
        j = j-1
    if mv == "Right":
        temp = array[i][j]
        array[i][j] = array[i][j+1]
        array[i][j+1] = temp
        j = j+1
    print_mat(array)
print(move)
