
// Given a string s, find the length of the longest  substring
//  without repeating characters.

var lengthOfLongestSubstring = function(s) {
    let n = s.length;
    let charSet = new Set();
    let maxLength = i = j = 0;

    while (i < n && j < n) {
        if (!charSet.has(s[j])) {
            charSet.add(s[j]);
            j++;
            maxLength = Math.max(maxLength, j-i);
            } else {
                charSet.delete(s[i]);
                i++;
                }
            }
  return maxLength;
};
