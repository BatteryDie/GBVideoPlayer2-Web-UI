from flask import Flask, request, render_template, jsonify, Response, Blueprint
import os
import subprocess
import datetime

# ##### Startup & Configuration Begin #####

cache_bp = Blueprint('cache', __name__, static_folder='cache', static_url_path='/cache')
app = Flask(__name__)
app.static_folder = 'static'
app.static_url_path = '/static'
app.register_blueprint(cache_bp)

# Check for installed programs:
REQUIRED_PROGRAMS = ['ffmpeg', 'make', 'rgbds']
missing_programs = []
for program in REQUIRED_PROGRAMS:
    if not any(os.access(os.path.join(path, program), os.X_OK) for path in os.environ["PATH"].split(os.pathsep)):
        missing_programs.append(program)
if missing_programs:
    print("Warning: The following required programs are missing and may affect functionality:")
    for program in missing_programs:
        print(f"- {program}")

# Check for folder:
CACHE_FOLDER = 'cache'
app.config['CACHE_FOLDER'] = CACHE_FOLDER
if not os.path.exists(CACHE_FOLDER):
    os.makedirs(CACHE_FOLDER)
    print('cache folder has created')

# ##### Startup & Configuration Complete #####

@app.route('/')
def index():
    return render_template('index.html')

def stream_command_output(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True, shell=True)
    for line in iter(process.stdout.readline, ''):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_line = f"[{current_time}] {line.strip()}\n"
        print(output_line, end='', flush=True)  # Print output to console
        yield output_line  # Yield output for web log
    process.stdout.close()
    return_code = process.wait()
    if return_code:
        error_message = f'Command execution failed with return code {return_code}.\n'
        print(error_message, end='', flush=True)  # Print error message to console
        yield error_message  # Yield error message for web log

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'}), 400

    file_path = os.path.join(app.config['CACHE_FOLDER'], file.filename)
    file.save(file_path)

    option_quality = request.form.get('optionQuality')
    command = f"make SOURCE={file_path} quality={option_quality}"

    return Response(stream_command_output(command), content_type='text/plain') # Print output to web UI

if __name__ == '__main__':
    print('Hello GBVideoPlayer2 Web UI!')
    app.run(debug=False)