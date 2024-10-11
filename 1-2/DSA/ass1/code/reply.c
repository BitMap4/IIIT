#include "reply.h"

Reply* createReply(char* username, char* content) {
    Reply* reply = (Reply*) malloc(sizeof(Reply));
    reply->username = strdup(username);
    reply->content = strdup(content);
    reply->next = NULL;
    reply->prev = NULL;
    return reply;
}