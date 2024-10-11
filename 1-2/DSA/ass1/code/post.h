#ifndef POST_H
#define POST_H

#include "comment.h"
typedef struct Post {
    char* username;
    char* caption;
    Comment* comments;
    struct Post* next;
    struct Post* prev;
} Post;

Post* createPost(char* username, char* caption); // Creates a post using the given parameters, returning a pointer to it

#endif // POST_H