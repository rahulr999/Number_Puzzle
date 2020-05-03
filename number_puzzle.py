import copy
array = [[1,4,2],[6,3,5],[0,7,8]] #array for the input here 0 is assumed to be  "-"
finish = 0 # Flag to check is a solution has been reached
list_array = [] #Stroing the list of currently explored states
prev_array = [] #Stroing the list of possible places to prevent recurring tiles to avoid looping
sol = [] # the actual solution
cnt = 0
for x in range(len(array)):   #Initalising the values of index value of the swap tile and the actual solution
    sl = []
    for y in range(len(array[0])):
        sl.append(cnt)
        cnt+=1
        if array[x][y] == 0:
            i=x
            j=y
    sol.append(sl)
def heuristic_val(array):  #Calculates the heuristic for a given state and to check if the solution has been met
    global sol
    val = 0
    for i in range(len(array)):
        for j in range(len(array[1])):
            if array[i][j] != sol[i][j] and array[i][j] != 0:
                val += abs(array[i][j] - ((len(sol)*i)+j))
    return val
def heuristic_fun(list_array): #to explore the new states
    global finish,prev_array
    while finish == 0 or len(list_array) > 0:
        array = list_array[0]
        del list_array[0]
        i = array[0][0]
        j = array[0][1]
        if i < len(sol)-1: #
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
        if j < len(sol[0])-1:
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
            if arr not in prev_array: #To check if this state has been reached before
                prev_array.append(arr)
                list_array.append([[i,j-1],arr,array[2]+["Left"],heuristic_val(arr)+(len(array[2])+1)*3])
        list_array.sort(key = lambda x: x[3]) #Sorting the list based on the heuristic value
        if heuristic_val(list_array[0][1]) == 0: #To check if the solution has been reached
            finish = 1
            break
    return list_array[0][2]
def print_mat(array): #printing the list of steps that leades to the solution
    for x in array:
        st = ""
        for y in x:
            if y == 0: st+="-"+" "
            else: st+=str(y)+" "
        print(st)
    print("\n")
move = heuristic_fun([[[i,j],array,[],9999]]) #calling the heuristic function
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
