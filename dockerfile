# Use the official Python image as the base image
FROM amd64/python:latest

# Set the workinßg directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install
RUN playwright install-deps

# Copy the entire project directory
COPY . .

# Expose the port your API will run on (replace 8000 with your desired port)
EXPOSE 5555
ENV PORT=5555
# Set the command to run your Python API
CMD ["python", "fusionAPI.py"]
