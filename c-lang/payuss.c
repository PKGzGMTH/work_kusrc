#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int num;
char name[30],*work;

void random_work(){
    int num = rand() % 5;

    switch (num) {    
    case 0:
        work = "Fisherman";
        break;
    case 1:
        work =  "Builder";
        break;
    case 2:
        work =  "Maker";
        break;
    case 3:
        work =  "Farmer";
        break;
    case 4:
        work =  "Miner";
        break;
    
    default:
        break;
    }
}

void main(){
    printf("Please Enter your name : ");
    scanf("%s", name);
    random_work();
    printf("Your name is : %s",name);
    printf("\nYour work is : %s",work);
    getch();
}