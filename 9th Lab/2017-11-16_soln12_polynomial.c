#include <stdio.h>
#include <stdlib.h>

/* 
12. (25 points) You’re required to write a C program to do symbolic calculus of univariate polynomials.
(a) (2 points) How would you represent the term of a univariate polynomial in C?
(b) (6 points) Write a function, monkey, that takes in an arg of the type you defined above, and re- turns an appropriate return variable to represent the result of integrating a univariate polynomial term.
(c) (6 points) Write a function, chicken, that takes in an arg of the type you defined above, and a second arg for the output, and assigns the output so that it represents the first derivative of the input univariate polynomial term. Assume the caller allocated the second arg.
(d) (5 points) Rewrite (c) assuming the caller did not allocate the second arg.
(e) (6 points) Show how a caller would call the above functions for all three cases. Include the definition of all variables that will be arguments and return values of the functions.
*/

struct term {
   float coeff;
   int power;
   int invalid;
};

typedef struct term termT;

termT monkey(termT arg) {
   termT rval;
   if (arg.power == -1) {
      rval.invalid = 1;
      return rval;
   }
   rval.invalid = 0;
   rval.coeff = arg.coeff/(1+arg.power);
   rval.power = arg.power+1;
   return rval;
}

int chicken_a(termT arg_in,termT *arg_out) {
   if (arg_out == NULL) { return -1; }
   arg_out->power = arg_in.power - 1;
   arg_out->coeff = arg_in.coeff * arg_in.power;
   arg_out->invalid = 0;
   return 0;
}

int chicken_b(termT arg_in,termT **arg_out) {
   if (arg_out == NULL) { return -1; }
   *arg_out = (termT *)malloc(sizeof(termT));
   (*arg_out)->power = arg_in.power - 1;
   (*arg_out)->coeff = arg_in.coeff * arg_in.power;
   (*arg_out)->invalid = 0;
   return 0;
}

int main(void) {
  termT arg;
  termT integ;
  termT diff;
  termT *pdiff;

  arg.coeff = 100.5;
  arg.power = 3;
  integ = monkey(arg);
  printf("integral of %f*x^(%d) is %f*x^(%d)\n",arg.coeff,arg.power,integ.coeff,integ.power); 

  chicken_a(integ,&diff);
  printf("diff     of %f*x^(%d) is %f*x^(%d)\n",integ.coeff,integ.power,diff.coeff,diff.power); 

  chicken_b(integ,&pdiff);
  printf("diff     of %f*x^(%d) is %f*x^(%d)\n",integ.coeff,integ.power,pdiff->coeff,pdiff->power); 

  return 0;
}
