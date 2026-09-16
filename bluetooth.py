import subprocess

SPEAKER_MAC = "28:FA:19:62:BA:DE"


def connect_speaker():
    result = subprocess.run(
        ["bluetoothctl", "connect", SPEAKER_MAC],
        capture_output=True,
        text=True
    )

    if "Connection successful" in result.stdout:
        print("Bluetooth speaker connected")
        return True

    print("Could not connect to Bluetooth speaker")
    print(result.stdout)
    return False