from pydub import AudioSegment
from pydub.silence import split_on_silence

def silence_remove():
    # 音声ファイル読み込み
    SOURCE_FILE =  'C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\convert_audio\\meeting.wav'

    sound = AudioSegment.from_file(SOURCE_FILE)

    # org_ms = len(sound)
    # print('original: {:.2f} [min]'.format(org_ms/60/1000))

    # 無音部分の削除
    chunks = split_on_silence(sound, min_silence_len=100, silence_thresh=-55, keep_silence=100)
    cutted_sound = sum(chunks)
    # cutted_ms = len(cutted_sound)
    # print('silence_thresh = {}: {:.2f} [min]'.format(-55, cutted_ms/60/1000))
    # ファイルの書き出し
    cutted_sound.export('C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\convert_audio\\meeting_silence_removed.wav', format='wav')