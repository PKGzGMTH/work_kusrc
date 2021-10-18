#include<stdio.h>
#include<stdlib.h>

void mean(int array[])
{
    float sum = 0,avg = 0;
    for (int i = 0; i < 40; i++) 
    {
        sum += array[i];
    }
    printf("Class's average is %.2f", sum / 40);
    printf("\n");
}

void sorting(int arr1[])
{
    int buff;
    for (int r = 1; r < 40; r++)
    {
        for (int i = 0; i < 39; i++) 
        {
            if (arr1[i] > arr1[i + 1]) 
            {
                buff = arr1[i];
                arr1[i] = arr1[i + 1];
                arr1[i + 1] = buff;
            }
        }
    }
}

void mode(int arr1[])
{
    int max = 0;
    int mode = 0;
    int f[20] = { 0 };

    for (int i = 0; i < 40; i++) 
    {
        ++f[arr1[i]];
    }
    for (int i = 0; i < 20; i++) 
    {
        if (f[i] > max)
        {
            max = f[i];
            mode = i;
        }
    }
    printf("\nClass's mode is %d", mode);
}



int main(void)
{
    int arr1[40], arr2[40];

    for(int i = 0; i < 40; i++){
        arr1[i] = (rand() % 50) + 50;
    }

    for(int i = 0; i < 40; i++){
        arr2[i] = (rand() % 50) + 50;
    }


    //for(int index = 0; index < 40; index++) printf("Class1 No.%d : %d\n", index + 1, arr1[index]);
    //for(int index = 0; index < 40; index++) printf("Class1 No.%d : %d\n", index + 1, arr2[index]);

    printf("\n");

    mean(arr1);
    mean(arr2);

    sorting(arr1);
    sorting(arr2);

    printf("\nData after sorting\n");
    for (int i = 0; i < 40; i++) 
    {
        printf("%d ", arr1[i]);
    }
    printf("\n");
    printf("Class1's median is %d or %d",arr1[19],arr1[20]);
    printf("\n");
    mode(arr1);
    return 0;
}