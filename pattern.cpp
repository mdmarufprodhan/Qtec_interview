#include<iostream>
using namespace std;

int pattern_search(string text,string pat){
  int t = text.size();
  int p = pat.size();
  int m = (t-p)+1;
  int n = 0; //couter for pattern
  for(int i=0;i<m;i++){
  int cnt = 0;
    for(int j=0;j<p;j++){
      if(text[i+j] == pat[j])
           cnt++;
    }
    if(cnt == p)
       n++;      
  }
return n;
}
int main(){
string str;
string pat;
cout<<"Enter The string:";
cin>>str;
cout<<"\nEnte The pattern:";
cin>>pat;
cout<<pattern_search(str,pat)<<" Times";
return 0;
}