#include <stdio.h>

void move(char getone, char putone) {
    printf("%c -> %c\n", getone, putone);
}

void hanoi(int n, char one, char two, char three) {
    if (n == 1) move(one, three);
    else {
        hanoi(n - 1, one, three, two);
        move(one, three);
        hanoi(n - 1, two, one, three);
    }
}

int main(int argc, char const *argv[])
{
    int m;
    printf("input n: ");
    scanf("%d", &m);
    hanoi(m, 'A', 'B', 'C');
    return 0;
}
