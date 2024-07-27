#include<stdio.h>
#include<math.h>
int main()
{
    int a,b,c;
    printf("Enter the number :");
    scanf("%d%d",&a,&b);
    c=a+b;
    printf("%d + %d =%d\n",a,b,c);
    c=a-b;
    printf("%d - %d = %d\n",a,b,c);
    c=a*b;
    printf("%d * %d = %d\n",a,b,c);
    c=a/b;
    printf("%d / %d = %d\n",a,b,c);
    c=a%b;
    printf("%d %% %d = %d\n",a,b,c);
    
}
