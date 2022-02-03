#include <stdio.h>
int amount,state = 1;
float exchangeRate;
char currency, *currencyName;

void main() {
    
    system("cls");
    printf("USD [D/d]\nJPY [Y/y]\nKRW [K/k]\n");
    printf("Select currency : ");
    scanf("%c", &currency);

    if (currency == 'D' || currency == 'd'){
        exchangeRate = 33.46;
        currencyName = "USD";
    } else if (currency == 'Y' || currency == 'y'){
        exchangeRate = 0.29;
        currencyName = "JPY";
    } else if (currency == 'K' || currency == 'k'){
        exchangeRate = 35.28;
        currencyName = "KRW";
    } else {
        printf("Currency Not match! please try again.\n");
        state = 0;
    }

    if (state == 1){
        printf("Enter amount : ");
        scanf("%d", &amount);
        printf("%d THB = %.2f %s", amount, amount/exchangeRate, currencyName);
    }
}