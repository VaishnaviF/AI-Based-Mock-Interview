import speech_recognition as sr
from time import sleep
import pyaudio as pyaudio
import wave
from os import path

recording = sr.Recognizer()

def record_to_file(filename="C:\\Users\\SIDDHI\\Downloads\\Django\\Django\\Examination\\text.wav",FORMAT = pyaudio.paInt16, CHANNELS = 1, RATE = 8000,
                    CHUNK = 1024, RECORD_SECONDS=8):
    audio = pyaudio.PyAudio()
    #print("[INFO] Audio will record for "+str(RECORD_SECONDS)+" seconds")
    # start Recording
    print("[INFO] Recording started")
    #print("Please Say something:")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    #print("[INFO] audio taken")

    waveFile = wave.open(filename, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    #print("[INFO] Audio written to "+filename)


def convert_speech2text(filename="C:\\Users\\SIDDHI\\Downloads\\Django\\Django\\Examination\\text.wav", file="mesg.txt"):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), filename)
    print(AUDIO_FILE)
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    #print("[INFO] Processing your file...")
    try:
        ret = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said \n" + ret)
        file = open(file,"w")
        file.write(ret)
        file.close()
        return 0
    except sr.UnknownValueError:
        print("[Error]  Speech Recognition Error")
        print("Google Speech Recognition could not understand audio")
        return 1
    except sr.RequestError as e:
        print("[Error]  Request Error")
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return 1
        
def main(res='res.txt'):
	record_to_file()

	filename="C:\\Users\\SIDDHI\\Downloads\\Django\\Django\\Examination\\text.wav"
	file=res
	convert_speech2text(filename, file)
if __name__ == '__main__':
    main()
