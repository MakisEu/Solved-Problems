#include <iostream>
#include <cmath>
int main(){
		int i=1,n=100,ss=0,s=0;
		for (i=1;i<=n;i++){
				ss=ss+pow(i,2);
				s=s+i;
		}
		s=pow(s,2);
		std::cout<<s-ss;
		return 0;
}
