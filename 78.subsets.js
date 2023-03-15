// Given an integer array nums of unique elements, return all possible 
// subsets
//  (the power set).

// The solution set must not contain duplicate subsets. Return the solution in any order.

// Iterative Solution

var subsets = function(nums) {

    // Iterative solution

    const res = [[]]
    for (let num of nums) {
        res.forEach(subset => {
            res.push([...subset, num])
            // let copy = [...subset]
            // copy.push(num)
            // res.push(copy)
            // console.log(res)
        })
    }
    return res

};

// Recursive Solution

function subsets(nums) {
    if (nums.length === 0) {
      return [[]];
    } else {
      const num = nums.pop();
      const prevSubsets = subsets(nums);
      const newSubsets = [];
      prevSubsets.forEach(subset => {
        newSubsets.push(subset);
        newSubsets.push([...subset, num]);
      });
      return newSubsets;
    }
  }
