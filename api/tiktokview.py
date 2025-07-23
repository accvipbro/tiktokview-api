from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/tiktokview')
def tiktokview():
    video_url = request.args.get('video')
    if not video_url:
        return jsonify({'error': 'Thiếu tham số video'}), 400

    return jsonify({
        'status': 'ok',
        'video': video_url,
        'sent_success': 1,
        'sent_fail': 0
    })
