from pydub import AudioSegment

def audio_cut():
    # wavファイルの読み込み
    sound = AudioSegment.from_file("C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\convert_audio\\take_silence_removed.wav", format="wav")

    # 時間を格納するリスト
    start_min = []
    start_sec = []
    start_msec = []
    stop_min = []
    stop_sec = []
    stop_msec = []
    text = []
    # 文字起こししたファイルを読み込み、時間のみ抽出
    with open("speak.txt") as f:
        for s_line in f:
            start_min.append(s_line[1:3])
            start_sec.append(s_line[4:6])
            start_msec.append(s_line[7:10])
            stop_min.append(s_line[15:17])
            stop_sec.append(s_line[18:20])
            stop_msec.append(s_line[21:24])
            text.append(s_line[25:-1])

    s_len = len(start_min)

    j = 0

    # 抽出した時間を元に音声ファイルを分割
    for i in range(s_len):
        start_min_conv = int(start_min[i]) * 60000
        start_sec_conv = int(start_sec[i]) * 1000
        start_msec_conv = int(start_msec[i])
        start_time = start_min_conv + start_sec_conv + start_msec_conv

        stop_min_conv = int(stop_min[i]) * 60000
        stop_sec_conv = int(stop_sec[i]) * 1000
        stop_msec_conv = int(stop_msec[i])
        stop_time = stop_min_conv + stop_sec_conv + stop_msec_conv

        output_sound = sound[start_time:stop_time]
        path = "C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\cut_audio\\" + str(j) + ".wav"
        j += 1
        output_sound.export(path, format="wav")