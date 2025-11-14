**🌱 Plantation Monitoring using SAM Segmentation and Resnet50**
This project implements a practical pipeline for plantation monitoring using the Segment Anything Model (SAM) for instance/semantic segmentation and a ResNet50 classifier for identifying segmented regions. The SAM model was uploaded and fine-tuned on domain-specific field imagery to produce accurate crop and field-category segments. A ResNet50 model was uploaded and subsequently fine-tuned on labeled segments to classify crop types and distinguish fallow/other land categories. A lightweight local web interface was developed to enable interactive upload of field images and visualization of segmentation and classification outputs. Results (segmentation masks, class labels, and summary tables) are presented with figures and numeric metrics in the Results section.

Monitoring plantations and crop cover at field level is crucial for agricultural planning, early detection of crop stress, and estimation of cultivated area. Recent progress in foundation segmentation models (e.g., SAM) and convolutional neural network classifiers (e.g., ResNet architectures) enables accurate, automated extraction of crop regions and their subsequent classification from field imagery. This project integrates these components into an end-to-end pipeline suitable for small-scale deployment and interactive use.

Technologies Used
1.      Segment anything model (SAM): Foundation segmentation model used for producing instance/semantic masks from raw field images.

2.      Resnet50: Convolutional neural network architecture used for classifying segmented regions into crop types and field categories.

3.      Python ecosystem: Model fine-tuning and inference performed using Python scripts/notebooks.

4.      Local webpage: simple local web interface to upload field images, run segmentation + classification, and visualize results.

Steps:
Use maskgen.ipynb to generate image masks, then use segment_transfer.ipynb to finetune the SAM model using this dataset: https://drive.google.com/drive/folders/1qCAFrPwb7R8tOdh_9BYxe2OmOtDJNOKp

Use resnet.ipynb and this dataset: https://www.kaggle.com/datasets/mdwaquarazam/agricultural-crops-image-classification, to finetune the Resnet50 model

Then change any paths in the code appropriately and run using streamlit run app.py

Access the application: The app will automatically open in your default browser Or manually navigate to: http://localhost:8501

📱 Features
Responsive Design: Works seamlessly on desktop, tablet, and mobile devices

Modern UI: Beautiful animations and hover effects

AI-Powered: Uses Meta's SAM and ResNet50 for image segmentation and classification

User Authentication: Secure login and signup system

Real-time Processing: Upload and analyze plantation images instantly

Note: The first time you run the application, SAM model loading may take 20-60 seconds. Subsequent runs will be faster as the model is cached in session state.ote: The first time you run the application, SAM model loading may take 20-60 seconds. Subsequent runs will be faster as the model is cached in session state.
