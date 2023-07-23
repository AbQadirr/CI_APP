import cv2
import streamlit as st
from PIL import Image
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

RTC_CONFIGURATION = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]},
    ]
}

RESIZE_WIDTH = 500
RESIZE_HEIGHT = 300

def process_camera_snapshot():
    video_capture = cv2.VideoCapture(0+cv2.CAP_DSHOW)
    
    if not video_capture.isOpened():
        st.warning("Error: Unable to access the camera.")
        return None
    
    ret, frame = video_capture.read()
    video_capture.release()  # Release the camera capture immediately after capturing the frame.

    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        image = image.resize((RESIZE_WIDTH, RESIZE_HEIGHT))
        snapshot_path = "snapshot.jpg"  # Save the resized snapshot image to a file
        image.save(snapshot_path)
        return snapshot_path
    else:
        st.warning("Error: Unable to capture a frame from the camera.")
        return None

def main():
    try:
        webrtc_ctx = webrtc_streamer(
            key="WYH",
            mode=WebRtcMode.SENDONLY,
            rtc_configuration=RTC_CONFIGURATION,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )

        if webrtc_ctx.video_receiver:
            # Display the camera stream preview
            st.image(webrtc_ctx.video_receiver.data, channels="RGB")
        
        # Capture snapshot
        snapshot_button = st.button("Take Snapshot")
        if snapshot_button:
            snapshot_path = process_camera_snapshot()
            if snapshot_path:
                st.success("Snapshot taken successfully.")
                st.image(snapshot_path, caption="Snapshot")
            else:
                st.error("Failed to capture snapshot.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
 # import streamlit as st
# import cv2
# import numpy as np
# from streamlit_webrtc import webrtc_streamer, VideoTransformerBase


# st.title("Webcam Snapshot")

# # Initialize the webcam
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     st.error("Error: Unable to access the webcam.")
# else:
#     # Capture a frame from the webcam
#     ret, frame = cap.read()

#     if ret:
#         # Display the captured frame using Streamlit
#         st.image(frame, channels="BGR", use_column_width=True)

#         # Check the type of the frame:
#         st.write("Frame type:", type(frame))

#         # Check the shape of the frame:
#         st.write("Frame shape:", frame.shape)
#     else:
#         st.error("Error: Unable to capture the frame from the webcam.")

#     # Release the webcam
#     cap.release()
# if __name__ == "__main__":
#     main()

