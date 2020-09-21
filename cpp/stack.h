#ifndef ALGO_STACK_H__
#define ALGO_STACK_H__

#include <stdint.h>
#include <stdbool.h>
//#inlcude <exception>
//from https://github.com/xtaci/algorithms/blob/master/include/stack.h


namespace alg{
	template <typename T=uintptr_t>
	class Stack{
		private:
			//exception 1?
			//exception 2?
			
			uint32_t m_capacity;
			uint32_t m_size;
			T* elements;
		
		public:
			Stack(uint32_t capacity) {
				this->m_capacity = capacity;
				this->m_size = 0;
				this->elements = new T[capacity];
			}
			~Stack(){
				delete [] elements;
			}
		// copy constructure
		private:
			Stack(const Stack&);
			//constructor 2?
		
		public:
			
			inline bool is_empty() const { return m_size==0?true:false; }
			
			inline void pop() {
				if (m_size!=0) m_size--;
				return;
			}
			
			inline const T& top() const {return elements[m_size-1];}
			
			inline bool push(const T& element) {
				if (m_capacity>m_size){
					elements[m_size++] = element;
					return true;
				}
				return false;												
			} 
			
			inline uint32_t count() const { return m_size;}
			
			const T& operator [] (uint32_t idx){
				return elements[m_size-idx-1];
			}				
	};
}
#endif
