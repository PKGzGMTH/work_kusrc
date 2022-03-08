#include <stdio.h>
float farenheit, celcius;

void calfarenheit(float celcius){
    farenheit = (celcius/1.8) + 32;
    printf("%.2f celcius = %.2f Farenheit", celcius,farenheit);
}

void main(){
    printf("Enter temperature in Farenheit: ");
    scanf("%f", &celcius);
    calfarenheit(celcius);
}
