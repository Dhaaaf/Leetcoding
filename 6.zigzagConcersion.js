// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)


// And then read line by line: "PAHNAPLSIIGYIR"

// Write the code that will take a string and make this conversion given a number of rows:

var convert = function(s, numRows) {
    if ( numRows < 2) return s
    let res = []

    let row = 0
    let dir = 1
    for (let i of s) {
        if (!res[row]) {
        res[row] = []
        }
        res[row].push(i)

        if (row === 0 && dir === -1 || row === numRows -1 && dir === 1) {
            dir *= -1
        }

        row += dir
    }

    // return res

    return res.map(r => r.join('')).join('')
};
