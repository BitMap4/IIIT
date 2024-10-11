#include <stdio.h>
#include <stdlib.h>
#define MAX 200009

typedef struct node* Node;
typedef struct node* List;
typedef struct node {
    int book;
    int data;
    Node next;
} node;

List insert(List* end, int book, int data) {
    List list = end[book%(MAX-9)];
    Node new = (Node)malloc(sizeof(node));
    new->book = book;
    new->data = data;
    if (list == NULL) {
        new->next = NULL;
        list = new;
    } else {
        Node curr = list;
        while (curr->next != NULL) {
            if (curr->book == book) {
                curr->data = data;
                return list;
            }
            curr = curr->next;
        }
        if (curr->book == book) {
            curr->data = data;
            return list;
        }
        curr->next = new;
        new->next = NULL;
    }
    return list;
}

int getData(List* end, int book) {
    Node curr = end[book%(MAX-9)];
    while (curr != NULL) {
        if (curr->book == book) return curr->data;
        curr = curr->next;
    }
    return 0;
}

int main(){
    int n;
    scanf("%d", &n);
    int books[n];
    List end[MAX] = {NULL};
    int max=0, max_index=0;
    for (int i=0; i<n; i++) {
        scanf("%d", &books[i]);
    }

    for (int i=0; i<n; i++) {
        int data = getData(end, books[i]-1) + 1;
        end[books[i]%(MAX-9)] = insert(end, books[i], data);
    }

    for (int i=0; i<n; i++) {
        int data = getData(end, books[i]);
        if (data > max) {
            max = data;
            max_index = books[i];
        }
    }

    printf("%d\n", max);

    int curr = max_index - max + 1, i=0;
    while (curr != max_index+1) {
        if (books[i] == curr) {
            printf("%d ", i);
            curr++;
        }
        i++;
    }
    return 0;
}