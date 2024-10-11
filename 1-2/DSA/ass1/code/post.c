#include "post.h"

Post* createPost(char* username, char* caption) {
    Post* post = (Post*) malloc(sizeof(Post));
    post->username = strdup(username);
    post->caption = strdup(caption);
    post->comments = NULL;
    post->next = NULL;
    post->prev = NULL;
    return post;
}
