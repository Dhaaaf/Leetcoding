// Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

// Players take turns placing characters into empty squares ' '.
// The first player A always places 'X' characters, while the second player B always places 'O' characters.
// 'X' and 'O' characters are always placed into empty squares, never on filled ones.
// The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
// The game also ends if all squares are non-empty.
// No more moves can be played if the game is over.
// Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

// You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.


var tictactoe = function(moves) {
    const grid = Array.from({ length: 3 }, () => Array(3).fill(' '));
  const n = moves.length;

  // Fill the grid with the moves
  for (let i = 0; i < n; i++) {
    const [row, col] = moves[i];
    grid[row][col] = i % 2 === 0 ? 'X' : 'O';
  }

  // Check for a winner
  const checkWinner = (player) => {
    // Check rows, columns, and diagonals
    for (let i = 0; i < 3; i++) {
      if (
        (grid[i][0] === player && grid[i][1] === player && grid[i][2] === player) ||
        (grid[0][i] === player && grid[1][i] === player && grid[2][i] === player)
      ) {
        return true;
      }
    }

    return (
      (grid[0][0] === player && grid[1][1] === player && grid[2][2] === player) ||
      (grid[0][2] === player && grid[1][1] === player && grid[2][0] === player)
    );
  };

  if (checkWinner('X')) {
    return 'A';
  }

  if (checkWinner('O')) {
    return 'B';
  }

  // If all squares are filled, it's a draw; otherwise, the game is pending
  return n === 9 ? 'Draw' : 'Pending';
};
