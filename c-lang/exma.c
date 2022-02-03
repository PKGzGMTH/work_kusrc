/*จงเขียนโปรแกรมคำนวณและแสดงคำนวณอัตราการแลกเปลี่ยนเงินไทยเป็นเงินสกุลดังต่อไปนี้ เมื่อกำหนดให้ 
1) กด D เพื่อเปลี่ยนเป็นเงินสกุล Dollar กำหนดให้ 1 Dollar = 35.5 บาท
2) กด Y เพื่อเปลี่ยนเป็นเงินสกุล Yen กำหนดให้ 1 Yen = 40 บาท
3) เขียนโปรแกรมให้อยุ่ในรูปแบบฟังก์ชันจำนวน 2 ฟังก์ชัน
4) ลักษณะของฟังก์ชันเป็นแบบส่งค่าไปและส่งค่ากลับ
5) หน้าจอโปรแกรมแสดงผลดังตัวอย่างด้านล่าง */
#include    <stdio.h>

float select_exchange(char charecter)
{
    if (charecter == 'D')
    {
        return 35.5;
    }
    else if (charecter == 'Y')
    {
        return 40;
    }
    
}

float calculate(float money, float exchange)
{
    return money/exchange;
}

main()
{
    char choice;
    float money;
    printf("Please input type of money : ");
    scanf("%c", &choice);
    printf("Please input the number of baht : ");
    scanf("%f", &money);
    prinf("%.2f baht = %.2f ", money, calculate(money, select_exchange(choice)));
    if (charecter == 'D')
    {
        printf("Dollar\n");
    }
    else if (charecter == 'Y')
    {
        printf("Yen\n");
    }
    return 0;
}