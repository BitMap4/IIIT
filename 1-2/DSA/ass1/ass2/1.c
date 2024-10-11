
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
    int data;
    struct node* left;
    struct node* right;
} node;
typedef struct node* tree;

typedef struct queue {
    tree* arr;
    int front;
    int rear;
} queue;

void printTree(tree root, char* path) {
    if (root == NULL) return;
    if (root->left == NULL && root->right == NULL) {
        printf("%s%d\n", path, root->data);
        return;
    }
    char leftPath[1000];
    char rightPath[1000];
    sprintf(leftPath, "%s%s%d", path, " left ", root->data);
    sprintf(rightPath, "%s%s%d", path, " right ", root->data);
    printTree(root->left, leftPath);
    printTree(root->right, rightPath);
}

// class Solution(object):
// def minCameraCover(self, root):
//     def solve(node):
//         # 0: Strict ST; All nodes below this are covered, but not this one
//         # 1: Normal ST; All nodes below and incl this are covered - no camera
//         # 2: Placed camera; All nodes below this are covered, plus camera here

//         if not node: return 0, 0, float('inf')
//         L = solve(node.left)
//         R = solve(node.right)

//         dp0 = L[1] + R[1]
//         dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
//         dp2 = 1 + min(L) + min(R)

//         return dp0, dp1, dp2

//     return min(solve(root)[1:])

int min(int a, int b) {
    return a < b ? a : b;
}

int* solve(tree root) {
    int* result = (int*)malloc(3 * sizeof(int));
    if (root == NULL) {
        result[0] = 0;
        result[1] = 0;
        result[2] = 1000000000;
        return result;
    }
    int* L = solve(root->left);
    int* R = solve(root->right);

    result[0] = L[1] + R[1];
    result[1] = min(L[2] + min(R[1], R[2]), R[2] + min(L[1], L[2]));
    result[2] = 1 + min(L[0], min(L[1], L[2])) + min(R[0], min(R[1], R[2]));

    return result;
}

int main() {
    int n, x=0;
    scanf("%d", &n);
    int arr[n];

    // while (n--){
    //     scanf("%d", &arr[0]);
    //     x+=arr[0];
    // }
    // printf("%d", (x+2)/3);

    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    tree root = (tree)malloc(sizeof(node));
    root->data = arr[0];
    queue* q = (queue*)malloc(sizeof(queue));
    q->arr = (tree*)malloc(n * sizeof(tree));
    q->front = 1;
    q->rear = 1;

    for (int i = 1; i < n; i++) {
        q->arr[q->rear] = (tree)malloc(sizeof(node));
        q->arr[q->rear]->data = arr[i];
        q->rear++;
    }

    int i=1;
    tree temp = root;
    while (q->front < q->rear) {
        if (i >= n) break;
        // printf("%d\n", i);
        if (arr[i] != 0) {
            temp->left = q->arr[i];
        }
        i++;
        if (arr[i] != 0) {
            temp->right = q->arr[i];
        }
        i++;
        do temp = q->arr[q->front++];
        while (temp!=NULL && temp->data == 0 && q->front < q->rear);
    }

    root->data = 0;
    for (int i = 1; i < n; i++) q->arr[i]->data = 0;

    int* result = solve(root);
    printf("%d", min(result[1], result[2]));
    // printTree(root, "0");


    return 0;
}
