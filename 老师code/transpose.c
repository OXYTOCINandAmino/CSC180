#include<stdio.h>
#include<stdlib.h>

int transpose(float *in,int rows,int cols,float **out) {
   int r=0, c=0;

   if (in == NULL) { return -1; }
   if (out == NULL) { return -1; }
   (*out) = (float *)malloc(sizeof(float)*rows*cols);
   if (*out == NULL) { return -1; }

   for(r=0;r<rows;r=r+1) {
      for(c=0;c<cols;c=c+1) {
	 /* (*out)[r*cols+c]=in[r*cols+c]; */ /* out = in */
         (*out)[c*rows+r]=   in[r*cols+c];    /* out = transpose(in) */
      }
   }
   return 0;
}

int main(void) {
   int rows=3;
   int cols=4;
   int r;
   int c;
   float in[] = {1,2,3,4, 5,6,7,8, 9,10,11,12};
   float *out;
   int error;

   for(r=0;r<rows;r=r+1) {
      for(c=0;c<cols;c=c+1) {
         printf("%8.3f   ",in[r*cols+c]);
      }
      printf("\n");
   }

   error = transpose(in,rows,cols,&out);
   if (error != 0) { printf("ERROR!\n"); return -1; }

   printf("\n... and the transpose is ...\n\n");
   for(r=0;r<cols;r=r+1) {
      for(c=0;c<rows;c=c+1) {
         printf("%8.3f   ",out[r*rows+c]);
      }
      printf("\n");
   }

   return 0;
}
