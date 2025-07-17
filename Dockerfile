# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY etl_script.py .

# Create the output directory that the script needs
RUN mkdir -p /app/output

# Define the command to run your app
CMD ["python", "etl_script.py"]