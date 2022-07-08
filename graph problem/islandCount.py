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