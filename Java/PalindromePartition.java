// DP, there cases, add one, add one combine two, add one combine two and three
// easy falls: size of the list, remove from large index to small, add (new xxxx) or not
public ArrayList<ArrayList<String>> partition(String s) {
    ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>> ();
    if (s.length() == 0) {
        result.add(new ArrayList<String>());
        return result;
    }
    ArrayList<ArrayList<String>> otherResult = partition(s.substring(1));
    for (ArrayList<String> temp: otherResult) {
        temp.add(0, s.substring(0,1));
        result.add(temp);
        if (temp.size() > 1 && isPalindrome(temp.get(0) + temp.get(1))) {
            ArrayList<String> here = new ArrayList<String> (temp);
            here.add(0, temp.get(0) + temp.get(1));                
            here.remove(2);
            here.remove(1);
            if (!result.contains(here))
                result.add(here);
        }
        if (temp.size() > 2 && isPalindrome(temp.get(0) + temp.get(1) + temp.get(2))) {
            ArrayList<String> here = new ArrayList<String> (temp);
            here.add(0,temp.get(0) + temp.get(1) + temp.get(2));                
            here.remove(3);
            here.remove(2);
            here.remove(1);
            if (!result.contains(here))
                result.add(here);           
        }
    }
    return result;
}

private boolean isPalindrome(String s) {
    if (s == null || s.length() == 0)
        return false;
    for (int i = 0; i < s.length()/2; i++) {
        if (s.charAt(i) != s.charAt(s.length() - i - 1))
            return false;
    }
    return true;
}


// nine chapter module, add recursive remove
public ArrayList<ArrayList<String>> partition(String s) {
    ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();
    if (s == null) {
        return result;
    }

    ArrayList<String> path = new ArrayList<String>();
    helper(s, path, 0, result);

    return result;
}

private boolean isPalindrome(String s) {
    int beg = 0;
    int end = s.length() - 1;
    while (beg < end) {
        if (s.charAt(beg) != s.charAt(end)) {
            return false;
        }

        beg++;
        end--;
    }

    return true;
}

private void helper(String s, ArrayList<String> path, int pos,
        ArrayList<ArrayList<String>> result) {
    if (pos == s.length()) {
        result.add(new ArrayList<String>(path));
        return;
    }

    for (int i = pos + 1; i <= s.length(); i++) {
        String prefix = s.substring(pos, i);
        if (!isPalindrome(prefix)) {
            continue;
        }

        path.add(prefix);
        helper(s, path, i, result);
        path.remove(path.size() - 1);
    }
}
