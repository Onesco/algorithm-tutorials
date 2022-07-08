'''
Write a function, minimumIsland, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.

test_00:
const grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
];

minimumIsland(grid); // -> 2

***Javascript solution***

const minimumIsland = (grid) => {

let inLandLength = 999999999
  let isVisited = new Set()
  for(let r=0; r < grid.length;  r +=1){
      let x = 0
      for(let c=0; c < grid[0].length;  c +=1){
        let [isLand, size] = exploreGrid(grid, r, c, isVisited, x)
        if(isLand){
           inLandLength = Math.min(inLandLength, size + 1)
          console.log(size + 1)
         }
    }
  }
  return inLandLength
};

const exploreGrid = (grid, row, col, isVisited, size)=>{

  const isWithinRowBoundry = 0<=row && row < grid.length
  const isWithinColBoundry = 0<= col && col < grid[0].length
  if(!isWithinColBoundry || !isWithinRowBoundry) return [false,size]

  const pos = row +','+ col
  if(isVisited.has(pos)) return [false,size]
  isVisited.add(pos)

  if(grid[row][col] ==='W') return [false,size]

  let [isLandR, sizeR] = exploreGrid(grid,row,col+1, isVisited, size) // right explore
  let [isLandL, sizeL] = exploreGrid(grid,row,col-1, isVisited, size) // left explore
  let [isLandU, sizeU] = exploreGrid(grid,row-1,col, isVisited, size) // up explore
  let [isLandD, sizeD] = exploreGrid(grid,row+1,col, isVisited, size) // down explore
  // console.log(sizeR, sizeL, sizeU, sizeD)
  if(isLandR) sizeR += 1
  if(isLandL) sizeL += 1
  if(isLandU) sizeU += 1
  if(isLandD) sizeD += 1

  size = sizeD + sizeU + sizeL + sizeR
  return [true,size]
}



const grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'L', 'L', 'L'],
  ['W', 'W', 'L', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
];

minimumIsland(grid)

module.exports = {
  minimumIsland,
};

'''