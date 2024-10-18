import os
from moviepy.editor import VideoFileClip
# from converter import convert_video  # Assuming this is your custom video conversion function


input_video_path = "C:\\Users\\Gowrish\\Desktop\\My\\PyFiles\\YTMaker\\input.mp4"
output_dir = "C:\\Users\\Gowrish\\Desktop\\My\\PyFiles\\YTMaker"

# Check if the input file is an MP4 file
input_filename, input_file_extension = os.path.splitext(os.path.basename(input_video_path))



# if input_file_extension.lower() == '.mkv':
#     # Convert the file to MP4 using the convert_video function
#     output_video_path = convert_video(input_video_path, output_dir)

#     # Debugging: Check if output_video_path is None
#     print(f"Output file path: {output_video_path}")

#     if output_video_path is None:
#         raise ValueError("The convert_video function did not return a valid output path.")
    
#     # Use the converted video as the input for further processing
#     input_video_path = output_video_path

# Ensure input_video_path is valid before proceeding
if not os.path.exists(input_video_path):
    raise FileNotFoundError(f"The video file at {input_video_path} was not found.")

def convert_landscape_to_portrait(input_video_path, output_video_path):
    # Load the video
    video = VideoFileClip(input_video_path)

    # Get the dimensions of the video
    width, height = video.w, video.h

    # Check if the video is already in portrait mode
    if height > width:
        print("The video is already in portrait mode.")
        return

    # Calculate the new dimensions for the portrait video (9:16 aspect ratio)
    new_height = height
    new_width = int(new_height * 9 / 16)  # Keep 9:16 aspect ratio for portrait

    # Crop the central part of the video to avoid distortion
    portrait_video = video.crop(x_center=width / 2, width=new_width, height=new_height)

    # Write the portrait video to a new file using GPU acceleration with h264_nvenc codec
    portrait_video.write_videofile(output_video_path, codec='h264_nvenc', preset='fast')

# Example usage:
output_video_path = os.path.join(output_dir, "output.mp4")
convert_landscape_to_portrait(input_video_path, output_video_path)
