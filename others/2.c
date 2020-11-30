#include <stdio.h>
#include <stdlib.h>

void reverse(long n) {
    if (n > 1000)
        reverse(n / 1000);
    printf("%d", n % 1000);
    putchar(',');
}

void reverse2(long n) {
    int s[100];
    int t = -1;
    do {
        s[++t] = n % 1000;
        n /= 1000;
    } while (n);
    for (int i = 0; i <= t; i++) {
        printf("%d", s[t - i]);
        putchar(',');
    }
}

int main(int argc, char const *argv[])
{
    long n;
    scanf("%ld", &n);
    reverse2(n);
    return 0;
}
