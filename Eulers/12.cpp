#include <iostream>

int main(){
		int j=0,triangle=1,cnt=1,divisors=0;
		long int sum=0;
		bool End=false;
		while (!End){
				divisors=0;
				j=1;
				while (j<triangle+1 && divisors<=500){
						if (triangle%j==0){
								divisors++;
						}
						j++;
				}
				if (divisors>500){
				End=true;
				}
				else{
					cnt++;
					triangle=triangle+cnt;
				}

		}
		std::cout<<triangle;

		return 0;
}
