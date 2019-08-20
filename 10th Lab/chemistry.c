

#include<stdio.h>
#include<stdlib.h>

struct bondNode;
struct atom;

struct bondNode {
   int strength;
   struct atom *pAtom;
   struct bondNode *pNext;
};

struct atom {
   int atomicNumber;
   struct bondNode *bondList;
};

typedef struct bondNode bondNode;
typedef struct atom atom;

int addBond(atom *pAtom, int strength, atom *pAtom2);
atom *createAtom(int atomicNumber);
int bondList_add(bondNode **ppList, int strength, atom *pAtom);
int printAtom(atom *pAtom,int n);
int printBonds(bondNode *pList,int n);
int genFormula(atom *pAtom,int **output,int *size);
int genAtom(atom *pAtom, int *L);
int genBonds(bondNode *pList,int *L);


atom *createAtom(int atomicNumber) {
   atom *p=(atom *)malloc(sizeof(atom));
   p->atomicNumber = atomicNumber;
   p->bondList = NULL;
   return p;
}

int bondList_add(bondNode **ppList, int strength, atom *pAtom) {
   if (ppList == NULL) { return -1; }
   if (*ppList == NULL) {
      *ppList = (bondNode *)malloc(sizeof(bondNode));
      (*ppList)->strength=strength;
      (*ppList)->pAtom=pAtom;
      (*ppList)->pNext=NULL;
      return 0;
   } else {
      return bondList_add( &((*ppList)->pNext), strength, pAtom );
   }
}

int addBond(atom *pAtom, int strength, atom *pAtom2) {
   if (pAtom == NULL) { return -1; }

   return bondList_add( &(pAtom->bondList), strength, pAtom2);
}

int printAtom(atom *pAtom,int n) {
   int i;
   if (pAtom == NULL) {
      printf("black hole sun...\n");
   } else {
      for(i=0;i<n;i=i+1) {
         printf("   ");
      }
      printf("-> atomic number=%d: bonded to:\n",pAtom->atomicNumber);
      printBonds(pAtom->bondList,n);
      for(i=0;i<n;i=i+1) {
         printf("   ");
      }
      printf("<- atomic number=%d\n",pAtom->atomicNumber);

   }
   return 0;
}

int printBonds(bondNode *pList,int n) {
   int i;
   for(i=0;i<n;i=i+1) {
      printf("   ");
   }
   if (pList == NULL) {
      printf("no bonds\n");
   } else {
      printf("strength=%d connected to:\n",pList->strength);
      printAtom(pList->pAtom,n+1);
      printBonds(pList->pNext,n);
   }
   return 0;
}

int genFormula(atom *pAtom,int **output,int *size){
    int L[300];
    int i;
    int x=0;
    int y=0;

    for(i=0;i<300;i++){
    L[i]=0;}

    genAtom(pAtom,L);

        for(i=0;i<300;i++){
        printf("%d",L[i]);
    }

    for(i=0;i<300;i++){
      if(L[i]!=0){
        x=x+1;}}

    *size=2*x;
    printf("%d",*size);
    *output=(int*)malloc(2*x*sizeof(int));

    for(i=0;i<300;i++){
      if(L[i]!=0){
        *output[y]=i;
        *output[y+1]=L[i];
        y=y+2;}}

    return **output;}

   int genAtom(atom *pAtom, int *L) {
    int n;
    if (pAtom == NULL) { return -1;}
    else{
        int n= pAtom->atomicNumber;
        L[n]=L[n]+1;
        genBonds(pAtom->bondList,L);}
    return 0;}

int genBonds(bondNode *pList,int *L){
   if (pList == NULL) { return -1;}
   else {
      genAtom(pList->pAtom,L);
      genBonds(pList->pNext,L);}
}


int main(void) {
   int r=0;
   atom *S;
   atom *tmp1,*tmp2;
   int *output;
   int *size;

   S = createAtom(16);

   tmp1=createAtom(8);
   r=addBond(S,2,tmp1);

   tmp1=createAtom(8);
   r=addBond(S,2,tmp1);

   tmp1=createAtom(8);
   tmp2=createAtom(1);
   r=addBond(tmp1,1,tmp2);
   r=addBond(S,1,tmp1);

   tmp1=createAtom(8);
   tmp2=createAtom(1);
   r=addBond(tmp1,1,tmp2);
   r=addBond(S,1,tmp1);

   printAtom(S,0);
   genFormula(S,&output,size);
   return 0;
}
