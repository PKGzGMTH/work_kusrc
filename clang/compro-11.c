#include    <stdio.h>
#include    <string.h>

int main(void)
{
    char    str1[50], str2[50], chr;
    int     size = 0;

    printf("Enter a string 1: ");
    gets(str1);
    printf("Enter a string 2: ");
    gets(str2);

    printf("All string = %s\n\n", strcat(str1, str2));
    printf("*****************\nFind a Character : ");
    chr = getchar();

    for (size_t i = 0; i < strlen(str1); i++)
        if (str1[i] == chr) size++;
    printf("Number of %c = %d", chr, size);
    return (0);
}