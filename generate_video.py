import os
from moviepy import ImageClip, AudioFileClip


VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30


def generate_video(image_file="background.jpg", audio_file="voice.mp3",
                   output_file="reel.mp4"):

    if not os.path.exists(image_file):
        raise FileNotFoundError(f"{image_file} not found.")

    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"{audio_file} not found.")

    audio = AudioFileClip(audio_file)

    video = (
        ImageClip(image_file)
        .resized(height=VIDEO_HEIGHT)
        .cropped(
            x_center=VIDEO_WIDTH / 2,
            y_center=VIDEO_HEIGHT / 2,
            width=VIDEO_WIDTH,
            height=VIDEO_HEIGHT
        )
        .with_duration(audio.duration)
        .with_audio(audio)
    )

    video.write_videofile(
        output_file,
        fps=FPS,
        codec="libx264",
        audio_codec="aac"
    )

    video.close()
    audio.close()

    print(f"Video generated: {output_file}")


if __name__ == "__main__":
    generate_video()
