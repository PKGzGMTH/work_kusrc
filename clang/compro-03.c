#include <stdio.h>
int volume;
float commission;
char *status;

void main() {
    printf("Enter Volume of cosmetics : ");
    scanf("%d", &volume);
    if (volume > 70000) {
        commission = volume * 0.07;
        status = "Good Performance";
        }
    else {
        commission = volume * 0.03;
        status = "Low Performance";
        }
    printf("Volume of cosmetics = %d\n", volume);
    printf("Commission = %.2f\n", commission);
    printf("%s\n", status);
}