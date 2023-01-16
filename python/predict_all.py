import os
import re
import csv
import librosa
from pydub import AudioSegment
import glob
import numpy as np
import pandas as pd
from pycaret.classification import *

# 表示する行数の指定
pd.set_option('display.max_rows', 500)

# ファイルの並び替え
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def predict_all():
    files = sorted(glob.glob('C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\cut_audio\\*.wav'), key=natural_keys)
    file_len = len(files)
    X_data = []  # 特徴行列
    y_data = []  # クラスラベルデータ
    predict_result = [] #予測結果

    for i in range (file_len):
        PATH = files[i]
        file_path = os.path.join(PATH)  # 音声ファイルへのパス
        y, sr = librosa.load(file_path)  # 音声ファイルを読み込む
        mfcc = librosa.feature.mfcc(y, sr)  # MFCC
        mfcc = np.average(mfcc, axis=1)  # 時間平均を取る
        mfcc = mfcc.flatten()
        mfcc = mfcc.tolist()
        mfcc = mfcc[1:13]  # 低次の係数を取り出す（12次まで取り出すことが多い）
        X_data.append(mfcc)
        y_data.append(2)

        X = pd.DataFrame(X_data, columns=[f'mfcc_{n}' for n in range(1, 13)])
        y = pd.DataFrame({'target': y_data})

        df = pd.concat([X, y], axis=1)
        # df.to_csv('mfcc_test.csv', index=False)  # csvで保存
        # df.head()

        load_model_pkl = load_model(model_name="finalmodel")

        predictions = predict_model(load_model_pkl, data = df)
        predict_result.append(predictions["prediction_label"])

    # 最終結果のみのリストを作成
    result = predict_result[-1:]

    with open('predict.txt', mode='w') as f:
        f.write('\n'.join(map(str,result)))

predict_all()