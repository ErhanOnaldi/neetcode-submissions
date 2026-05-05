public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if (s1.Length > s2.Length) return false;

        int[] freq = new int[26];

        foreach (char c in s1) {
            freq[c - 'a']++;
        }

        int l = 0;

        for (int r = 0; r < s2.Length; r++) {
            freq[s2[r] - 'a']--;

            if (r - l + 1 > s1.Length) {
                freq[s2[l] - 'a']++;
                l++;
            }

            if (r - l + 1 == s1.Length && AllZero(freq)) {
                return true;
            }
        }

        return false;
    }

    private bool AllZero(int[] freq) {
        for (int i = 0; i < 26; i++) {
            if (freq[i] != 0) return false;
        }

        return true;
    }
}