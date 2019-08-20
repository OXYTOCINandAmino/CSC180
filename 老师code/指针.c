#include <stdio.h>

int main(void){
int *a;
a=(int*)malloc(sizeof(int));
*a=9;
printf("*a=%d a=%p",*a,a);
}
