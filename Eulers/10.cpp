#include <iostream>
bool isPrime(int i,int primes[],int n){
		int k=0;
		for (k=0;k<n;k++){
				if (i%primes[k]==0){
						return false;
				}
		}
		return true;
}
int main(){
		int i=2,cnt=0,primes[2000000];
		long int sum=0;
		while (i<2000000){
				if (isPrime(i,primes,cnt)){
						primes[cnt]=i;
						cnt++;
						sum=sum+i;
				}
				i++;
		}
		std::cout<<sum;

		return 0;
}
