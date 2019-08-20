#include<stdio.h>
#include<stdlib.h>

struct TreeNode;

struct TreeNode{
   int val;
   struct TreeNode *left;
   struct TreeNode *right;
};


typedef struct TreeNode TreeNode;

int add(TreeNode **root, int val){
  if (root == NULL) { return -1; }

  if (*root == NULL) {
     *root = (TreeNode *)malloc(sizeof(TreeNode));
     (*root)->val=val;
     (*root)->left=NULL;
     (*root)->right=NULL;
     return 0;}

  if (*root != NULL) {
      if (val<(*root)->val){
      (*root)->left= (TreeNode *)malloc(sizeof(TreeNode));
      ((*root)->left)->val=val;
         return 0;}
      if (val>(*root)->val){
      (*root)->right= (TreeNode *)malloc(sizeof(TreeNode));
      ((*root)->right)->val=val;
         return 0;}
  }


int print(TreeNode *root, int val){
   if (root == NULL) { return -1; }
   else{
     printf("(root->left)->val=%d \n",(root->left)->val);
     printf(" root->val=%d \n",root->val);
     printf("(root->right)->val=%d \n",(root->right)->val);}}


