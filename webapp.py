from flask import Flask, Response, render_template, request
import os
import time

app = Flask(__name__)

def generate_board_svg():
    with open('board.svg', 'r') as f:
        
        return f.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/board')
def board():
    return Response(generate_board_svg(), mimetype='image/svg+xml')

def watch_board_file():
    last_modified = os.path.getmtime('board.svg')
    while True:
        time.sleep(1)
        modified = os.path.getmtime('board.svg')
        if modified != last_modified:
            last_modified = modified
            yield 'update'

@app.route('/stream/board')
def stream_board():
    return Response(watch_board_file(), content_type='text/event-stream')

@app.route('/update_board')
def update_board():
    modified = os.path.getmtime('board.svg')
    return str(modified)

if __name__ == '__main__':
    app.run(debug=True)
