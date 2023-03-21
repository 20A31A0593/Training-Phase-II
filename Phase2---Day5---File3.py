# Breadth First Search Algorithm(BFS)

def BFS(graph,start):
    q=[start]
    visited=[start]
    while(len(q)!=0):
        ele=q.pop(0)
        for i in graph[ele]:
            if i not in visited:    #checking for non-visited nodes
                q.append(i)
                visited.append(i)
    print(*visited,sep="->")
graph_elements={
     "a":["b","c"],
     "b":["a","d"],
     "c":["a","d"],
     "d":["e","c","b"],
     "e":["d"]
    }
obj=BFS(graph_elements,"e")
