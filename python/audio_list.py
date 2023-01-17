from collections import Counter

def make_audio_list():
    speaker_list = []
    line_number = []
    audio_list = []
    audio_truck = []

    with open('predict.txt', mode='r') as f:
        lines = f.readlines()

    # listから空白、\nを削除し、話者番号、行番号を分離して取り出し
    for i in range(len(lines) - 1):
        speaker_list.append(lines[i].replace(' ', '').replace('\n', '')[-2:])
        line_number.append(lines[i].replace(' ', '').replace('\n', '')[:-2])

    # 話者分類された番号を取り出す
    counter = list(Counter(speaker_list))

    # それぞれの音声の番号を取り出す
    for i in range(len(counter)):
        for j in range(len(line_number)):
            if counter[i] == speaker_list[j]:
                audio_list.append(j)
                break
    
    for i in range(len(counter)):
        audio_truck.append("/cut_audio/" + str(audio_list[i]) + ".wav")
    
    audio_dict = {}
    for i in range(len(counter)):
        audio_dict[counter[i]] = audio_truck[i]
    
    return audio_dict