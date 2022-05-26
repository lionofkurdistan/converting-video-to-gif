from moviepy.editor import*


#instert video
clip = (VideoFileClip("3.mp4")
        .subclip(0.3))

#insert gif flie path
clip.write_gif("mygif.gif")