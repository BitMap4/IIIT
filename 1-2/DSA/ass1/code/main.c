#include "platform.h"

int main() {
    platform = createPlatform();
    if (platform == NULL) {
        return 1;
    }
    char command[20];
    while(1) {
        printf("\nCommands\n "
        "create_platform\n "
        "add_post <username> <caption>\n "
        "delete_post <n>\n "
        "view_post <n>\n "
        "current_post\n "
        "previous_post\n "
        "next_post\n "
        "add_comment <username> <content>\n "
        "delete_comment <n>\n "
        "view_comments\n "
        "add_reply <username> <content> <n>\n "
        "delete_reply <n> <m>\n "
        "exit\n\n");
        scanf("%s", command);

        if (strcmp(command, "create_platform") == 0) {
            platform = createPlatform();
            if (platform == NULL) {
                return 1;
            }
        } else if (strcmp(command, "add_post") == 0) {
            char username[100];
            char caption[100];
            scanf("%s %[^\n]s", username, caption);
            if (!addPost(username, caption)) {
                printf("Error: Could not add post\n");
            }
        } else if (strcmp(command, "delete_post") == 0) {
            int n;
            scanf("%d", &n);
            if (!deletePost(n)) {
                printf("Error: Could not delete post\n");
            }
        } else if (strcmp(command, "view_post") == 0) {
            int n;
            scanf("%d", &n);
            Post* post = viewPost(n);
            if (post == NULL) {
                printf("Error: Could not view post\n");
            } else {
                printf("%s %s\n", post->username, post->caption);
            }
        } else if (strcmp(command, "current_post") == 0) {
            Post* post = currPost();
            if (post == NULL) {
                printf("Error: Could not view post\n");
            } else {
                printf("%s %s\n", post->username, post->caption);
            }
        } else if (strcmp(command, "previous_post") == 0) {
            Post* post = previousPost();
            if (post == NULL) {
                printf("Error: Could not view post\n");
            } else {
                printf("%s %s\n", post->username, post->caption);
            }
        } else if (strcmp(command, "next_post") == 0) {
            Post* post = nextPost();
            if (post == NULL) {
                printf("Error: Could not view post\n");
            } else {
                printf("%s %s\n", post->username, post->caption);
            }
        } else if (strcmp(command, "add_comment") == 0) {
            char username[100];
            char content[100];
            scanf("%s %[^\n]s", username, content);
            if (!addComment(username, content)) {
                printf("Error: Could not add comment\n");
            }
        } else if (strcmp(command, "delete_comment") == 0) {
            int n;
            scanf("%d", &n);
            if (!deleteComment(n)) {
                printf("Error: Could not delete comment\n");
            }
        } else if (strcmp(command, "view_comments") == 0) {
            Comment* currentComment = viewComments();
            if (currentComment == NULL) {
                printf("No comments available\n");
            } else {
                while (currentComment != NULL) {
                    printf("%s %s\n", currentComment->username, currentComment->content);
                    Reply* currentReply = currentComment->replies;
                    while (currentReply != NULL) {
                        printf("%s %s\n", currentReply->username, currentReply->content);
                        currentReply = currentReply->next;
                    }
                    currentComment = currentComment->next;
                }
            }
        } else if (strcmp(command, "add_reply") == 0) {
            char username[100];
            char content[100];
            int n;
            scanf("%s %[^\n]s", username, content);
            n = content[strlen(content) - 1] - '0';
            content[strlen(content) - 2] = '\0';
            if (!addReply(username, content, n)) {
                printf("Error: Could not add reply\n");
            }
        } else if (strcmp(command, "delete_reply") == 0) {
            int n, m;
            scanf("%d %d", &n, &m);
            if (!deleteReply(n, m)) {
                printf("Error: Could not delete reply\n");
            }
        } else if (strcmp(command, "exit") == 0){
            break;
        }else {
            printf("Invalid command\n");
        }
    }
    
    while (platform->posts != NULL) {
        Post* post = platform->posts;
        platform->posts = platform->posts->next;
        while (post->comments != NULL) {
            Comment* comment = post->comments;
            post->comments = post->comments->next;
            while (comment->replies != NULL) {
                Reply* reply = comment->replies;
                comment->replies = comment->replies->next;
                free(reply);
            }
            free(comment);
        }
        free(post);
    }
    return 0;
}