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


int genFormula(atom *pAtom,int **output,int *size){
    int L[300];
    int i;
    int x=0;
    int y=0;
    int *z;

    for(i=0;i<300;i++){
    L[i]=0;}

    genAtom(pAtom,L);

    for(i=0;i<300;i++){
        printf("%d",L[i]);
    }

    for(i=0;i<300;i++){
      if(L[i]!=0){
        x=x+1;}}

    if(size==NULL||output==NULL){
            return -1;}
    else{
    size=(int*)malloc(sizeof(int));
    *size=2*x;
    printf("%d",*size);}

    *output=(int*)malloc(sizeof(int)*6);
    printf("%d",sizeof(z));
    printf("here1");
    for(i=0;i<300;i++){
      if(L[i]!=0){
        printf("here2");
        *output[y]=i;
        printf("here3");
        *output[y+1]=L[i];
        printf("here4");
        y=y+2;
        z=z+2;}}

        return 0;}






int genAtom(atom *pAtom, int *L) {
    int n;
    if (pAtom == NULL) { return -1;}
    else{
        n= pAtom->atomicNumber;
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
   int i;
   atom *S;
   atom *tmp1,*tmp2;
   int *Output;
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

   genFormula(S,&Output,size);

}
