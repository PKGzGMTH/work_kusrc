#include <stdio.h>

int main(void)
{
    int data[10];
    int *pt_data[10];

    for (int i = 0; i < 10; i++)
    {
        printf("Insert Number %d: ", i+1);
        scanf("%d", &data[i]);
    }
    printf("\n----- Result -----\n");
    for (int i = 9; i >+ 0; i--)
    {
        pt_data[i] = &data[i];
        if ((i + 1) % 2 == 0)
            printf("Position %d => address: %p and value is: %d\n", i + 1, pt_data[i], *pt_data[i]);
    }
    return (0);
}