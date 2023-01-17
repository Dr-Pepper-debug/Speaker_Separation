import whisper

model = whisper.load_model("medium")

path ="C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\convert_audio\\meeting_silence_removed.wav"

result = model.transcribe(path, verbose=True, language='ja')