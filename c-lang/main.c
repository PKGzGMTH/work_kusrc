// use command: gcc .\work_kusrc\c-lang\main.c -o .\work_kusrc\c-lang\main ; .\work_kusrc\c-lang\main.exe

#include <stdio.h>
char stdName[30] = "Pongsakorn Tippayasomdech", faculty[20] = "Computer Science", stdCode[10] = "6430200850" ;
int stdAge = 19;
float gpa = 3.21;

void main (void) {
   printf("My name is %s and student id is %s\n", stdName, stdCode);
   printf("I am %d year old and study %s\n", stdAge, faculty);
   printf("My GPA is %.2f", gpa);
}