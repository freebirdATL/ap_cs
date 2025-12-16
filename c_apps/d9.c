#include <stdio.h>

int main() {
    //create 10x10 map
    int map[10][10];

    //loop through array and default to 0
    for(int i = 0; i < 10; i++) {
        //loop through columns
        for(int j = 0; j < 10; j++) {
            map[i][j] = 0;
        }
    }

    //loop through array and print
    for(int i = 0; i < 10; i++) {
        //loop through columns
        for(int j = 0; j < 10; j++) {
            //receive values from user
            printf("%d, ", map[i][j]);
        }
        printf("\n");
    }
    for(int k = 0; k < 5; k++) {
        int x_value;
        int y_value;
        printf("give me a coordinate for ship number %d", k);
        scanf("%d", &x_value);
        scanf("%d", &y_value);
        map[x_value][y_value] = 1;
    }

    //loop through array and print
    for(int i = 0; i < 10; i++) {
        //loop through columns
        for(int j = 0; j < 10; j++) {
            //receive values from user
            printf("%d, ", map[i][j]);
        }
        printf("\n");
    }
}