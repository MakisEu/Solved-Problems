class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLen=0,i=0,prev=0,cr,t;
        string chars,b=s;
        while (i<s.length()-maxLen){
            chars=s[i];
            cr=1;
            i++;
            t=chars.find(s[i]);
            while (t==-1 && i<s.length()){
                chars=chars+s[i];
                i++;
                cr++;
                t=chars.find(s[i]);
            }
            if (chars.find(s[i])<chars.length()){
                i=chars.find(s[i])+prev+1;
                prev=i;
            }
            if (maxLen<cr){
                maxLen=cr;
            }
        }
        return maxLen;
    }
};
