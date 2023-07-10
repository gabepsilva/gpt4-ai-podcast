
from core.person import Person


class SpecialGuest(Person):
    def __init__(self):
        super().__init__()

        self.persona = "Guest"
        self.duration = 10
        self.samplerate = 44100

    def record_audio(self):

        import sounddevice as sd
        from scipy.io.wavfile import write
        import wavio as wv

        # Sampling frequency
        freq = 44100

        # Recording duration
        duration = 5

        # Start recorder with the given values
        # of duration and sample frequency
        recording = sd.rec(int(duration * freq),
                           samplerate=freq, channels=2)

        # Record audio for the given number of seconds
        sd.wait()

        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write("recording0.wav", freq, recording)

        # Convert the NumPy array to audio file
        wv.write("recording2.wav", recording, freq, sampwidth=2)
        self.convert_wav_to_mp3("recording0.wav", "recording0.mp3")
        self.convert_wav_to_mp3("recording2.wav", "recording2.mp3")

    def convert_wav_to_mp3(self, wav_file, mp3_file):

        from pydub import AudioSegment

        audio = AudioSegment.from_wav(wav_file)
        audio.export(mp3_file, format="mp3")
