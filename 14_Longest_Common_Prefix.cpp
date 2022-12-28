class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        //select the first string to base the prefix off of
        string prefix = strs[0];
        
        //loop over all the strings
        for(int i = 1; i < strs.size(); i++){
            //loop through all the characters of the prefix
            //until you find the prefix
            while(strs[i].find(prefix) != 0){
                //continually remove chars from the prefix
                prefix = prefix.substr(0, prefix.size() -1);
                if (prefix.empty()){
                    return "";
                }
            }
        }
        return prefix;
    }
};