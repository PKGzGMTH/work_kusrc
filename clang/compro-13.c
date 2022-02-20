#include    <stdio.h>
#include    <stdlib.h>


int main(void)
{
    char name[30];
    float price;
    FILE *product_t, *price_t;

    product_t = fopen("product.txt", "w+");
    price_t = fopen("price.txt", "w+");

    for (int i = 0; i < 3; i++)
    {
        printf("Please input product name :\n");
        scanf("%s", name);
        printf("Please input product price :\n");
        scanf("%f", &price);
        fprintf(product_t, "%s\n", name);
        fprintf(price_t, "%.2f\n", price);
        printf("\n*******\n");
    }

    fclose(product_t);
    fclose(price_t);

    return (0);
}