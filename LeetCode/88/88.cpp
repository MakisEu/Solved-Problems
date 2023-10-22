#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
			int l=0,r=0;
			vector<int> v;
			while (l<m && r<n){
					if (nums1[l]<=nums2[r]){
						v.push_back(nums1[l]);
						l++;
					}
					else{
							v.push_back(nums2[r]);
							r++;
					}
			}
			while (l<m){
					v.push_back(nums1[l]);
					l++;
			}
			while (r<n){
					v.push_back(nums2[r]);
					r++;
			}
			nums1=v;
    }
};

int main(){
		 
		vector<int> a={1,2,3},b={1,2};
		int m=3,n=2;
		Solution s;
		s.merge(a,m,b,n);
		for (int i=0;i<(m+n);i++){
				cout<<a.at(i)<<endl;
		}
		return 0;
}
