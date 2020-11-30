#include <stdio.h>

long fib(int n) {
    if (n == 1 || n == 2) 
        return 1;
    return fib(n - 1) + fib(n - 2);
}

int main(int argc, char const *argv[])
{
    int n;
    scanf("%d", &n);
    printf("%d", fib(n));
    return 0;
}
