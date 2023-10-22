#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n=static_cast<int>(nums.size());
				int prev=-101;
				int move=0;
				for (int i=0; i+move<n;i++){
						cout<<"Before: "<<i<<": "<<nums.at(i)<<endl;
					if (prev==nums.at(i+move)){
						while (i+move<n && prev==nums.at(i+move)){
							move++;
						}
						if (i+move<n)
						nums.at(i)=nums.at(i+move);
						
							
					}
					if (i+move<n){
						nums.at(i)=nums.at(i+move);
						prev=nums.at(i+move);
					}
						cout<<"After: "<<i<<": "<<nums.at(i)<<endl;
				}
				nums.resize(n-move);
				return (n-move);
		}
};
int main(){
		vector <int> v={1,1,2,3};
		int val=2;
		Solution s;
		int n=s.removeDuplicates(v);
		return 0;
}
