public class Solution {
    public bool IsPalindrome(string s) {
    StringBuilder sb = new StringBuilder();
        foreach (char ch in s)
        {
            if (char.IsLetterOrDigit(ch))
            {
                sb.Append(char.ToLower(ch));
            }
        }
        string cleaned = sb.ToString();

        int l = 0;
        int r = cleaned.Length - 1; // Hata 1 ve 2 düzeltildi

        while (l < r)
        {
            if (cleaned[l] != cleaned[r])
            {
                return false;
            }
            l++; // Hata 3 düzeltildi (artırıldı)
            r--; // Hata 3 düzeltildi (azaltıldı)
        }

        return true;
    }
}
