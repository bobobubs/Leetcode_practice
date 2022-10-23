class Solution {
public:
    bool isSubsequence(string s, string t) {
        int x = s.length();
        int y = t.length();
        int i=0, j=0;
        while(i<x && j<y){
            if(s[i]!=t[j]){
                j++;
            }       
            else{
                i++;
                j++;
            }
        }
        if(i!=x){
            return false;
        }
        return true;
    }
};
