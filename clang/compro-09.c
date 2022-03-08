#include <stdio.h>

int main(void)
{
    int data[5];
    int *pt_data;

    pt_data = &data[0];
    for (int i = 0; i < 5; i++)
    {
        printf("Insert Number %d: ", i+1);
        scanf("%d", pt_data);
        if (i < 4)
            pt_data++;
    }
    printf("\n----- Result -----\n");
    for (int i = 5; i > 0; i--)
    {
        printf("Position %d => address: %p and value is: %d\n", i, pt_data, *pt_data);
        if (i > 1)
            pt_data--;
    }
    return (0);
}