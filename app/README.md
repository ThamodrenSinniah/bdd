# Running the Application

## Docker
### Prerequisites
- Docker
### Run the docker container
1. **Build and run the Docker container:**
   ```sh
   # In /app directory
   docker build -t myapp .
   docker run -p 8081:8081 myapp
   ```

2. **Access the application:**
   Open your browser and go to `http://localhost:8081`.

## Python
### Prerequisites
- Python 3.12

### Run the python webserver
1. **Ensure your virtual environment is activated with poetry**
   ```sh
   poetry shell
   ```
2. **Build and run the Docker container:**
   ```sh
   # In /app directory
   python -m http.server 8081
   ```
3. **Access the application:**
   Open your browser and go to `http://localhost:8081`.

