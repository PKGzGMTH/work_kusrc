#include<stdio.h>
#include<stdlib.h>

int base[16][4] = {
    {0,0,0,0},
    {0,0,0,1},
    {0,0,1,0},
    {0,0,1,1},
    {0,1,0,0},
    {0,1,0,1},
    {0,1,1,0},
    {0,1,1,1},
    {1,0,0,0},
    {1,0,0,1},
    {1,0,1,0},
    {1,0,1,1},
    {1,1,0,0},
    {1,1,0,1},
    {1,1,1,0},
    {1,1,1,1},
};

void main(void)
{
    for(int index = 0; index < 16; index++){
        int num = ((base[index][0]*8) + (base[index][1]*4) + (base[index][2]*2) + (base[index][3]*1));
        printf("\n%d", num);
    }

}