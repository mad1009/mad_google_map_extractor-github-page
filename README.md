# 🗺️ Google Maps Scraper Pro

A powerful, multi-threaded Google Maps scraper with advanced anti-detection techniques and a modern GUI interface.

## ✨ Features

- **🎨 Modern GUI** - Built with CustomTkinter for a sleek, user-friendly interface
- **⚡ Multi-threading** - Scrape multiple queries simultaneously without UI freezing
- **🔒 Anti-Detection** - Advanced stealth techniques to avoid being blocked
- **🌐 Proxy Support** - Rotate proxies to prevent rate limiting
- **📊 Data Export** - Export results to CSV, Excel, or JSON
- **🧹 Data Processing** - Automatic cleaning, deduplication, and validation
- **📝 Comprehensive Logging** - Detailed logs for debugging and monitoring

## 🏗️ Architecture

```
mad_google_map_extractor/
├── src/
│   ├── gui/                    # User interface
│   │   ├── main_window.py      # Main application window
│   │   ├── styles.py           # GUI styling
│   │   └── components/         # Reusable UI components
│   ├── scraper/                # Web scraping logic
│   │   ├── google_maps.py      # Main scraper
│   │   ├── stealth.py          # Anti-detection techniques
│   │   └── proxy_manager.py    # Proxy rotation
│   ├── utils/                  # Utilities
│   │   ├── logger.py           # Logging system
│   │   ├── data_processor.py   # Data cleaning
│   │   └── exporter.py         # Export functionality
│   └── core/                   # Core components
│       ├── config.py           # Configuration manager
│       └── worker.py           # Multi-threading workers
├── config/                     # Configuration files
├── output/                     # Scraped data output
├── logs/                       # Application logs
├── main.py                     # Application entry point
└── requirements.txt            # Python dependencies
```

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- Windows/Linux/macOS

### Step 1: Clone or Download

Download the project to your local machine.

### Step 2: Create Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate  # Windows PowerShell
```

### Step 3: Install Dependencies

```powershell
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

## 📖 Usage

### Quick Start

1. **Run the application:**
   ```powershell
   python main.py
   ```

2. **Enter search queries** (one per line):
   ```
   restaurants in New York
   coffee shops in Los Angeles
   hotels in Miami
   ```

3. **Configure settings:**
   - Max Results: Number of results per query (default: 20)
   - Threads: Number of concurrent workers (default: 3)
   - Use Proxies: Enable proxy rotation (optional)
   - Headless Mode: Run browser invisibly (recommended)

4. **Click "Start Scraping"** and wait for results

5. **Export data:**
   - Click "Export CSV" or "Export Excel"
   - Find your data in the `output/` folder

### Using Proxies

1. Open `config/proxies.txt`
2. Add your proxies (one per line):
   ```
   http://proxy1.example.com:8080
   http://username:password@proxy2.example.com:8080
   ```
3. Enable "Use Proxies" checkbox in the GUI

### Configuration

Edit `config/settings.json` to customize:

```json
{
    "max_threads": 3,
    "request_delay_min": 2,
    "request_delay_max": 5,
    "use_proxy": false,
    "headless": true,
    "timeout": 30000,
    "max_results_per_query": 20
}
```

## 🛡️ Anti-Detection Features

The scraper implements multiple techniques to avoid detection:

1. **Browser Fingerprinting**
   - Removes automation flags
   - Randomizes user agents
   - Spoofs browser properties

2. **Human-like Behavior**
   - Random delays between actions
   - Realistic typing speed
   - Mouse movement simulation

3. **Network Stealth**
   - Proxy rotation support
   - Realistic HTTP headers
   - Connection pooling

4. **Playwright Stealth**
   - Uses Playwright (better than Selenium)
   - Stealth plugin integration
   - WebDriver detection bypass

## 📊 Scraped Data

Each business entry contains:

- **Name** - Business name
- **Rating** - Star rating (0-5)
- **Reviews** - Number of reviews
- **Category** - Business category
- **Address** - Full address
- **Phone** - Phone number
- **Website** - Website URL
- **Price Level** - Price indicator ($, $$, $$$)

## 🔧 Advanced Usage

### Programmatic Usage

```python
from src.scraper.google_maps import GoogleMapsScraper
from src.utils.exporter import DataExporter
import asyncio

async def scrape():
    scraper = GoogleMapsScraper(headless=True)
    await scraper.initialize()
    
    page = await scraper.create_page()
    await scraper.search_location(page, "restaurants in NYC")
    results = await scraper.extract_businesses(page, max_results=50)
    
    await scraper.close()
    
    # Export results
    DataExporter.to_csv(results, "my_results.csv")

# Run
asyncio.run(scrape())
```

### Custom Data Processing

```python
from src.utils.data_processor import DataProcessor

processor = DataProcessor()

# Clean data
cleaned = processor.clean_results(raw_results)

# Remove duplicates
unique = processor.remove_duplicates(cleaned)

# Filter by rating
high_rated = processor.filter_by_rating(unique, min_rating=4.0)

# Sort by rating
sorted_results = processor.sort_by_rating(high_rated)
```

## 📁 Output Files

Results are saved to the `output/` folder with timestamps:

- CSV: `google_maps_results_20231215_143022.csv`
- Excel: `google_maps_results_20231215_143022.xlsx`
- JSON: `google_maps_results_20231215_143022.json`

Logs are saved to the `logs/` folder:

- `scraper_20231215_143022.log`

## ⚠️ Important Notes

### Legal & Ethical Usage

- **Respect robots.txt** and Google's Terms of Service
- **Rate limiting** - Don't scrape too aggressively
- **Use proxies** for large-scale scraping
- **Personal use** - This tool is for educational/research purposes

### Performance Tips

1. **Headless mode** - Faster and uses less resources
2. **Optimal threads** - 3-5 threads work best
3. **Proxies** - Use for large scraping jobs
4. **Max results** - Start with 20-50 per query

### Troubleshooting

**Browser won't launch:**
```powershell
playwright install chromium --force
```

**Import errors:**
```powershell
pip install -r requirements.txt --upgrade
```

**No proxies working:**
- Test proxies individually
- Check proxy format: `http://host:port`
- Some free proxies may be unreliable

**Application freezes:**
- Reduce number of threads
- Enable headless mode
- Check system resources

## 🔄 Updates & Maintenance

To update the scraper:

1. **Update dependencies:**
   ```powershell
   pip install -r requirements.txt --upgrade
   ```

2. **Update Playwright:**
   ```powershell
   playwright install chromium --force
   ```

## 📝 Logging

Logs provide detailed information:

- **INFO** - General operation info
- **WARNING** - Non-critical issues
- **ERROR** - Errors during scraping
- **DEBUG** - Detailed debugging info

Change log level in `.env`:
```
LOG_LEVEL=DEBUG
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional data fields extraction
- More export formats
- Enhanced anti-detection
- UI improvements
- Performance optimization

## 📜 License

This project is for educational purposes only. Use responsibly and in accordance with Google's Terms of Service.

## 🙏 Acknowledgments

- **CustomTkinter** - Modern GUI framework
- **Playwright** - Browser automation
- **Pandas** - Data processing

## 📞 Support

For issues or questions:

1. Check the logs in `logs/` folder
2. Review configuration in `config/settings.json`
3. Enable DEBUG logging for more details

---

**Happy Scraping! 🚀**

*Remember: Always scrape responsibly and ethically.*
