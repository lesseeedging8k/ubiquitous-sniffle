#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter string: ");
    scanf("%s", str);
    int len = strlen(str);
    printf("Reversed: ");
    for (int i = len - 1; i >= 0; i--)
        putchar(str[i]);
    putchar('\n');
}
