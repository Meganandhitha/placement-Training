#include<stdio.h>
int main()
{
    int a,b;
    printf("Enter the number :");
    scanf("%d%d",&a,&b);
    if (a>b)
      printf("Result: %d\n",(a/b));
    if (a<b)
      printf("Result: %d\n",(a*b));
    return 0;
}
    
