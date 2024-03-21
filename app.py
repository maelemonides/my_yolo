import streamlit as st
from PIL import Image, ImageDraw
import torch
from transformers import YolosImageProcessor, YolosForObjectDetection

# Load YOLOS model
model = YolosForObjectDetection.from_pretrained('hustvl/yolos-tiny')
image_processor = YolosImageProcessor.from_pretrained("hustvl/yolos-tiny")

# Streamlit setup
st.title("Object Detection using YOLOS")

# File uploader
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform object detection on button click
    if st.button("Detect Objects"):
        # Preprocess image
        inputs = image_processor(images=image, return_tensors="pt")
        
        # Run inference
        outputs = model(**inputs)

        # Post-process detection results
        target_sizes = torch.tensor([image.size[::-1]])
        results = image_processor.post_process_object_detection(outputs, threshold=0.9, target_sizes=target_sizes)[0]
        
        # Draw bounding boxes on the image
        annotated_image = image.copy()
        draw = ImageDraw.Draw(annotated_image)
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            xmin, ymin, xmax, ymax = box
            draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)
            draw.text((xmin, ymin), f"{model.config.id2label[label.item()]} {score.item():.2f}", fill="red")
        
        # Display annotated image
        st.image(annotated_image, caption="Annotated Image", use_column_width=True)
