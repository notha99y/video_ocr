# About
I am a simple script that can read in videos and perform OCR with cv2 and pytesseract.

# Setup
1. Download Docker [here](https://www.docker.com/get-started)
1. Create docker image
```bash
docker build -t <image name> .
```
1. You can also docker pull the image
```bash
docker pull notha99y/pytesseract
```

# To run
```bash
docker run -it --volume <path to your script>:/workspace <image name>
```
This would allow you to "tty" inside the container.
```bash
cd workspace
python main.py -f <path to video file>
```