# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app 
ADD . /app



# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]