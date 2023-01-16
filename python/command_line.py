import subprocess

def command_cc():
    with open("speak.txt", "w") as f:
        subprocess.run(["python", "C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\python\\cc_test.py"], stdout=f)