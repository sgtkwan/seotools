# Flask Keyword Classifier

A Flask web application that uses Google's Gemini AI to classify keywords from uploaded Excel/CSV files.

## Features

- Upload CSV, XLS, or XLSX files
- AI-powered keyword classification using Google Gemini
- Batch processing with configurable batch sizes
- Excel output with formatted results
- Secure file handling and cleanup

## Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd flask_app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit .env with your actual values
   # You'll need a Google Gemini API key
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

   The app will be available at `http://localhost:5000`

## Environment Variables

Create a `.env` file with the following variables:

- `GOOGLE_API_KEY`: Your Google Gemini API key (required)
- `SECRET_KEY`: Flask secret key for sessions (change in production)
- `FLASK_ENV`: Set to `development` for local dev, `production` for deployment
- `MAX_CONTENT_LENGTH`: Maximum file upload size in bytes (default: 16MB)
- `DEFAULT_BATCH_SIZE`: Number of keywords to process per batch (default: 200)

## Deployment to Render

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Create a new account or sign in
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

3. **Configure the service**
   - **Name**: `flask-keyword-classifier` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

4. **Set environment variables in Render**
   - `GOOGLE_API_KEY`: Your Google Gemini API key
   - `SECRET_KEY`: A strong, random secret key
   - `FLASK_ENV`: `production`
   - `FLASK_APP`: `app.py`

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - Your app will be available at the provided URL

## API Usage

### Upload File
- **POST** `/`
- Upload a CSV, XLS, or XLSX file with keywords and brand data

### Process File
- **POST** `/process/<filename>`
- Process the uploaded file with AI classification
- Optional form parameter: `batch_size` (default: 200)

### Download Results
- **GET** `/download/<filename>`
- Download the processed Excel file with classification results

## File Format Requirements

Your input file should have:
- **Column 1**: Keywords to classify
- **Column 2**: Brand names
- **Additional columns**: Categories with predefined tags

Example:
```
Keyword,Brand,Category1,Category2
"best running shoes",Nike,["sports","casual"],["athletic","comfortable"]
"coffee maker",Starbucks,["beverages","home"],["hot","caffeinated"]
```

## Security Features

- Secure file uploads with size limits
- File type validation
- Automatic file cleanup after download
- Security headers on responses
- Environment variable configuration for sensitive data

## Dependencies

- Flask 3.0.0
- pandas 2.1.4
- google-generativeai 0.3.2
- openpyxl 3.1.2
- gunicorn 21.2.0 (for production)
- python-dotenv 1.0.0

## License

This project is licensed under the MIT License.

## Support

For issues or questions, please open an issue in the GitHub repository.
