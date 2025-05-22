function lengthOfLongestSubstring(s: string): number {
  const char_set = new Set<string>();
  let longest: number = 0;
  let l: number = 0;

  for (let r: number = 0; r < s.length; r++) {
    while (char_set.has(s[r])) {
       char_set.delete(s[l]);
       l++;
    }

    char_set.add(s[r]);
    longest = Math.max(longest, r - l + 1);
  }

  return longest;
}



const s = "pwwkew";

console.log(lengthOfLongestSubstring(s));
