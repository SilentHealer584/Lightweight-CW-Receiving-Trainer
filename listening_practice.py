from random import choice
from time import sleep
from pyaudio import PyAudio, paFloat32
from numpy import pi, sin, arange, float32

stream = PyAudio().open(format=paFloat32, channels=1, rate=44100, output=True)

def Beep(d):
    wave = 0.3*sin(2 * pi * arange(int(44100 * d)) * 800 / 44100).astype(float32)
    stream.write(wave.tobytes())

WPM = 10

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

right = 0
wrong = 1
count = 1

while True:
    opt = input("\nWhat letters to include ? ( @ for whole alphabet )\n List : ")
    if opt=="@":
        pass
    else:
        if opt.isalpha():
            alphabet = list(set(opt))
            break
        else: 
            print("Only letters allowed.\n")

speed = 1.2/WPM
print(f"\nRunning at {WPM} WPM\n{round(speed, 2)} s/DOT ; {round(speed*3, 2)} s/DASH ; {round(speed*3, 2)} s/LETTER ; {round(speed*7, 2)} s/WORD")
sleep(3)

while True:
    letter = ""
    morse = ""
    print("\nGet ready...")

    for i in range(count):
        morse += "@"
        tletter = choice(alphabet)
        letter += tletter
        morse += MORSE_CODE_DICT[tletter]

    for i in list(morse):
        if i=="@":
            sleep(speed*2)
            continue
        if i==".":
            Beep(speed)
        else:
            Beep(speed*3)
        sleep(speed)

    answer = input("What character did you hear? ")
    
    if answer.upper()==letter:
        print("Correct!")
        right += 1
    else:
        print(f"Wrong, it was {letter}")
        wrong += 1
    if right/wrong>(3+3*count):
        count+=1
        right = 0
        wrong = 1
