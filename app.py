from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask import send_from_directory

import ffmpeg
import os
# import subprocess
import python.command_line as command_line
import python.silence_remove as silence_remove
import python.audio_cut as audio_cut
import python.txt_shaping as txt_shapint
import python.predict_all as predict_all




UPLOAD_FOLDER = './uploads'
AUDIO_FOLDER = './convert_audio'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # データの取り出し
        file = request.files['file']
        filename = "sample.mp4"

        # ファイルの保存
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # 動画ファイルを音声に変換
        stream = ffmpeg.input("C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\uploads\\sample.mp4")
        stream = ffmpeg.output(stream, "C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\convert_audio\\minutes.wav")
        ffmpeg.run(stream)

        # 無音部分の削除
        silence_remove.silence_remove()
        # 文字起こし
        command_line.command_cc()
        # 時間ごとに分割
        audio_cut.audio_cut()
        # 分割音声の話者分類
        predict_all.predict_all()
        # 議事録の作成
        txt_shapint.make_contents()
        return render_template('progress.html')
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)