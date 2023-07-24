import streamlit as st
import cv2
from PIL import Image


RESIZE_WIDTH = 500
RESIZE_HEIGHT = 300



 


def process_uploaded_image(uploaded_file):
   if uploaded_file is not None:
       image = Image.open(uploaded_file)
       # Convert RGBA to RGB if image has an alpha channel
       if image.mode == 'RGBA':
           image = image.convert('RGB')

       image = image.resize((RESIZE_WIDTH, RESIZE_HEIGHT))
       image_path = "uploaded_image.jpg"  # Save the resized image to a file
       image.save(image_path)
       return image_path
   return None



def process_camera_snapshot():
  video_capture = cv2.CaptureFromCAM(0+cv2.CAP_V4L2)
   # while(video_capture.isOpened()):
  ret, frame = video_capture.read()
  if ret:
   frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   image = Image.fromarray(frame)
   image = image.resize((RESIZE_WIDTH, RESIZE_HEIGHT))
   snapshot_path = "snapshot.jpg"  # Save the resized snapshot image to a file
   image.save(snapshot_path)
   return snapshot_path
   
  return None


def main():
        
    # image = Image.open('https://github.com/AbQadirr/CI_APP/blob/main/MediTi.png')
    # st.image(
    #         image,
    #         width=400, # Manually Adjust the width of the image as per requirement
    #     )

    st.title("Image Comparing Streamlit App")

    col1, col2 = st.columns(2)

    image_path = None  # Initialize image_path variable
    snapshot_path = None  # Initialize snapshot_path variable

    
    # Add the logo image
    

    with col1:
        st.subheader("Upload an Image")
        uploaded_file = st.file_uploader("&nbsp;", type=["jpg", "jpeg", "png"], accept_multiple_files=False, help="", label_visibility='visible')
        if uploaded_file is not None:
            image_path = process_uploaded_image(uploaded_file)

    with col2:
        st.subheader("Camera Snapshot")
        snapshot_button = st.button("Take Snapshot")
        if snapshot_button:
            snapshot_path = process_camera_snapshot()

    # Show both images in a balanced manner
    if image_path is not None and snapshot_path is not None:
        st.subheader("Images")
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_path, caption="Uploaded Image")
        with col2:
            st.image(snapshot_path, caption="Snapshot")    



if __name__ == "__main__":
    main()
