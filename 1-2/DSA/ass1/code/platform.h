#ifndef PLATFORM_H
#define PLATFORM_H

#include "post.h"
#include <stdbool.h>
typedef struct {
    Post* posts;
    Post* lastViewedPost;
} Platform;

extern Platform* platform;

// Create an instance of the platform data type
Platform* createPlatform(); 

// Create a post of the given parameters (by calling the previous implemented function) and adds it to the existing list of posts, returning whether the process is successful or not
bool addPost(char* username, char* caption); 

// Deletes the n-th recent post, returning,whether the deletion is successful or not. Also, it should clear the comments and replies as well to the post
bool deletePost(int n); 

// Returns the n-th recent post, if existing. If it does not exist, a NULL pointer must be returned
Post* viewPost(int n); 

// Returns the lastViewedPost. As described earlier, this post will be the most recent post, if no other post has been viewed. If no post has been done, a NULL pointer must be returned
Post* currPost(); 

// Returns post which was posted just before posting the lastViewedPost. If the lastViewedPost is the first post to be added, then return it. In case of any error, a NULL pointer must be returned. Doing this operation, will change the lastViewedPost, by it’s definition
Post* nextPost(); 

// Returns post which was posted just after posting the lastViewedPost. If the lastViewedPost is the last post to be added, then return it. In case of any error, a NULL pointer must be returned. Doing this operation, will change the lastViewedPost, by it’s definition
Post* previousPost(); 

// Adds a comment to the lastViewedPost, returning whether the addition is successful or not
bool addComment(char* username, char* content); 

// Deletes the n-th recent comment of the lastViewedPost, returning whether the deletion is successful or not. Also, it should clear the replies as well to the comment
bool deleteComment(int n); 

// Returns a list of all comments to the lastViewedPost. The order of the comments in the list must be in order of the time of commenting, the latest being at last. The order of replies should be the same as well
Comment* viewComments(); 

// Adds a reply to the n-th recent comment of the lastViewedPost, returning whether the addition is successful or not
bool addReply(char* username, char* content, int n); 

// Deletes the m-th recent reply to the n-th recent comment of the lastViewedPost, returning whether the deletion is successful or notbool deleteReply(int n, int m); 
bool deleteReply(int n, int m);

#endif // PLATFORM_H