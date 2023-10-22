#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
			int move=0;
			int n= static_cast<int>(nums.size());
			for (int i=0;i<n;i++){
				cout<<"Before: "<<i<<": "<<nums.at(i)<<endl;
				while (i+move<n && nums.at(i+move)==val){
					move++;
				}
				if (i+move<n)
				nums.at(i)=nums.at(i+move);
				cout<<"After: "<<i<<": "<<nums.at(i)<<endl;
			}
			nums.resize(n-move);
				return (n-move);
    }
};

int main(){
		vector <int> v={0,1,2,2,3,0,4,2};
		int val=2;
		Solution s;
		int n=s.removeElement(v,val);
		return 0;
}
