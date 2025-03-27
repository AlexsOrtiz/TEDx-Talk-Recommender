# TEDx Talk Recommender

A machine learning-based web application that recommends TEDx talks based on user input. The application uses natural language processing techniques to find the most relevant talks from a curated dataset.

## Features

- Interactive web interface for inputting talk content
- Real-time recommendations using machine learning
- Detailed explanation of the recommendation system
- Responsive design for all devices
- Beautiful and intuitive user interface

## Technologies Used

- Python 3.x
- Flask (Web Framework)
- Pandas (Data Manipulation)
- scikit-learn (Machine Learning)
- NLTK (Natural Language Processing)
- HTML5 & CSS3
- JavaScript
- Gunicorn (Production Server)

## Installation

1. Clone the repository:
```bash
[git clone https://github.com/yourusername/tedx-talk-recommender.git](https://github.com/AlexsOrtiz/TEDx-Talk-Recommender.git)
cd tedx-talk-recommender
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Download the NLTK data:
```python
python -c "import nltk; nltk.download('stopwords')"
```

5. Run the application:

Development:
```bash
python app.py
```

Production:
```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

6. Open your browser and navigate to:
```
Development: http://localhost:5000
Production: http://localhost:8000
```

## How It Works

The application uses several machine learning techniques to provide accurate recommendations:

1. **Text Preprocessing**
   - Removes stopwords
   - Cleans punctuation
   - Converts text to lowercase

2. **TF-IDF Vectorization**
   - Converts text into numerical vectors
   - Weights words based on their importance

3. **Similarity Calculation**
   - Uses Cosine Similarity
   - Implements Pearson Correlation
   - Combines both metrics for better results

4. **Recommendation Generation**
   - Ranks talks based on similarity scores
   - Returns top 5 most relevant talks

## Project Structure

```
tedx-talk-recommender/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── tedx_dataset.csv      # Dataset of TEDx talks
├── static/
│   └── css/
│       └── style.css     # Stylesheets
└── templates/
    ├── index.html        # Main page
    └── explanation.html  # How it works page
```

## Usage

1. Enter your talk content or topic in the text area
2. Click "Get Recommendations"
3. View the recommended TEDx talks
4. Click "How It Works" to learn more about the recommendation system

## Deployment

For production deployment:

1. Set up your production environment:
```bash
pip install -r requirements.txt
```

2. Configure environment variables (if needed):
```bash
export FLASK_ENV=production
```

3. Run with Gunicorn:
```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

Additional Gunicorn options:
- `--workers 4`: Number of worker processes
- `--timeout 120`: Worker timeout in seconds
- `--access-logfile -`: Log to stdout
- `--error-logfile -`: Log errors to stderr

Example with all options:
```bash
gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 120 --access-logfile - --error-logfile - app:app
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- TEDx for providing the dataset
- scikit-learn and NLTK communities for their excellent libraries
- Flask team for the web framework 
