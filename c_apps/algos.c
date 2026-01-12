#include <stdio.h>

int main() {
    int a = 97;
    int b = 'b';
    //int c = "c"; //incompatible pointer to integer conversion
    char d = a;
    char e = (char)a;
    printf(
        "a: %d\n"
        "b: %d\n"
        "b: %c\n"sadfsdf
        // "c: %d\n"
        // "c: %c\n"
        // "c: %s\n"
        "d: %d\n"
        "d: %c\n"
        // "d: %s\n"
        "e: %d\n"
        "e: %c\n"
        //"e: %s\n"
        ,a,b,b,d,d,e,e
    );
}