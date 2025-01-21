## **HTTP Range-Request Video Streaming Demo**


Imagine watching your favorite movie or any random video on a website, you don’t have to wait for the entire file to be downloaded before you start watching it. Instead the video/movie begins playing almost immediately, with the rest of the video buffering seamlessly in the background.

One of the way to achieve this is by using the HTTP Range-Request to fetch the file in chunks from the given byte.


This demo showcases a simple video streaming implementation that utilizes HTTP Range-Requests to achieve seamless playback without requiring the entire video file to be downloaded beforehand.

### **Understanding HTTP Range-Requests**

HTTP Range-Requests enable clients to request specific byte ranges of a resource from a server. This functionality is particularly beneficial for various applications, including:   

- Media players with random access capabilities
- Data tools that only require a portion of a large file
- Download managers that support pausing and resuming downloads

### **Setting Up the Demo**

- *Clone the Repository*:
Begin by cloning this repository to your local machine. Ensure you have Python installed before proceeding.

- *Navigate to the Project Directory*:
Use the `cd video-streaming-demo` command to enter the project directory.

- *Install Dependencies*:
Install the required FastAPI and its associated packages by running the following command:
    `pip install -r requirements.txt`

- *Start the Backend Server*:
Execute the command `uvicorn main:app --reload` to launch the backend server.

- *View the Demo*:
Open the video.html file in your web browser to witness HTTP Range-Requests in action during video playback.
