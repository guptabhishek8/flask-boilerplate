# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for virtual environment
ENV VIRTUAL_ENV=/venvfusion
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create a directory for your application and set the working directory
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY . .
RUN python -m venv $VIRTUAL_ENV && \
    pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the port your uWSGI application will run on
EXPOSE 8000

# Specify the command to run your uWSGI application
CMD ["uwsgi", "--socket", "0.0.0.0:8000", "--protocol", "http", "-w", "app:app", "--enable-threads"]