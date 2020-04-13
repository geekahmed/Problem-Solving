/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

/*
// Sample code to perform I/O:
 
cin >> name;                            // Reading input from STDIN
cout << "Hi, " << name << ".\n";        // Writing output to STDOUT
 
// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/
 
// Write your code here
 
#include <iostream>
 
 
using namespace std;
void printArray(int arr[], int n);
void insertionSort(int arr[], int n);
int main(){
 
    int n;
    cin >> n ;
    int powerOfCreatures[n];
    for (int i = 0 ; i < n ; i++)
        cin >> powerOfCreatures[i];
    insertionSort(powerOfCreatures, n);
    int zombies[1000] , vampire[1000] , z = 0 , v = 0, sumZ = 0 , sumV = 0 ;
    for (int i = 0 ; i < n ; i++){
        if (powerOfCreatures[i] % 2 == 0){
            zombies[z]  = powerOfCreatures[i];
            z++;
            sumZ += powerOfCreatures[i];
        } else {
            vampire[v] = powerOfCreatures[i];
            v++;
            sumV += powerOfCreatures[i];
        }
    }
    printArray(zombies, z);
    cout << sumZ << " " ;
    printArray(vampire, v);
    cout << sumV;
    return 0;
}
void printArray(int arr[], int n)  {
 
    for (int i = 0; i < n; i++)
        cout << arr[i] << " " ;
 
}
void insertionSort(int arr[], int n){
 
    if (n <= 1)
        return;
    insertionSort( arr, n-1 );
    int last = arr[n-1];
    int j = n-2;
     while (j >= 0 && arr[j] > last){
        arr[j+1] = arr[j];
        j--;
    }
    arr[j+1] = last;
}
