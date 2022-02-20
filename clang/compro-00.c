// use command: gcc .\work_kusrc\c-lang\main.c -o .\work_kusrc\c-lang\main ; .\work_kusrc\c-lang\main.exe
#include <stdio.h>
char stdName[30], faculty[20], stdCode[10];
int stdAge;
float gpa;

int main () {
   printf("Enter Name : ");
   gets(stdName);
   printf("Enter Student ID : ");
   gets(stdCode);
   printf("Enter Faculty : ");
   gets(faculty);
   printf("Enter Age : ");
   scanf("%d", &stdAge);
   printf("Enter GPA : ");
   scanf("%f", &gpa);
   printf("My name is %s and student id is %s\n", stdName, stdCode);
   printf("I am %d year old and study %s\n", stdAge, faculty);
   printf("My GPA is %.2f", gpa);

   return 0;
}