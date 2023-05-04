// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32 - bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.



var productExceptSelf = function (nums) {
    // Your code here
    let left = 1;
    let right = 1;
    let product = [];

    for (let i = 0; i < nums.length; i++) {
        product[i] = left;
        left *= nums[i];
    }

    for (let i = nums.length - 1; i > -1; i--) {
        product[i] = right * product[i];  // left * right
        right *= nums[i];
    }
    return product;
};