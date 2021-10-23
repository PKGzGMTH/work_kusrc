#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void randomArray(int arr[5][5]){
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            arr[i][j] = (rand() % 75) + 1;
        }
    }
}

void printArray(const int arr[5][5])
{
    for (int i = 0; i <= 4; i++) 
    {
        for (int j = 0; j <= 4; j++) 
        {
            if (i == 2 && j == 2)
            {
                printf("X ");
            }
            else
            {
                printf("%d ", arr[i][j]);
            }
        }
        printf("\n");
    }
}

int main(void)
{
    int a[5][5];
    int b[5][5];

    srand(time(NULL));
    randomArray(a);
    randomArray(b);
    printArray(a);
    printf("\n\n");
    printArray(b);
    getch();
    return 0;
}