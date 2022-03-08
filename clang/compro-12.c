#include    <stdio.h>
#include    <stdlib.h>

typedef struct
{
    int electric;
    int water;
    int trash;
    int central;
}   s_utilities;

int is_num(char *str)
{
    while (*str != 0)
    {
        if ('0' <= *str && *str <= '9')
            str++;
        else
        {
            printf("Error!\n");
            return (0);
        }
    }
    return (1);
}

int input_value(s_utilities *room_util, int room_num)
{
    char    str[50];

    printf("Room number %d\n", room_num + 1);
    printf("Enter number of electric: ");
    gets(str);
    if (is_num(str))
        room_util -> electric = atoi(str);
    else
        return (0);

    printf("Enter number of water: ");
    gets(str);
    if (is_num(str))
        room_util -> water = atoi(str);
    else
        return (0);

    room_util -> trash = 100;
    room_util -> central = 150;
    printf("Added !\n\n");
    return (1);
}

void    print_output(s_utilities *room_util, int room_num)
{
    float   cost;

    printf("Room number %d\n", room_num + 1);
    printf("Number of Electric = %d ", room_util->electric);
    printf("Cost of Electric = %.2f\n", (float)room_util->electric * 15);
    printf("Number of Water = %d ", room_util->water);
    printf("Cost of Water = %.2f\n", (float)room_util->water * 30);
    printf("Cost of waste = %.2f\n", (float)room_util->trash);
    printf("Cost of service = %.2f\n", (float)room_util->central);
    cost = (room_util->electric * 15) + (room_util->water * 30) + room_util->trash + room_util->central;
    printf("Cost of Room number %d = %.2f\n", room_num + 1, cost);
    printf("***********************\n");
}

void    print_high(s_utilities *room_util, int count)
{
    int     room, max;

    room = 0;
    max = 0;
    for(int i = 0; i < count; i++)
    {
        if (room_util[i].electric > max)
        {
            max = room_util[i].electric;
            room = i;
        }
    }
    
    printf("High electric is Room number%d\n", room + 1);

    room = 0;
    max = 0;
    for(int i = 0; i < count; i++)
    {
        if (room_util[i].water > max)
        {
            max = room_util[i].water;
            room = i;
        }
    }
    printf("High water is Room number%d\n", room + 1);
}

int main(void)
{
    int stat = 1;
    int count = 3;
    s_utilities *room;

    room = (s_utilities *) malloc (sizeof(s_utilities) * count);
    for (int i = 0; i < count; i++)
    {
        if (input_value(&room[i], i))
            continue ;
        else
        {
            stat = 0;
            break;
        }
    }
    if (stat == 1)
    {
        for (int i = 0; i < count; i++)
            print_output(&room[i], i);
    }
    printf("\n");
    print_high(room, count);
    free(room);
    return (0);
}