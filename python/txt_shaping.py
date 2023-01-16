def make_contents():
    speaker_list = []
    content_list = []
    result_list = []

    with open('predict.txt', mode='r') as f:
        lines = f.readlines()

    # listから空白、\nを削除し、話者番号のみ取り出し
    for i in range(len(lines) - 1):
        speaker_list.append(lines[i].replace(' ', '').replace('\n', '')[-2:])

    # 会話の内容を取得
    with open('speak.txt') as f:
        for s_line in f:
            # 時間以外を格納
            content_list.append(s_line[25:-1])
    # 話者番号と内容を合体
    for i in range(len(speaker_list)):
        result_list.append(str(speaker_list[i]) + str(content_list[i]) + '\n')

    # 結果をファイルに書き出し
    with open('content_result.txt', 'w', encoding='utf-8', newline='\n') as rf:
        for i in range(len(speaker_list)):
            rf.write(result_list[i])