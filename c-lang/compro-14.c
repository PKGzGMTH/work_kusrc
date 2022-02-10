#include    <stdio.h>
#include    <stdlib.h>


int main(void)
{
    char    name[30];
    float   price;
    int     count;

    FILE *data_t;
    data_t = fopen("data.txt", "r");

    for (int i = 0; i < 3; i++)
    {
        fscanf(data_t, "%d-%f-%s", &count, &price, name);
        printf("Name = %s\tNumber = %d\t Price = %.2f\tTotal = %.2f\n", name, count, price, count * price);
    }

    fclose(data_t);

    return (0);
}