# Stock Market Data Pipeline

A Python-based ETL pipeline that fetches daily stock market data from Alpha Vantage API and stores it in CSV format for analysis.

## 🎯 Project Overview

This pipeline extracts historical and current stock prices for major tech companies (AAPL, GOOGL, TSLA, NVDA), transforms the data into a clean format, and loads it into timestamped CSV files for tracking and analysis.

**Key Features:**
- Automated data extraction from Alpha Vantage API
- Data transformation with proper type casting and column standardization
- Error handling and API rate limit compliance
- Timestamped output files for historical tracking
- Support for multiple stock symbols

## 🏗️ Architecture

```
API Source (Alpha Vantage) 
    ↓
Extract (Python requests)
    ↓
Transform (Pandas - clean, type cast, combine)
    ↓
Load (CSV storage with timestamps)
```

## 📊 Data Schema

The pipeline outputs CSV files with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| date | datetime | Trading date |
| symbol | string | Stock ticker symbol |
| open | float | Opening price |
| high | float | Highest price of the day |
| low | float | Lowest price of the day |
| close | float | Closing price |
| volume | integer | Number of shares traded |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Alpha Vantage API key (free tier available at [alphavantage.co](https://www.alphavantage.co/support/#api-key))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-data-pipeline.git
cd stock-data-pipeline
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
- Sign up for a free API key at Alpha Vantage
- Add your API key to the script or use environment variables

### Usage

Run the pipeline:
```bash
python stock_pipeline.py
```

The script will:
1. Fetch data for all configured stock symbols
2. Process and clean the data
3. Save output to `stock_data/stock_data_YYYY-MM-DD.csv`

### Configuration

Modify the `symbols` list in the script to track different stocks:
```python
symbols = ["AAPL", "GOOGL", "TSLA", "NVDA", "MSFT", "AMZN"]
```

## 📁 Project Structure

```
stock-data-pipeline/
│
├── stock_pipeline.py          # Main ETL script
├── stock_data/                # Output directory for CSV files
│   └── stock_data_YYYY-MM-DD.csv
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Technical Decisions

**Why CSV instead of a database?**
- Lightweight and portable for initial development
- Easy to inspect and share
- Can be easily migrated to a database later (PostgreSQL, DuckDB)

**API Rate Limiting:**
- Alpha Vantage free tier: 25 calls/day, 5 calls/minute
- Added 12-second delay between requests to respect limits
- Error handling ensures graceful failures

## 📈 Future Enhancements

- [ ] Add Apache Airflow for scheduling and orchestration
- [ ] Containerize with Docker
- [ ] Implement data quality checks (missing values, duplicate dates)
- [ ] Add database storage (PostgreSQL/DuckDB)
- [ ] Create visualization dashboard (Streamlit/Plotly)
- [ ] Add unit tests
- [ ] Implement incremental loading (only fetch new data)

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Pandas** - Data manipulation and transformation
- **Requests** - HTTP client for API calls
- **Alpha Vantage API** - Financial data source

## 📝 What I Learned

- Building ETL pipelines from scratch
- Working with financial time-series data
- API rate limiting and error handling best practices
- Data type conversion and validation
- Structuring data engineering projects for production

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

MIT License - feel free to use this project for learning and portfolio purposes.

## 👤 Contact

Anisat Olapade - [LinkedIn](https://www.linkedin.com/in/anisat-olapade/) | [Email](mailto:anisatolapade@gmail.com)

Project Link: [https://github.com/Lahmie/Data-Engineering-Projects/stock-data-pipeline](https://github.com/Lahmie/Data-Engineering-Projects/stock-data-pipeline)