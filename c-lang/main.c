// use command: gcc .\work_kusrc\c-lang\main.c -o .\work_kusrc\c-lang\main ; .\work_kusrc\c-lang\main.exe

#include <stdio.h>

int main () {
   char str1[90], str2[30];

   printf("Enter name: ");
   scanf("%s", str1);

   printf("Enter your website name: ");
   scanf("%s", str2);

   printf("Entered Name: %s", str1);
   printf("\nEntered Website:%s", str2);
   
   return(0);
}