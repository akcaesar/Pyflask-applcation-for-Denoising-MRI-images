import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from skimage import io
from skimage.restoration import denoise_tv_chambolle, denoise_nl_means, denoise_wavelet

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/denoise', methods=['POST'])
def denoise():
    # Retrieve the uploaded file and denoising method from the form submission
    file = request.files['image']
    method = request.form['method']

    # Check if the file is allowed
    if file and allowed_file(file.filename):
        # Save the uploaded file to the server
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Load the uploaded image and apply the chosen denoising method
        img_orig = io.imread(filepath, as_gray=True)
        if method == 'tv_chambolle':
            img_denoised = denoise_tv_chambolle(img_orig, weight=0.1)
        elif method == 'nl_means':
            img_denoised = denoise_nl_means(img_orig, patch_size=5, patch_distance=3, h=0.1)
        elif method == 'wavelet':
            img_denoised = denoise_wavelet(img_orig, sigma=0.1, rescale_sigma=True)
        
        # Save the denoised image to the server
        denoised_filename = f'denoised_{filename}'
        denoised_filepath = os.path.join(app.config['UPLOAD_FOLDER'], denoised_filename)
        io.imsave(denoised_filepath, img_denoised)

        # Pass the filenames of the original and denoised images to the results template
        return render_template('results.html', 
                               img_orig_filename=filename, 
                               img_denoised_filename=denoised_filename)
    else:
        return 'Invalid file type or file exceeds 16MB limit.'

if __name__ == '__main__':
    app.run(debug=True)
