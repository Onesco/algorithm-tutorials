''''
Write a function, shortestPath, that takes in an array of edges for an undirected graph and two nodes (nodeA, nodeB).
The function should return the length of the shortest path between A and B. Consider the length as the number of edges
in the path, not the number of nodes. If there is no path between A and B, then return -1.

test_00:
const edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
];

shortestPath(edges, 'w', 'z'); // -> 2

***solution in Javascript***
const shortestPath = (edges, nodeA, nodeB) => {
  const graph = edgesToGraph(edges)
  const isVisited = new Set()

  let [status, len] = exploreGraph(graph, nodeA, nodeB, isVisited)
  return len
};

const  exploreGraph = (graph, nodeA, nodeB, isVisited)=>{
  let n = 1
  let queue = [[nodeA, n]]
  isVisited.add(nodeA)
  while(queue.length >0){
      let [current, e] = queue.shift()
      // console.log(current,e)
      for(let neighbor of graph[current]){
        if(!isVisited.has(neighbor)){
          isVisited.add(neighbor)
        	if(neighbor === nodeB) return  [true, e]
            queue.push([neighbor,e+1])
        }
      }
  }
  return [false, -1]

}



const edgesToGraph = (edges)=>{
  let graph = {}
  for (let [a,b] of edges){
    if(!graph[a]) graph[a] = []
    if(!graph[b]) graph[b] = []
    graph[b].push(a)
    graph[a].push(b)
  }
  return graph
}

const edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
];
shortestPath(edges, 'w', 'z');
module.exports = {
  shortestPath,
};

'''