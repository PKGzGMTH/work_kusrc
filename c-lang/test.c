#include <stdio.h>
#include <stdlib.h>
 
int main(void)
{
    int arr1[40], arr2[40];

    for(int i = 0; i < 40; i++){
        int randNum = (rand() % 50) + 50;
        arr1[i] = randNum ;
    }

    for(int i = 0; i < 40; i++){
        int randNum = (rand() % 50) + 50;
        arr2[i] = randNum ;
    }

    for (int index = 0; index < 40; index++)
        printf("%d : %d ",index+1,arr1[index]);

    printf("\n");

    for (int index = 0; index < 40; index++)
        printf("%d : %d ",index+1,arr2[index]);

    return 0;
}