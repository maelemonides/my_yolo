---
title: My Yolo
emoji: 🌍
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.32.2
app_file: app.py
pinned: false
---

# Deep Learning Model Deployment with YOLOv8 and Streamlit

## Overview:
This project aims to deploy a deep learning model for object detection using YOLOv8 architecture and Streamlit for web application development. Due to constraints in model size and compatibility, a YOLOv8 model from `hustvl` is utilized instead of a custom-trained model. The deployment process involves fine-tuning the YOLOv8 model on Colab and building a Streamlit application using Cloudflare on Colab.

## Problem Statement:
The objective is to create a user-friendly web application for real-time object detection. This application can be beneficial for various scenarios, including security surveillance, retail analytics, and traffic monitoring. By leveraging YOLOv8's efficiency and Streamlit's interactivity, users can easily upload images and receive instant object detection results.

## Data:
The dataset used for training and testing the YOLOv8 model consists of images containing various objects across different categories. However, due to constraints in model size, a pre-trained YOLOv8 model from `hustvl` is employed.

## Methodology:

### Model Building and Fine-tuning:
- YOLOv8 architecture is utilized for object detection.
- The model is fine-tuned on a dataset containing labeled images to adapt it to specific object detection tasks.

### Deployment with Streamlit:
- Streamlit is chosen as the framework for building the web application due to its simplicity and ease of use.
- Cloudflare is used for hosting the Streamlit application on Colab to make it accessible via the web.

### Limitations and Workarounds:
- **Model Size Limitation:** The custom-trained YOLOv8 model exceeded the size limit imposed by Hugging Face Spaces, which prohibits direct upload of models larger than 10MB.
- **Extension Incompatibility:** Issues were encountered with model extensions and compatibility with Hugging Face's existing APIs, making it challenging to integrate the custom model into the Hugging Face ecosystem.
- **Alternative Solution:** To circumvent these compatibility issues, a pre-trained YOLOv8 model from `hustvl` was employed, allowing for the development of a Streamlit application without constraints posed by model size or compatibility with hosting platforms.

## Deployment Details:
- The Streamlit application is deployed on Colab using Cloudflare to enable web accessibility.
- Docker and docker-compose are employed for packaging the application, ensuring easy setup and deployment.
- The repository includes documentation, tests, and a README summarizing the project.

## Architecture:

- **Components/Services:** 
  - YOLOv8 Model (Fine-tuned)
  - Streamlit Web Application
  - Cloudflare Hosting
  - Docker Container

- **Interactions:**
  - Streamlit interacts with the YOLOv8 model for object detection.
  - Cloudflare hosts the Streamlit application, making it accessible via the web.
  - Docker containerizes the application for easy deployment.

- **Exposed Ports:**
  - Streamlit Web Application Port: 8501
  - Cloudflare Exposed Endpoint: `https://example.com/object-detection`

## Conclusion:
Despite challenges related to model size and compatibility, this project successfully deploys a YOLOv8-based object detection system using Streamlit. By leveraging cloud-based solutions and containerization, the application achieves scalability and ease of deployment. Future improvements may include exploring alternative deployment platforms and addressing model size constraints for enhanced flexibility.

