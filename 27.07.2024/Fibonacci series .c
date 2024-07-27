#include <stdio.h>

int main() {
    int N, first = 0, second = 1, next;
    printf("Enter the number of terms: ");
    scanf("%d", &N);

    printf("Fibonacci series: ");
    for (int i = 0; i < N; i++) {
        if (i <= 1)
            next = i;
        else {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%d ", next);
    }
    printf("\n");
    return 0;
}
