#ifndef ALGO_QUEUE_H__
#define ALGO_QUEUE_H__

#include <stdint.h>
#include <stdbool.h>

namespace alg{
	template <typename T>
	class Queue{
		private:
			uint32_t m_cap, m_size, m_front, m_rear;
			T* m_elems;
		
		public:
			Queue(int cap){
				this->m_cap=cap;
				this->m_size=0;
				this->m_front=0;
				this->m_rear=-1;
				this->m_elems = new T[cap];				
			}
			
			~Queue(){
				delete [] m_elems;
			}
			
		private:
			Queue(const Queue&);
			Queue& operator=(const Queue&);
		
		public:
			inline const T& front() const{
				// throw exception if m_size==0
//				if (m_size==0) return; //this will cause it to break
				return m_elems[m_front];
			}
			inline bool enqueue(const T& value){
				if (m_size<m_cap){
					m_rear++;
					m_size++;
					if (m_rear==m_cap) m_rear=0;
					m_elems[m_rear] = value;
					return true;					
				}
				return false;
			}
			inline bool dequeue() {
				if (m_size==0) return false;
				m_size--;
				m_front++;
				if (m_front==m_cap) m_front=0;
				return true;				
			}
			inline bool is_empty() const { return m_size==0?true:false; }
			inline uint32_t count() const { return m_size;}
			inline uint32_t capacity() const { return m_cap;}
		
	};
}
#endif
