#include <iostream>
#include <cmath>
bool isNatural(float c){
		if (std::trunc(c) == c){
				return true;
		}
		return false;
}

int main(){
		int sum=0,j=1,i=1,a=0,b=0,c=0;
		bool found=false;
		while(i<500 && !found){
				sum=0;
				a=i;
				b=0;
				for (j=i+1;a+b<1000;j++){
						b=j;
						if (isNatural(sqrt(pow(a,2)+pow(b,2)))){
								c=sqrt(pow(a,2)+pow(b,2));
								if (a+b+c==1000){
										std::cout<<"a= "<<a<<", b= "<<b<<", c= "<<c;
										found=true;
										break;
								}
						}
  			     }
				i++;
		}
		std::cout<<a*b*c;
		return 0;
}
