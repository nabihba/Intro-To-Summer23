def create_youtube_video(title, description):
	youtube_video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return youtube_video

def likes(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"]+=1
	return youtube_video
def dislikes(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1
	return youtube_video
def add_comment(youtube_video, username, comment_text):
	if "comments" in youtube_video:
		youtube_video["comments"][username]= comment_text
	return youtube_video

youtube_video=create_youtube_video("shahar", "nice")
youtube_video=likes(youtube_video)
youtube_video=dislikes(youtube_video)
youtube_video=add_comment(youtube_video,"shahar","bomboclat")

print(youtube_video)