// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

var moveZeroes = function(nums) {
    let i = 0

    for (let j = 0; j < nums.length; j++) {
        if(nums[j] !== 0) {
            let inter = nums[i]
            nums[i] = nums[j]
            nums[j] = inter
            i++
        }
    }
    
};
