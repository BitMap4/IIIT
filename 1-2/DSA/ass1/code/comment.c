#include "comment.h"

Comment* createComment(char* username, char* content) {
    Comment* comment = (Comment*) malloc(sizeof(Comment));
    comment->username = strdup(username);
    comment->content = strdup(content);
    comment->replies = NULL;
    comment->next = NULL;
    comment->prev = NULL;
    return comment;
}