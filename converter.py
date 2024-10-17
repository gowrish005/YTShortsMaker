import subprocess
import os

def convert_video(input_video_path, output_dir):
    print(input_video_path)
    # """
    # Convert a video file from one format to another using FFmpeg and NVIDIA GPU acceleration.

    # Args:
    #     input_video_path (str): Path to the input video file.
    #     output_dir (str): Directory where the output video file will be saved.

    # Returns:
    #     str: Path to the output video file.
    # """
    # # Get the input file name and extension
    # input_filename, input_file_extension = os.path.splitext(os.path.basename(input_video_path))

    # # Construct the output file name with the same name as the input file but with .mp4 extension
    # output_filename = f"{input_filename}.mp4"

    # # Check if the output file exists in the output directory
    # output_video_path = os.path.join(output_dir, output_filename)
    # if os.path.exists(output_video_path):
    #     # If it exists, append a number to the filename
    #     counter = 1
    #     while os.path.exists(os.path.join(output_dir, f"{input_filename}_{counter}.mp4")):
    #         counter += 1
    #     output_video_path = os.path.join(output_dir, f"{input_filename}_{counter}.mp4")

    # # Construct the FFmpeg command
    # cmd = f"D:\\Softwares\\Installed\\ffmpeg-7.1-essentials_build\\bin\\ffmpeg.exe -i {input_video_path} -c:v h264_nvenc -crf 18 {output_video_path}"

    # # Run the FFmpeg command using subprocess
    # try:
    #     subprocess.run(cmd, shell=True, check=True)
    #     print(f"Video converted successfully: {input_video_path} -> {output_video_path}")
    #     return output_video_path
    # except subprocess.CalledProcessError as e:
    #     print(f"Error converting video: {e}")
    #     return None

# Example usage:
input_video_path = "C:\\Users\\Gowrish\\Desktop\\My\\PyFiles\\YTMaker\\input.mkv"
output_dir = "C:\\Users\\Gowrish\\Desktop\\My\\PyFiles\\YTMaker"
output_file_path = convert_video(input_video_path, output_dir)
print(f"Output file path: {output_file_path}")