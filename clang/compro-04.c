#include <stdio.h>
int amount,state = 1;
float exchangeRate;
char currency, *currencyName;

void main() {
    
    system("cls");
    printf("USD [D/d]\nJPY [Y/y]\nKRW [K/k]\n");
    printf("Select currency : ");
    scanf("%c", &currency);



    switch (currency) {
    case 'D': case 'd':
        exchangeRate = 33.46;
        currencyName = "USD";
        break;
    case 'Y': case 'y':
        exchangeRate = 0.29;
        currencyName = "JPY";
        break;
    case 'K': case 'k':
        exchangeRate = 35.28;
        currencyName = "KRW";
        break;

    default:
        printf("Currency Not match! please try again.\n");
        state = 0;
        break;
    }

    if (state == 1){
        printf("Enter amount : ");
        scanf("%d", &amount);
        printf("%d THB = %.2f %s", amount, amount/exchangeRate, currencyName);
    }
}