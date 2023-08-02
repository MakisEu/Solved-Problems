class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int size1=nums1.size(),size2=nums2.size(),size=size1+size2;
        //vector<int> merged; 
        int k=0,l=0,sum=0,last=0;
        for (int i=0;i<size/2+1;i++){
            if (k<size1 && l<size2){
                if (nums1.at(k)<nums2.at(l)){
                    sum=last+nums1.at(k);
                    last=nums1.at(k);
                    k++;
                }
                else {
                    sum=last+nums2.at(l);
                    last=nums2.at(l);
                    l++;
                }
            }
            else if (k==size1){
                    sum=last+nums2.at(l);
                    last=nums2.at(l);
                    l++;
            }
            else {
                    sum=last+nums1.at(k);
                    last=nums1.at(k);
                    k++;            }
        }
        if (size%2==1){
            return last;
        }
        else {
            return sum/2.0;
        }
        
    }
};
