#include <stdio.h>
#include <stdlib.h>
int i = 1;
void other();

int main(int argc, char const *argv[])
{
    static int a;
    register int b = -10;
    int c = 0;
    printf("---Main---\n");
    printf("i:%d a:%d b:%d c %d\n", i, a, b, c);
    c = c + 8;
    other();
    printf("---Main---\n");
    printf("i:%d a:%d b:%d c %d\n", i, a, b, c);
    i = i + 10;
    other();
    return 0;
}

void other() {
    static int a = 2;
    static int b;
    int c = 10;
    a = a + 2;
    i = i + 32;
    c = c + 5;
    printf("---Other---\n");
    printf("i:%d a:%d b:%d c %d\n", i, a, b, c);
    b = a;
}