FROM python:3.9.15-slim
Add . /build
WORKDIR /build
RUN pip install -r requirements.txt
RUN pip install opencv-python
CMD ["python", "app.py"]