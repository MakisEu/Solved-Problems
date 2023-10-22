#include <iostream>

int main(){
		int chain=0,mx=0,longestNum;
		long int temp=0;
		for (int i=1;i<1000000;i++){
				temp=i;
				while(temp!=1){
						chain++;
						if (temp%2==0){
								temp=temp/2;
						}
						else{
								temp=3*temp+1;
						}
				}
				if (chain>mx){
						mx=chain;
						longestNum=i;
				}
		}

		std::cout<<longestNum;

		return 0;
}
