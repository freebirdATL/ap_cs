#include <stdio.h>

    char player1_map[10][10][5];
    char player2_map[10][10][5];
    char name_p1[10];
    char name_p2[10];

void game_setup() {
    //player 1 name input
    printf("\nProvide a name for player 1: ");
    scanf("%s", name_p1);
    printf("Welcome, %s\n\n", name_p1);
    //player 2 name input
    printf("\nProvide a name for player 2: ");
    scanf("%s", name_p2);
    printf("Welcome, %s\n\n", name_p2);
}

void ship_allocation(char player_name[10], char player_map[10][10][5]) {
    printf("%s, allocate your 5 ships:\n\n", player_name);

    for(int i = 0; i < 10; i++) {
        printf("row %d: ",i);
        for(int j = 0; j < 10; j++) {
            printf("%s, ", player_map[i][j]);
        }
        printf("\n");
    }

}

int main() {
    game_setup();
    ship_allocation(name_p1, player1_map);
    ship_allocation(name_p2, player2_map);
}