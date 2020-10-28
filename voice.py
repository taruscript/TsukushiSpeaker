import speech_recognition as sr
 
import numpy as np
import pyaudio
import wave
 


class voiceFunctionsClass:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 48000
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME ="recorded.wav"

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

    # 録音処理
    def voice_recode(self):
        print("＜＜＜録音中＞＞＞")

        frames = []
        calc = int(self.RATE / self.CHUNK * self.RECORD_SECONDS)
        for i in range(0, calc):
            data = self.stream.read(self.CHUNK)
            buf = np.frombuffer(data, dtype="int16")
            frames.append(b''.join(buf[::3]))
        
        print("＜＜＜録音終了＞＞＞")
        # 録音保存　処理
        self.voice_save(frames)
    

    # 録音保存　処理
    def voice_save(self, frames):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE / 3)
        wf.writeframes(b''.join(frames))
        wf.close()
    

    #　音声認識
    def voice_recognize(self):
        print("音声認識を開始します") 
        r = sr.Recognizer()
        with sr.AudioFile(self.WAVE_OUTPUT_FILENAME) as source:
            audio = r.record(source)
        result = r.recognize_google(audio, language='ja-JP')
        return result


if __name__ == "__main__":
    voice = voiceFunctionsClass()
    voice.voice_recode()
    print(f"音声認識結果: {voice.voice_recognize()}")
