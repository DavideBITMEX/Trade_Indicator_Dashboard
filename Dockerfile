# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY requirements.txt /app/
COPY data_pipeline.py /app/
COPY highcharter_dashboard.py /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the pipeline and then the Dash app
CMD ["sh", "-c", "python data_pipeline.py && python highcharter_dashboard.py"]


