// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

var containsDuplicate = function(nums) {
    let ourSet = new Set();

        for (let n of nums) {
            if (ourSet.has(n)) {
                return true;
            }
            ourSet.add(n);
        }
        return false;
};
