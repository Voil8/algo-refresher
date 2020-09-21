#include <iostream>
#include "stack.h"

int main(){
	alg::Stack<int> s(4);
	s.push(4);
	s.push(7);
	s.push(112);
	std::cout<<s.push(12)<<std::endl;
	std::cout<<s.push(21)<<std::endl;
	
	
	for (uint32_t i=0; i<s.count(); i++){
		std::cout<<"element at "<<i<<" is "<<s[i]<<std::endl;	
	}
	
	while(!s.is_empty()){
		std::cout<<"popping "<<s.top()<<std::endl;
		s.pop();
	}
	
	int t = 1;	
	while(s.push(t)){
		std::cin>>t;		
	}
	
	while(!s.is_empty()){
		std::cout<<"popping "<<s.top()<<std::endl;
		s.pop();
	}
	
	
}
