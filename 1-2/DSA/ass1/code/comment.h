#ifndef COMMENT_H
#define COMMENT_H

#include "reply.h"
typedef struct Comment {
    char* username;
    char* content;
    Reply* replies;
    struct Comment* next;
    struct Comment* prev;
} Comment;

Comment* createComment(char* username, char* content); // Creates a comment using the given parameters, returning a pointer to it

#endif // COMMENT_H