from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask import send_from_directory

import ffmpeg
import os
# import subprocess
import python.command_line as command_line

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
        # アップロード後のページに転送
        # return redirect(url_for('uploaded_file', filename=filename))
        # 動画ファイルを音声に変換
        stream = ffmpeg.input("C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\uploads\\sample.mp4")
        stream = ffmpeg.output(stream, "C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\convert_audio\\minutes.wav")

        ffmpeg.run(stream)
        command_line.command_execution()
        return '議事録作成中'
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)