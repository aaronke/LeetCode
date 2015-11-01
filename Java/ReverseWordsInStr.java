public class Solution {
    public String reverseWords(String s) {
        if (s.length() < 1)
            return s;
        StringBuilder sb = new StringBuilder();
        int slow = 0, fast = s.length()-1;
        while (slow <= fast && s.charAt(slow) == ' ')
            slow++;
        while (fast >= slow && s.charAt(fast) == ' ')
            fast--;
        while (slow <= fast) {
            int cursor = fast;
            while (cursor >= slow && s.charAt(cursor) != ' ')
                cursor--;
            sb.append(s.substring(cursor+1, fast+1)+" ");
            while (cursor >= slow && s.charAt(cursor) == ' ')
                cursor--;
            fast = cursor;
        }
        String result = sb.toString();
        if (result.length()>1)
            result = result.substring(0, result.length()-1);
        return result;
        
    }
}
