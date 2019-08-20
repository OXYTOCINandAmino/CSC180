#include <stdio.h>

void printArr(int *a, int n);

void printArr(int *a, int n) {
    // NEED to pass in n ***
    // if you try: sizeof(a)/sizeof(int) you will always get 2
    // because sizeof(int *) is always 8
    //         sizeof(int)   is always 2
    int i;
    for(i=0;i<n;i++){
       printf("a[%d]=%d located at %p\n",i,a[i],&(a[i])); // equivalent
       printf("a[%d]=%d located at %p\n",i,*(a+i),a+i);   // equivalent
    }
}

int main(void) {

   int a[] = {1,2,3,4,5}; // this is how you define an array
                          // with initial values
                          // this syntax can ONLY be used when
                          // defining an array variable, as shown,
                          // and you can not use {1,...} any other way
                          // as the comments below indicate
   int b[6];
   int len_a;
   int i;

   b[0]=10;
   b[1]=100;
   b[2]=1000;
   b[3]=10000;
   b[4]=100000;
   b[5]=1000000;
   // YOU CAN NOT DO: b = {10,100,...}

   len_a = (int)(sizeof(a)/sizeof(int));
      // 1. This is not necessary; sizeof should never be used in your
      //    program except when you malloc. I only show this here as an
      //    example of how len can be derived. It isn't necessary, since
      //    the programmer already knows that a is 5 elements long.
      //    You should really say "len_a=5".
      // 2. Having said that: for those of you who mentioned you can
      //    derive size of an array via the sizeof() function --- YES
      //    you can use sizeof (but shouldn't) where the array has been
      //    defined, but NO you can not use sizeof() to get the size of
      //    an array once you are in a function where the pointer/address
      //    of the array has been passed in. See above (printArray ***)
      // 3. You have to use (int)(...) to convert the sizeof() expression
      //    from (long int) to int --- otherwise gcc will give warnings
      //    and you must ALWAYS ensure ALL warnings are eliminated by
      //    correcting your code.
   printArr(a,len_a);
   printArr(b,6);
   //printArr({1,2,3,4,5},5);  ... this doens't work
   return 0;
}
