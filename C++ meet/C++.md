```c++
#include <bits/stdc++.h>
using namespace std;
int main() {
	cout << "hello world" << endl;
}
```

```c++
int a[5] = {1,2,3,4,5};
for (int i : a) cout << i << "\n"; // for i in a: print(i)
```

## STL Datatypes

### String
```c++
string s;
cin >> s;
s+=" is a string";
cout << "String is " << s << " and the size is " << s.size() << '\n';
if (s=="this is a string") cout << "checked\n";
else cout<<"no\n";
```
### Vector
- Does linear search, so small vectors are faster than sets/multisets which do logarithmic search.
- Supposed to be only insertable at the end, so `insert()` takes $O(n)$ time and so do `erase()` and `find()`.

```c++
vector<int> v1;
vector<int> v2(5,0); // length, initial value
vector<int> v3 = {1,2,3,4}
v1.push_back(6) //appends 6
v1.pop_back() //pops
v1.size()
vector<int> v_2d(3, vector<int>(3,0)) // 2d vector
v.begin() // start of the vector
v.end() // end of the vector
```
#### Sorting
```c++
v.sort(v.begin(), v.end()) // sort from beginning to end
v.sort(v.end(), v.begin()) // sort from end to begin ()reverse sort)
```

```c++
v.sort(start, end, compare);
bool compare(int a, int b) {
return a<b;
}
```
#### Other useful functions
```c++
reverse() // reverses a vector/array
accumulate() // returns sum of all elements
insert()
erase()
find(element) // returns iterator of the element, if not present then v.end()
max_element()
min_element()
```
### Set/Multiset
- Sets hold unique elements, multisets can hold duplicates
- Always sorted.
- `insert`/`delete`/`find` can be done in $O(logn)$ time since it is sorted.
- Does logarithmic search.
- Can't access element through index, need to iterate through the set.
```c++
set<int> s;
s.insert(2);
s.insert(3);
s.insert(4);
cout << s.size() << "\n";
cout << s.find(3) << "\n";
```
### Map
```c++
map<string, int> mp;
mp["hello"] = 3;
```