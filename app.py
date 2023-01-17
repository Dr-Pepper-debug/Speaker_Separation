from flask import Flask, render_template, request, send_file, send_from_directory
from werkzeug.utils import secure_filename

import ffmpeg
import os
import shutil
import python.command_line as command_line
import python.silence_remove as silence_remove
import python.audio_cut as audio_cut
import python.txt_shaping as txt_shapint
import python.audio_list as audio_list



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
        # # データの取り出し
        # file = request.files['file']
        # filename = "sample.mp4"

        # # ファイルの保存
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # # 動画ファイルを音声に変換
        # stream = ffmpeg.input("C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\uploads\\sample.mp4")
        # stream = ffmpeg.output(stream, "C:\\Users\\takumi\\デスクトップ\\大学\\3年\\後期\\実験2\\発表\\convert_audio\\meeting.wav")
        # ffmpeg.run(stream)

        # # 無音部分の削除
        # silence_remove.silence_remove()

        # # 文字起こし
        # command_line.command_cc()

        # # 時間ごとに分割
        # audio_cut.audio_cut()

        # # 分割音声の話者分類
        # command_line.command_speaker_classification()
        # # 議事録の作成
        # txt_shapint.make_contents()

       
        audio_result_dict = audio_list.make_audio_list()
        play_music(0)
        return render_template('form.html', speaker_dict=audio_result_dict)
        # return render_template('button.html', speaker_dict=audio_result_dict)
        # return '404'
    elif request.method == 'GET':
        return render_template('upload.html')

@app.route("/cut_audio/<int:id>.wav")
def play_music(id):
    return send_from_directory("cut_audio", str(id) + ".wav")

@app.route('/confirm', methods=['POST', 'GET'])
def confirm():
    text = request.form.getlist('item')
    print(text)
    # 動画、音声ファイルのディレクトリ削除
    shutil.rmtree("convert_audio/")
    shutil.rmtree("cut_audio/")
    shutil.rmtree("uploads/")
    
    # ディレクトリの作成
    os.mkdir("convert_audio/")
    os.mkdir("cut_audio/")
    os.mkdir("uploads/")

    # # 作成した議事録のダウンロード
    filepath = "content_result.txt"
    filename = os.path.basename(filepath)
    return send_file(filepath, as_attachment=True, download_name=filename, mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True)