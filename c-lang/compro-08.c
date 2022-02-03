#include    <stdio.h>

void input_score(float table[5][4])
{
    for (int p = 0; p < 5; p++)
    {
        table[p][3] = 0;    //sum
    }
    for (int r = 0; r < 3; r++)
    {
        printf("\n*******Exam%d*******\n", r+1);
        for (int p = 0; p < 5; p++)
        {
            printf("Please input score of Student %d: ", p+1);
            scanf("%f", &table[p][r]);
            table[p][3] += table[p][r];
        }
    }
}

void print_score(float table[5][4])
{
    printf("\n*******Table*******\n");
    printf("person\texam1\texam2\texam3\ttotal\n");
    for (int p = 0; p < 5; p++)
    {
        printf("%d\t", p+1);
        for (int r = 0; r < 4; r++)
        {
            printf("%.2f\t", table[p][r]);
        }
        printf("\n");
    }
}

void print_max(float table[5][4])
{
    int score, max[3]; 

    for (int r = 0; r < 3; r++)
    {
        score = 0;
        for (int p = 0; p < 5; p++)
        {
            if (table[p][r] > score)
            {
                score = table[p][r];
                max[r] = p + 1;
            }
        }
    }
    printf("max\t");
    for (int r = 0; r < 3; r++)
        printf("%d\t", max[r]);
    printf("\n");
}

int main(void)
{
    float mytable[5][4];
    input_score(mytable);
    print_score(mytable);
    print_max(mytable);
    return 0;
}