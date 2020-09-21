#include <iostream>
using namespace std;
#define MAX_N 1000


struct node{
  int parent, rank;
};

node djs[MAX_N];

inline void make_set(int x){
  djs[x].parent = x;
  djs[x].rank = 0;
}

inline int find(int x){
  if (djs[x].parent == x) return x;
  djs[x].parent = find(djs[x].parent);
  return djs[x].parent;
}

inline void unio(int x, int y){
  int xp = find(x);
  int yp = find(y);
  if (xp==yp) return;

  int xr = djs[xp].rank;
  int yr = djs[yp].rank;
  if (xr > yr) djs[yp].parent = xp;
  else {
    djs[xp].parent = yp;
    if (xr == yr) djs[yp].rank += 1;
  }
}

inline bool are_same(int a, int b){
  return find(a)==find(b);
}

int main() {
  make_set(1);
  make_set(2);
  make_set(3);
  make_set(4);
  make_set(7);
  make_set(42);
  make_set(53);
  make_set(32);

  unio(1, 2);
  unio(2, 1);
  unio(2, 3);


  cout<<find(4)<<endl;

  unio(32, 42);
  unio(42, 7);
  unio(4, 32);
  cout<<are_same(32, 3)<<endl;
  unio(7, 1);
  cout<<are_same(32, 3)<<endl;

  int nums[] = {1, 2, 3, 4, 7, 32, 42, 53};
  int len = 8;
  while(len--){
  	cout<<nums[len]<<" parent "<<find(nums[len])<<" | ";
  }

}
