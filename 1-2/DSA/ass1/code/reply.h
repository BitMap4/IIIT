#ifndef REPLY_H
#define REPLY_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Reply {
    char* username;
    char* content;
    struct Reply* next;
    struct Reply* prev;
} Reply;

Reply* createReply(char* username, char* content); // Creates a reply using the given parameters, returning a pointer to it

#endif // REPLY_H