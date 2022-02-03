#include <stdio.h>
int number;
int primenumber(int number){
    int div = 2;
    while (number >= 2) {
        if (number == 2) return 1;
        else {
            if (number%div == 0) {
                number = number/div;
                return 0;
                }
            else div += 1;
            if (number <= div) return 1;
        }
    }
    return 0;
}
void main(){
    printf("Enter number: ");
    scanf("%d", &number);
    if (primenumber(number)) printf("%d is Prime Number\n", number);
    else printf("%d is not Prime Number\n", number);
}