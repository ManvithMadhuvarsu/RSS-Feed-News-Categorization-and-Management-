# RSS-Feed-News-Categorization-and-Management
This project implements an automated news article classification system that fetches articles from various RSS feeds and categorizes them using Natural Language Processing (NLP). Articles are stored in a MySQL database and classified into categories like:

- **Terrorism / Protest / Political Unrest / Riot**
- **Positive / Uplifting**
- **Natural Disasters**
- **Others**

## Key Features

- Fetches articles from multiple RSS feeds
- NLP-based categorization of news articles
- Persistent storage in a MySQL database
- Detailed logging for monitoring and debugging
- Modular design for easy updates and testing

## Getting Started

### Prerequisites

- Python 3.x
- MySQL
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ManvithMadhuvarsu/RSS-Feed-News-Categorization-and-Management-.git

```

2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

3. Set up your MySQL database:

- Create a database named project.
- Run the SQL commands to create the news_articles table as defined in models.py.
- Update the database connection details in database.py if necessary.

4. Usage
Run the main application:

```bash
python main.py
```

The application will fetch articles from the specified RSS feeds, categorize them, and store them in the database.

## Contribution
Feel free to fork the repository, make changes, and submit pull requests. Any contributions are welcome!
