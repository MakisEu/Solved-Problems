#include <algorithm>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m;
        int n=nums.size(),temp;
        vector<int> indices;
        for (int i=0;i<n;i++){
            if (m.find(target-nums[i]) != m.end()){
                indices.push_back(m[target-nums[i]]);
                indices.push_back(i);
                return indices; 
            }            
            m.insert({nums[i],i});
        }
        return indices;
    }
};
