// To complie this file type: gcc main.c -o <filename>

#include <stdio.h>

void main () {
   char str1[90], str2[30];

   printf("Enter name: ");
   scanf("%s", str1);

   printf("Enter your website name: ");
   scanf("%s", str2);

   printf("Entered Name: %s", str1);
   printf("\nEntered Website:%s", str2);
   
}