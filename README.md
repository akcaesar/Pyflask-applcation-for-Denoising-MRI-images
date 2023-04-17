# Pyflask-application-for-Denoising-MRI-images
A simple pyflask application that accepts input MRI images and denoises it using TV loss, wavelet based and NLM methods

**Project Title:** MRI Image Denoiser

**Project Description:** This project is a web application that allows users to upload MRI images and denoise them using one of three denoising methods: Total Variation (TV) Chambolle, Non-local Means, or Bayesian Wavelet Denoising. The web application is built using Python and Flask, and it uses the scikit-image library for image processing.

**Project Workflow:**

User uploads an MRI image and selects a denoising method.
The Flask server receives the image and denoising method from the user.
The server saves the uploaded image to a temporary folder and applies the selected denoising method to the image.
The server saves the denoised image to a permanent folder and renders a results page to the user.
The user can view the original and denoised images on the results page, and they can choose to go back to the home page to upload another image.
**Key Features:**

User-friendly interface for uploading and denoising MRI images
Three different denoising methods to choose from
Automatic saving of uploaded and denoised images to a permanent folder
Option to view the original and denoised images side by side on the results page
**Potential Improvements:**

Allow users to choose the denoising parameters for each method
Implement additional denoising methods or image processing techniques
Add functionality for downloading the denoised image from the results page
Improve the user interface with more responsive design and better styling.
