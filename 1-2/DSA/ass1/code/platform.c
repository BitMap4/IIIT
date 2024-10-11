#include "platform.h"

Platform* platform = NULL;

Platform* createPlatform() {
    Platform* platform = (Platform*) malloc(sizeof(Platform));
    platform->lastViewedPost = NULL;
    platform->posts = NULL;
    return platform;
}

bool addPost(char* username, char* caption) {
    Post* post = createPost(username, caption);
    if (post == NULL) {
        return false;
    }
    if (platform->posts == NULL) {
        platform->posts = post;
        platform->lastViewedPost = post;
        return true;
    } else {
        Post* currentPost = platform->posts;
        while (currentPost->next != NULL) currentPost = currentPost->next;
        currentPost->next = post;
        post->prev = currentPost;
        if (!platform->lastViewedPost) {
            platform->lastViewedPost = post;
        }
        return true;
    }
}

void freePost(Post* currentPost) {
    if (platform->lastViewedPost == currentPost) {
        platform->lastViewedPost = platform->posts;
    }
    while (currentPost->comments != NULL) {
        Comment* currentComment = currentPost->comments;
        currentPost->comments = currentComment->next;
        while (currentComment->replies != NULL) {
            Reply* currentReply = currentComment->replies;
            currentComment->replies = currentReply->next;
            free(currentReply);
        }
        free(currentComment);
    }
    free(currentPost);
}

bool deletePost(int n) {
    if (platform->posts == NULL) {
        return false;
    }
    Post* currentPost = platform->posts;
    while (currentPost->next != NULL) currentPost = currentPost->next;
    int i = 1;
    while (currentPost != NULL) {
        if (i == n) {
            if (currentPost->prev != NULL) {
                currentPost->prev->next = currentPost->next;
            }
            if (currentPost->next != NULL) {
                currentPost->next->prev = currentPost->prev;
            }
            freePost(currentPost);
            return true;
        }
        currentPost = currentPost->prev;
        i++;
    }
    return false;
}

Post* viewPost(int n) {
    if (platform->posts == NULL) {
        return NULL;
    }
    Post* currentPost = platform->posts;
    while (currentPost->next != NULL) currentPost = currentPost->next;
    int i = 1;
    while (currentPost != NULL) {
        if (i == n) {
            platform->lastViewedPost = currentPost;
            return currentPost;
        }
        currentPost = currentPost->prev;
        i++;
    }
    return NULL;
}

Post* currPost() {
    return platform->lastViewedPost;
}

Post* nextPost() {
    if (platform->lastViewedPost == NULL) {
        return NULL;
    }
    platform->lastViewedPost = platform->lastViewedPost->prev;
    return platform->lastViewedPost;
}

Post* previousPost() {
    if (platform->lastViewedPost == NULL) {
        return NULL;
    }
    platform->lastViewedPost = platform->lastViewedPost->next;
    return platform->lastViewedPost;
}

bool addComment(char* username, char* content) {
    if (platform->lastViewedPost == NULL) {
        return false;
    }
    Comment* comment = createComment(username, content);
    if (comment == NULL) {
        return false;
    }
    if (platform->lastViewedPost->comments == NULL) {
        platform->lastViewedPost->comments = comment;
        return true;
    } else {
        Comment* currentComment = platform->lastViewedPost->comments;
        while (currentComment->next != NULL) {
            currentComment = currentComment->next;
        }
        currentComment->next = comment;
        comment->prev = currentComment;
        return true;
    }
}

void freeComment(Comment* currentComment) {
    while (currentComment->replies != NULL) {
        Reply* currentReply = currentComment->replies;
        currentComment->replies = currentReply->next;
        free(currentReply);
    }
    free(currentComment);
}

bool deleteComment(int n) {
    if (platform->lastViewedPost == NULL) {
        return false;
    }
    Comment* currentComment = platform->lastViewedPost->comments;
    if (currentComment == NULL) return false;
    while (currentComment->next != NULL) currentComment = currentComment->next;
    int i = 1;
    while (currentComment != NULL) {
        if (i == n) {
            if (currentComment == platform->lastViewedPost->comments) {
                platform->lastViewedPost->comments = currentComment->next;
                if (platform->lastViewedPost->comments != NULL) {
                    platform->lastViewedPost->comments->prev = NULL;
                }
                freeComment(currentComment);
                return true;
            }
            currentComment->prev->next = currentComment->next;
            if (currentComment->next != NULL) {
                currentComment->next->prev = currentComment->prev;
            }
            freeComment(currentComment);
            return true;
        }
        currentComment = currentComment->prev;
        i++;
    }
    return false;
}

Comment* viewComments() {
    if (platform->lastViewedPost == NULL) {
        return NULL;
    }
    return platform->lastViewedPost->comments;
}

bool addReply(char* username, char* content, int n) {
    if (platform->lastViewedPost == NULL) {
        return false;
    }
    Comment* currentComment = platform->lastViewedPost->comments;
    if (currentComment == NULL) return false;
    while(currentComment->next != NULL) currentComment = currentComment->next;
    int i = 1;
    while (currentComment != NULL) {
        if (i == n) {
            Reply* reply = createReply(username, content);
            if (reply == NULL) {
                return false;
            }
            if (currentComment->replies == NULL) {
                currentComment->replies = reply;
                return true;
            } else {
                Reply* currentReply = currentComment->replies;
                while (currentReply->next != NULL) {
                    currentReply = currentReply->next;
                }
                currentReply->next = reply;
                reply->prev = currentReply;
                return true;
            }
        }
        currentComment = currentComment->prev;
        i++;
    }
    return false;
}

bool deleteReply(int n, int m) {
    if (platform->lastViewedPost == NULL) {
        return false;
    }
    Comment* currentComment = platform->lastViewedPost->comments;
    if (currentComment == NULL) return false;
    while(currentComment->next != NULL) currentComment = currentComment->next;
    int i = 1;
    while (currentComment != NULL) {
        if (i == n) {
            Reply* currentReply = currentComment->replies;
            if (currentReply == NULL) return false;
            while (currentReply->next != NULL) currentReply = currentReply->next;
            int j = 1;
            while (currentReply != NULL) {
                if (j == m) {
                    if (currentComment->replies == currentReply) {
                        currentComment->replies = currentReply->next;
                        if (currentComment->replies != NULL) {
                            currentComment->replies->prev = NULL;
                        }
                        free(currentReply);
                        return true;
                    }
                    currentReply->prev->next = currentReply->next;
                    if (currentReply->next != NULL) {
                        currentReply->next->prev = currentReply->prev;
                    }
                    free(currentReply);
                    return true;
                }
                currentReply = currentReply->prev;
                j++;
            }
        }
        currentComment = currentComment->prev;
        i++;
    }
    return false;
}