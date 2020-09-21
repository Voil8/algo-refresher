# include <iostream>
using namespace std;

void put_items_in_arr(int* arr, int numi){
  int curr;
  for(int i=0; i<numi; i++){
    cin >> curr;
    arr[i] = curr;
  }
}
void print_arr(int* arr, int numi){
	for (int i=0; i<numi; i++){
		cout << arr[i] <<' ';
	}
	
}

int main(){
  int numitems;
  cin >> numitems;
  int *arr = new int[numitems];
  put_items_in_arr(arr, numitems);
  print_arr(arr, numitems);
  delete[] arr;
  cout<<endl;
  print_arr(arr, numitems);
}
