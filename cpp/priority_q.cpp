#include <iostream>
#define MAX_N 10000

using namespace std;

int PQ[MAX_N];
int heap_size = 0;

inline void swap(int &a, int &b){
  int temp = a;
  a = b;
  b = temp;
}

inline bool is_empty() {
  return heap_size == 0;
}

inline int top () {
  if(is_empty()) return -1;
  return PQ[1];
}

inline void push(int x){
  PQ[++heap_size]=x;
  int pos = heap_size;
  while (pos>1 && PQ[pos]>PQ[pos/2]) {
    swap(PQ[pos], PQ[pos/2]);
    pos /= 2;
  }
}

inline void pop() {
  if (is_empty()) return;
  int pos = 1;
  swap(PQ[pos], PQ[heap_size--]);
  while (pos<=heap_size) {
    int ret = pos;
    int left = pos*2;
    int right = pos*2 + 1;
    if (left <= heap_size && PQ[ret] < PQ[left]) ret = left;
    if (right <= heap_size && PQ[ret] < PQ[right]) ret = right;
    if (ret!=pos){
      swap(PQ[ret], PQ[pos]);
      pos = ret;
    }
    else break;
  }
}

int main() {
  push(5);
  push(7);
  push(11);
  push(2);
  push(34);
  push(10);
  int i=3;
  while (!is_empty() && i--) {
    cout<<"max item is: "<<top()<<endl;
    pop();
  }
  push(390);
  push(3902);
  i = 3;
  while (!is_empty() && i--) {
    cout<<"max item is: "<<top()<<endl;
    pop();
  }
}
