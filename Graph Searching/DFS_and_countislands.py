def convert_to_graph(sample_array):
    cmap = {}
    #converting multidimensional array to graph
    for i in range(len(sample_array)):
            for j in range(len(sample_array[i])):
                    cmap[(i,j)] = set()
                    if (j-1>=0):
                            cmap[(i,j)].add((i,j-1))

                    if (i-1>=0):
                            cmap[(i,j)].add((i-1,j))

                    if (i+1<len(sample_array)):
                            cmap[(i,j)].add((i+1,j))

                    if (j+1<len(sample_array[0])):
                            cmap[(i,j)].add((i,j+1))
    return cmap

#standard implementation of dfs
def dfs(cmap, start, visited=set()):
    print start
    visited.add(start)
    for vertex in (cmap[start]-visited):
        dfs(cmap,vertex, visited)
    return visited


#island solving problem using dfs, find islands of 1s
#steps of solving problem
#1. convert cysystem over to map where coordinates connect if 1<->1
#2. DFS the map, recording the number of times DFS must "restart" with a 1 as a start coordinate
def convert_islands(arr):
    cmap = {}
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] is 0: continue
            cmap[(i,j)] = set()
            #left coord
            in_range = True if j-1>=0 else None
            if(in_range and arr[i][j-1] is 1):
                cmap[(i,j)].add((i,j-1))
        
            #down coord
            in_range = True if i-1>=0 else None
            if(in_range and arr[i-1][j] is 1):
                cmap[(i,j)].add((i-1,j))
            
            #right coord
            in_range = True if j+1<len(arr[0]) else None
            if(in_range and arr[i][j+1] is 1):
                cmap[(i,j)].add((i,j+1))
            
            #up coord
            in_range = True if i+1<len(arr) else None
            if(in_range and arr[i+1][j] is 1):
                cmap[(i,j)].add((i+1,j))
    return cmap
    
def search_islands(cmap, arr):
    visited = set()
    island_count = 0
    for vertex in cmap:
        if (arr[vertex[0]][vertex[1]] is 1) and (not vertex in visited):
            visited = visited | c_dfs(cmap,vertex)
            island_count = island_count+1
    return island_count
    
#standard implementation of dfs
def c_dfs(map, start, visited=set()):
    visited.add(start)
    for vertex in (map[start]-visited):
        c_dfs(map, vertex, visited)
    return visited


sample_array = [[1,0,1,1,0,1,1]]

cmap = convert_islands(sample_array)
print search_islands(cmap, sample_array)

