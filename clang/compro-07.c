#include <stdio.h>
inputMatrix(int row, int colum, int matrix[row][colum], char name){
    printf("\n*****Input Matrix%c*******\n",name);
    for (int rowMatrix = 0; rowMatrix < row; rowMatrix++){
        for (int columMatrix = 0; columMatrix < colum; columMatrix++){
            printf("Please input Matrix%c[%d][%d]: ",name , rowMatrix+1, columMatrix+1);
            scanf("%d", &matrix[rowMatrix][columMatrix]);
        }
    }
    printf("\n*****Matrix%c*******\n",name);
    for (int rowMatrix = 0; rowMatrix < row; rowMatrix++){
        for (int columMatrix = 0; columMatrix < colum; columMatrix++){
            printf("%d\t", matrix[rowMatrix][columMatrix]);
        }
        printf("\n");
    }
}
sumMatrix(int row, int colum, int matrixa[row][colum], int matrixb[row][colum]){
    printf("\n*****Result*******\n");
    for (int rowMatrix = 0; rowMatrix < row; rowMatrix++){
        for (int columMatrix = 0; columMatrix < colum; columMatrix++){
            printf("%d\t", matrixa[rowMatrix][columMatrix] + matrixb[rowMatrix][columMatrix]);
        }
        printf("\n");
    }
}
main(){
    int row,colum;
    printf("Please input number of row: ");
    scanf("%d", &row);
    if (row > 20) row = 20;
    printf("Please input number of colum: ");
    scanf("%d", &colum);
    if (colum > 20) colum = 20;
    int matrixA[row][colum], matrixB[row][colum];
    inputMatrix(row, colum, matrixA, 'A');
    inputMatrix(row, colum, matrixB, 'B');
    sumMatrix(row, colum, matrixA, matrixB);
}