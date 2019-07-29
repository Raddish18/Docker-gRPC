# Use an official Python runtime as a parent image
FROM python:3-onbuild

COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 50051 available to the world outside this container
EXPOSE 8080:5000

# Run app.py when the container launches
CMD ["python", "email.py"]
