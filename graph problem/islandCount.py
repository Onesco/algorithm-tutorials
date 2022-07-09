'''
Write a function, islandCount, that takes in a grid containing Ws and Ls. W represents water and L represents land.
The function should return the number of islands on the grid. An island is a vertically or horizontally connected
region of land.

test_01:
const grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
];

islandCount(grid); // -> 4

***Javascript solution***
const islandCount = (grid) => {
  let count = 0
  let isVisited = new Set()
  for(let r=0; r < grid.length;  r +=1){
      for(let c=0; c < grid[0].length;  c +=1){
         if(exploreGrid(grid, r, c, isVisited)){
           count +=1
         }
    }
  }
  return count
};

const exploreGrid = (grid, row, col, isVisited)=>{

  const isWithinRowBoundry = 0<=row && row < grid.length
  const isWithinColBoundry = 0<= col && col < grid[0].length
  if(!isWithinColBoundry || !isWithinRowBoundry) return false

  const pos = row +','+ col
  if(isVisited.has(pos)) return false
  isVisited.add(pos)

  if(grid[row][col] ==='W') return false

  let right = exploreGrid(grid,row,col+1, isVisited) // right explore
  let left = exploreGrid(grid,row,col-1, isVisited) // left explore
  let up = exploreGrid(grid,row-1,col, isVisited) // up explore
  let down = exploreGrid(grid,row+1,col, isVisited) // down explore

  return true
}



const grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
];

console.log(islandCount(grid))

module.exports = {
  islandCount,
};

'''

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'W', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
];



def Island_count(grid):
    count = 0
    is_visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if exploreGrid(grid, r, c, is_visited):
                count += 1
    return count



def exploreGrid(grid, r, c, is_visited):
    # print(r, c)
    col_boundries = 0 <= c & c < len(grid[0])
    row_boundries = 0 <= r & r < len(grid)

    if (not col_boundries or not row_boundries):
        return False

    pos = f"{r},{c}"
    if pos in is_visited:
        return False
    is_visited.add(pos)

    if grid[r][c] =='W':
        return False

    exploreGrid(grid, r, c+1 , is_visited)
    exploreGrid(grid, r, c - 1, is_visited)
    exploreGrid(grid, r-1, c, is_visited)
    exploreGrid(grid, r + 1, c, is_visited)

    return True

