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
		int i=2,cnt=0,primes[10001];
		while (cnt<10001){
				if (isPrime(i,primes,cnt)){
						primes[cnt]=i;
						cnt++;
				}
				i++;
		}
		std::cout<<primes[10000];

		return 0;
}
