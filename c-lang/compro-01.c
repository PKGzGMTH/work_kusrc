#include <stdio.h>

int num1 = 100, num2 = 2000;
float num3 = 3000, num4 = 25.6789, num5 = 101.101;
char name1[] = "coding is simple", name2[] = "C & C++", name3[] = "Computer";

int	main()
{
    printf("num1 \t= %6d\n", num1);
    printf("num2 \t= %-7d\n", num2);
    printf("num3 \t= %12f\n", num3);
    printf("num4 \t= %5.2f\n", num4);
    printf("num5 \t= %-7.1f\n", num5);
    printf("name1 \t=%.3s\n", name1);
    printf("name2 \t=%9s\n", name2);
    printf("name3 \t=%-10s\n", name3);
    return (0);
}
