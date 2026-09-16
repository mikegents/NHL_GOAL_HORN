from pathlib import Path
import subprocess

def play_sound():

    soundFile = Path(__file__).parent / "goal-horn-short.mp3"

    subprocess.run(["ffplay",
                   "-autoexit",
                   str(soundFile)])



def main():
    play_sound()

if __name__ == "__main__":
    main()


