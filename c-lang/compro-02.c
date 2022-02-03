#include <stdio.h>

float farenheit, celcius;

void main(){
    printf("Enter temperature in Farenheit: ");
    scanf("%f", &farenheit);
    printf("%.2f Farenheit = %.2f celcius", farenheit, celcius = (farenheit - 32) * 1.8);
}