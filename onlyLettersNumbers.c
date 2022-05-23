//only letters words numbers solution by gauravnv
// i/p "hello #every 1 one one123 #123"
// o/p  hello 1 one

#include <stdio.h>
#include <string.h>
#include <ctype.h>

char *getString(char str1[1000]){
    
    char ns[100];
    char * t = strtok(str1," ");
    while(t!=NULL){
        char s[100]=" ";
        int q = 0,wc = 0,dc = 0,spc = 0;
        for(int i =0;i<strlen(t);i++){
            if(isalpha(t[i]) != 0 && dc == 0 && spc == 0){
                wc++;
                s[q++] = t[i];
            }
            else if(wc>0){
                strcpy(s," ");
            }
            else if(isdigit(t[i])!=0 && wc == 0 && spc == 0){
                dc++;
                s[q++] = t[i];
            }
            else{
                spc++;
            }
        }t = strtok(NULL," ");
        if(s[0] != ' ')
        printf("%s ",s);
        
    }
    
}

int main(){
    char s[] = "hello #every 1 one one123 #123";
    getString(s);
    return 0;
}
