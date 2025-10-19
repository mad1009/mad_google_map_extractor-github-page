# 🗺️ Google Maps Scraper Pro

A powerful, production-ready Google Maps scraper with advanced anti-detection, intelligent interface handling, and a modern three-column GUI with real-time monitoring and desktop notifications.

## ✨ Key Features

### 🎨 Modern Three-Column Interface
- **Left Panel** - Input controls and settings for quick configuration
- **Middle Panel** - Real-time worker thread status and activity monitoring
- **Right Panel** - Live color-coded logs with emoji indicators for easy scanning

### ⚡ Smart Multi-Threading
- Parallel scraping with configurable worker threads (1-10 threads)
- Thread-safe UI updates using queue-based logging (no freezing!)
- Real-time worker status showing active/idle state for each thread
- Individual task progress tracking with completion counter

### 🔒 Advanced Anti-Detection
- **Dual Interface Detection** - Automatically detects and handles both desktop and mobile-like Google Maps layouts
- **Close-and-Recreate Strategy** - Forces proper desktop interface by recreating pages until correct layout loads
- **Windows Desktop User Agents** - 6 hardcoded Chrome/Edge user agents for Windows 10/11
- **Playwright Stealth** - Advanced browser fingerprint masking and automation detection bypass

### 💾 Intelligent Auto-Save
- **Per-Task CSV Files** - Each search query saves to separate CSV immediately upon completion
- **Sanitized Filenames** - Auto-generates safe filenames from query names with timestamps
- **Combined Results** - Creates unified CSV with all unique results at the end
- **Auto-Open** - Automatically opens combined CSV file when scraping completes

### 🔔 Desktop Notifications
- **Cross-Platform** - Works on Windows, macOS, and Linux using plyer library
- **Completion Alerts** - Notifies when all tasks finish with results count
- **Error Alerts** - Immediate notification when individual tasks fail
- **Non-Intrusive** - System tray notifications don't interrupt your workflow

### 📊 Advanced Data Extraction
- **Click-Based Extraction** - Clicks each listing and extracts from detail panel using stable XPath selectors
- **Comprehensive Data** - Name, rating, reviews, category, address, phone, website, hours, price level
- **Smart Deduplication** - Automatically removes duplicate entries across all results
- **Data Validation** - Cleans and validates extracted information

### 🎨 Color-Coded Logging
- **DEBUG** (Gray) - Detailed debugging information
- **INFO** (Blue) - General operation updates
- **SUCCESS** (Green) - Task completions and successes
- **WARNING** (Orange) - Non-critical issues
- **ERROR** (Red) - Error messages and failures
- **CRITICAL** (Dark Red) - Critical system errors

## 🏗️ Project Architecture

```
mad_google_map_extractor/
├── src/
│   ├── gui/                        # User Interface Components
│   │   ├── main_window.py          # Three-column main window with real-time updates
│   │   ├── styles.py               # CustomTkinter styling and themes
│   │   └── components/             # Reusable UI components
│   │
│   ├── scraper/                    # Web Scraping Engine
│   │   ├── google_maps.py          # Main scraper with dual interface handling
│   │   ├── stealth.py              # Anti-detection and fingerprint masking
│   │   └── proxy_manager.py        # Proxy rotation and management
│   │
│   ├── utils/                      # Utility Modules
│   │   ├── logger.py               # Queue-based thread-safe logging with UI handler
│   │   ├── data_processor.py       # Data cleaning, deduplication, validation
│   │   ├── exporter.py             # CSV, Excel, JSON export functionality
│   │   └── notifier.py             # Cross-platform desktop notifications
│   │
│   └── core/                       # Core System Components
│       ├── config.py               # Configuration management
│       └── worker.py               # Multi-threaded worker pool with async support
│
├── config/                         # Configuration Files
│   ├── settings.json               # Application settings
│   └── proxies.txt                 # Proxy list (optional)
│
├── output/                         # Scraped Data Output
│   ├── {query_name}_{timestamp}.csv        # Per-task results
│   └── combined_all_results_{timestamp}.csv # Unified results
│
├── logs/                           # Application Logs
│   └── scraper_{timestamp}.log     # Detailed operation logs
│
├── env/                            # Virtual Environment
│
├── main.py                         # Application Entry Point
├── requirements.txt                # Python Dependencies
└── README.md                       # This File
```

## 📸 Screenshots

### Three-Column Layout
- **Left**: Search queries, settings (Max Results, Threads), checkboxes (Proxies, Headless, Auto-save), Start/Stop buttons
- **Middle**: Worker threads status with progress bar, real-time thread activity, general status log
- **Right**: Large results panel with color-coded logs, export buttons (CSV, Excel, Clear)

### Features in Action
- Real-time worker status showing "Worker 1: 🔄 restaurants in New York"
- Color-coded logs: Blue info, Green success, Orange warnings, Red errors
- Progress bar showing 3/5 tasks completed
- Desktop notifications when tasks complete or fail

## 🚀 Quick Start Installation

### Prerequisites

- **Python 3.10+** (Tested on Python 3.10-3.13)
- **Windows 10/11** (macOS and Linux also supported)
- **4GB RAM minimum** (8GB recommended for multiple threads)
- **Internet connection** (for scraping and Playwright installation)

### One-Command Setup (PowerShell)

```powershell
# Run the setup script
.\setup.ps1
```

This will automatically:
1. Create virtual environment
2. Install all Python dependencies
3. Install Playwright browsers
4. Verify installation

### Manual Installation

#### Step 1: Create Virtual Environment

```powershell
# Create virtual environment
python -m venv env

# Activate virtual environment
.\env\Scripts\Activate.ps1  # Windows PowerShell
# OR
.\env\Scripts\activate      # Windows CMD
# OR
source env/bin/activate     # macOS/Linux
```

#### Step 2: Install Dependencies

```powershell
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers (Chromium)
playwright install chromium
```

#### Step 3: Install Notifications (Optional)

```powershell
# For desktop notifications
pip install plyer

# Test notifications
python -c "from plyer import notification; notification.notify(title='Test', message='Working!', timeout=10)"
```

### Verify Installation

```powershell
# Run validation script
python validate_structure.py

# Should show: "✅ All checks passed!"
```

## 📖 Usage Guide

### Starting the Application

```powershell
# Make sure virtual environment is activated
.\env\Scripts\Activate.ps1

# Run the scraper
python main.py
```

The modern three-column interface will open with:
- **Left Panel**: Input and controls
- **Middle Panel**: Worker status monitoring
- **Right Panel**: Live results and logs

### Basic Workflow

#### 1. Enter Search Queries (Left Panel)

In the "Search Queries" textbox, enter one query per line:

```
restaurants in New York
coffee shops in Los Angeles
hotels in Miami Beach
gyms near Times Square
dentists in Brooklyn
```

**Tips:**
- Be specific with locations for better results
- Use natural language (e.g., "pizza near Central Park")
- Mix different business types for varied data

#### 2. Configure Settings (Left Panel)

| Setting | Description | Recommended |
|---------|-------------|-------------|
| **Max Results** | Results per query | 20-50 |
| **Threads** | Concurrent workers | 3-5 |
| **Use Proxies** | Enable proxy rotation | Optional |
| **Headless Mode** | Hide browser windows | ✅ Enabled |
| **Auto-save CSV** | Save results automatically | ✅ Enabled |

#### 3. Monitor Progress (Middle Panel)

Watch real-time updates:
- **Progress Bar** - Shows X/Y tasks completed
- **Worker Status** - See what each thread is doing:
  ```
  Worker 1: 🔄 restaurants in New York
  Worker 2: 🔄 coffee shops in Los Angeles  
  Worker 3: ⏸️ Idle
  ```
- **Task Counter** - "Processed: 3/5 tasks"
- **Results Count** - "Total results: 87"

#### 4. View Live Results (Right Panel)

Color-coded logs appear in real-time:

```
ℹ️ Starting scraping for 5 queries
📊 Settings: 20 results per query, 3 threads
✅ restaurants in New York: 20 results extracted
💾 Saved restaurants in New York results to: restaurants_in_New_York_20251018_143025.csv
❌ Error: Task 'invalid query' failed: No results found
🎉 Scraping complete! Total results: 87
💾 Saved combined results to: combined_all_results_20251018_143030.csv
📂 Opened combined CSV file
```

#### 5. Desktop Notifications

If `plyer` is installed, you'll receive system notifications:
- **Completion**: "Scraping Complete! Completed 5 tasks - Extracted 87 results"
- **Errors**: "Task 'coffee shops' failed: Timeout error"
- **Warnings**: "Scraping complete but no results found"

#### 6. Access Your Data

**Auto-Saved Files** (in `output/` folder):
- Per-task CSVs: `restaurants_in_New_York_20251018_143025.csv`
- Combined CSV: `combined_all_results_20251018_143030.csv` (opens automatically)

**Manual Export** (Right Panel buttons):
- Click **📄 CSV** to export combined results
- Click **📊 Excel** for .xlsx format
- Click **🗑️ Clear** to reset results

### Advanced Features

#### Using Proxies

1. **Add proxies** to `config/proxies.txt` (one per line):
   ```
   http://proxy1.example.com:8080
   http://username:password@proxy2.example.com:8080
   socks5://proxy3.example.com:1080
   ```

2. **Enable "Use Proxies"** checkbox in the GUI

3. **Scraper will rotate** through proxies automatically

#### Desktop Notifications Setup

```powershell
# Install notification library
pip install plyer

# Test it works
python -c "from plyer import notification; notification.notify(title='Test', message='Notifications working!', timeout=10)"
```

**Windows Settings:**
- Go to Settings → System → Notifications & actions
- Enable "Get notifications from apps and other senders"
- Make sure Python.exe is allowed

#### Configuration File

Edit `config/settings.json` for advanced customization:

```json
{
    "max_threads": 3,
    "request_delay_min": 2,
    "request_delay_max": 5,
    "use_proxy": false,
    "headless": true,
    "timeout": 30000,
    "max_results_per_query": 20,
    "log_level": "INFO"
}
```

**Key Settings:**
- `max_threads`: Number of worker threads (1-10)
- `request_delay_min/max`: Random delay between actions (seconds)
- `timeout`: Page load timeout (milliseconds)
- `log_level`: DEBUG, INFO, WARNING, ERROR, CRITICAL

## 🛡️ Anti-Detection System

### Dual Interface Detection

Google Maps can serve two different interfaces:

1. **Desktop Interface** (GOOD ✅)
   - Has `input#searchboxinput` element
   - Standard desktop layout
   - Reliable and stable

2. **Mobile-Like Interface** (BAD ❌)
   - Has `div.JdG3E[role="button"]` instead
   - Compact mobile-optimized layout
   - Triggers detection more easily

**Our Solution:**
- Automatically detects which interface loaded
- If mobile interface detected, **closes and recreates page**
- Repeats up to 5 times until desktop interface loads
- Ensures consistent, reliable scraping

### Windows Desktop User Agents

Uses 6 hardcoded user agents for Windows 10/11:
```python
WINDOWS_DESKTOP_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    # ... 4 more variants
]
```

Forces desktop interface by using desktop user agents.

### Stealth Techniques

1. **Browser Fingerprinting Bypass**
   - Removes `navigator.webdriver` flag
   - Spoofs browser properties
   - Randomizes viewport sizes
   - Uses realistic window dimensions

2. **Human-like Behavior**
   - Random delays between actions (2-5 seconds)
   - Realistic typing speed
   - Scrolling simulation
   - Mouse movement patterns

3. **Network Stealth**
   - Realistic HTTP headers
   - Proper referer handling
   - Connection pooling
   - Request timing randomization

4. **Playwright Stealth Plugin**
   - Advanced WebDriver detection bypass
   - Chrome DevTools Protocol hiding
   - Permissions API spoofing
   - Plugin array randomization

### Click-Based Extraction

Instead of parsing HTML directly, we:
1. **Click each business listing** to open detail panel
2. **Extract from detail panel** using stable XPath selectors
3. **Wait for elements** to load properly
4. **Handle errors gracefully** if data missing

This approach is more reliable and mimics human behavior.

## 📊 Extracted Data Fields

Each business entry contains up to 15+ data points:

| Field | Description | Example |
|-------|-------------|---------|
| **Name** | Business name | "Joe's Pizza" |
| **Rating** | Star rating | "4.5" |
| **Reviews** | Number of reviews | "1,234" |
| **Category** | Business type | "Pizza restaurant" |
| **Address** | Full address | "123 Main St, New York, NY 10001" |
| **Phone** | Phone number | "(212) 555-0123" |
| **Website** | Website URL | "https://joespizza.com" |
| **Hours** | Opening hours | "Mon-Fri: 11AM-10PM" |
| **Price Level** | Price indicator | "$$" |
| **Plus Code** | Google Plus Code | "ABCD+XY New York" |
| **Coordinates** | GPS coordinates | "40.7589,-73.9851" |
| **Service Options** | Delivery, dine-in, etc. | "Dine-in · Takeout · Delivery" |
| **Accessibility** | Wheelchair accessible | "Yes" |
| **Amenities** | WiFi, parking, etc. | "Free Wi-Fi · Outdoor seating" |
| **Description** | Business description | "Family-owned pizza since 1975" |

**Data Quality:**
- All fields validated and cleaned
- Missing data marked as "N/A"
- Duplicates removed across all results
- Phone numbers formatted consistently
- Ratings converted to numeric values

## 📁 Output Files

### Per-Task CSV Files

Each search query creates a separate file immediately after completion:

**Filename Format:** `{sanitized_query}_{timestamp}.csv`

**Examples:**
```
restaurants_in_New_York_20251018_143025.csv
coffee_shops_in_Los_Angeles_20251018_143026.csv
hotels_in_Miami_Beach_20251018_143027.csv
```

**Benefits:**
- Data saved immediately (prevents loss if scraping stops)
- Easy to find results for specific queries
- Can analyze individual queries separately

### Combined Results CSV

At the end of scraping, all unique results are merged into one file:

**Filename Format:** `combined_all_results_{timestamp}.csv`

**Example:** `combined_all_results_20251018_143030.csv`

**Features:**
- Contains all unique businesses (duplicates removed)
- Opens automatically in default spreadsheet app
- UTF-8 encoding for international characters
- Proper CSV quoting for fields with commas

### Export Formats

| Format | Extension | Use Case |
|--------|-----------|----------|
| **CSV** | `.csv` | Excel, Google Sheets, databases |
| **Excel** | `.xlsx` | Advanced Excel analysis, formatting |
| **JSON** | `.json` | APIs, programming, data processing |

### Log Files

Detailed logs saved to `logs/` folder:

**Filename:** `scraper_{timestamp}.log`

**Contains:**
- All operations with timestamps
- Error stack traces
- Debug information
- Worker thread activity
- Network requests

## � Building Standalone Executable

Convert the application to a standalone `.exe` file for easy distribution.

### Quick Build

**Option 1: PowerShell Script (Recommended)**
```powershell
# One command to build everything
.\build_exe.ps1
```

**Option 2: Batch File**
```cmd
build_exe.bat
```

### Build Process

The build script will:
1. ✅ Activate virtual environment
2. ✅ Install PyInstaller
3. ✅ Clean previous builds
4. ✅ Check for icon file
5. ✅ Build executable
6. ✅ Verify build success

**Output:** `dist/GoogleMapsScraper/GoogleMapsScraper.exe`

### Custom Icon (Optional)

**Create Icon with Python:**
```powershell
# Generates a map pin icon automatically
python create_icon.py
```

**Use Your Own Icon:**
```powershell
# Create assets folder
New-Item -ItemType Directory -Path "assets" -Force

# Copy your icon (must be .ico format)
Copy-Item "your_icon.ico" -Destination "assets\icon.ico"
```

**Skip Icon:**
- Build will work with default Python icon
- Edit `build_exe.spec`: change `icon='assets/icon.ico'` to `icon=None`

### Distribution

**What to Share:**
```
GoogleMapsScraper/          # Share entire folder
├── GoogleMapsScraper.exe   # Main executable
├── _internal/              # Dependencies
├── config/                 # Settings
│   ├── settings.json
│   └── proxies.txt
├── output/                 # Results (empty)
└── logs/                   # Logs (empty)
```

**Create Distribution Package:**
```powershell
# Compress to ZIP
Compress-Archive -Path "dist\GoogleMapsScraper" -DestinationPath "GoogleMapsScraper_v3.0.zip"
```

### End User Instructions

Users can run the executable without Python installed:

1. **Extract ZIP** to desired location
2. **Double-click** `GoogleMapsScraper.exe`
3. **Start scraping** - Chromium browser is bundled, ready immediately!

### Build Documentation

- **README_EXE.md** - Complete executable build guide with browser bundling
- **build_exe.spec** - PyInstaller configuration
- **create_icon.py** - Icon generation script

### System Requirements (For Executable)

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10/11 (64-bit) |
| **RAM** | 8 GB recommended |
| **Disk Space** | 1 GB (includes browsers) |
| **Python** | Not required! |

**Note:** End users don't need Python installed. All dependencies are bundled in the executable.

## �🔧 Advanced Usage

### Programmatic API

Use the scraper in your own Python scripts:

```python
import asyncio
from src.scraper.google_maps import GoogleMapsScraper
from src.utils.exporter import DataExporter

async def scrape_google_maps():
    """Scrape Google Maps programmatically"""
    
    # Initialize scraper
    scraper = GoogleMapsScraper(
        headless=True,
        proxy=None,  # or "http://proxy:8080"
        timeout=30000
    )
    
    try:
        # Start browser
        await scraper.initialize()
        
        # Create page
        page = await scraper.create_page()
        
        # Search and extract
        await scraper.search_location(page, "restaurants in New York")
        results = await scraper.extract_businesses(page, max_results=50)
        
        # Export results
        DataExporter.to_csv(results, filename="my_results.csv")
        
        print(f"✅ Extracted {len(results)} businesses")
        
    finally:
        # Always close browser
        await scraper.close()

# Run the async function
asyncio.run(scrape_google_maps())
```

### Multi-Query Scraping

```python
from src.core.worker import WorkerPool
from src.scraper.google_maps import GoogleMapsScraper

# Define your scraping function
async def scrape_query(query, max_results, use_proxy, headless, proxy_manager):
    scraper = GoogleMapsScraper(headless=headless)
    await scraper.initialize()
    page = await scraper.create_page()
    await scraper.search_location(page, query)
    results = await scraper.extract_businesses(page, max_results)
    await scraper.close()
    return results

# Create worker pool
queries = [
    "restaurants in NYC",
    "coffee shops in LA",
    "hotels in Miami"
]

pool = WorkerPool(
    num_workers=3,
    scraper_func=scrape_query,
    max_results=20,
    use_proxy=False,
    headless=True
)

# Add tasks and start
pool.add_tasks(queries)
pool.start()

# Get results
all_results = []
while pool.is_active():
    result = pool.get_result(timeout=1)
    if result and result['status'] == 'success':
        all_results.extend(result['result'])

pool.stop(wait=True)
print(f"Total results: {len(all_results)}")
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

# Filter by reviews
popular = processor.filter_by_reviews(high_rated, min_reviews=100)

# Sort by rating
sorted_results = processor.sort_by_rating(popular, ascending=False)

# Export
DataExporter.to_excel(sorted_results, filename="premium_businesses.xlsx")
```

### Desktop Notifications in Code

```python
from src.utils.notifier import Notifier

# Show success notification
Notifier.notify_success("Scraping completed successfully!")

# Show error notification
Notifier.notify_error("Failed to connect to proxy")

# Show custom notification
Notifier.notify(
    title="Processing Complete",
    message="Extracted 500 businesses from 10 queries",
    timeout=15  # seconds
)

# Show completion notification
Notifier.notify_complete(
    total_results=500,
    total_tasks=10
)
```

## ⚠️ Troubleshooting

### Common Issues & Solutions

#### Issue: Application Won't Start

**Error:** `ModuleNotFoundError: No module named 'customtkinter'`

**Solution:**
```powershell
# Activate virtual environment
.\env\Scripts\Activate.ps1

# Reinstall dependencies
pip install -r requirements.txt
```

---

#### Issue: Browser Won't Launch

**Error:** `Playwright browser not found`

**Solution:**
```powershell
# Reinstall Playwright browsers
playwright install chromium --force

# Or install all browsers
playwright install
```

---

#### Issue: UI Freezing or Not Responding

**Symptoms:** Window becomes unresponsive during scraping

**Solution:**
- ✅ Make sure "Headless Mode" is enabled
- ✅ Reduce number of threads (try 2-3)
- ✅ Close other applications using browser
- ✅ Check system resources (RAM, CPU)

---

#### Issue: No Results Found

**Symptoms:** Scraping completes but 0 results

**Causes & Solutions:**

1. **Wrong Interface Detected**
   - Check logs for "Mobile-like interface detected"
   - Should see "Desktop interface confirmed"
   - If stuck on mobile interface, increase retry attempts in code

2. **Search Query Too Specific**
   - Use broader terms: "restaurants in NYC" instead of "vegan gluten-free restaurants on 5th Avenue"
   - Try different query formats

3. **Rate Limiting**
   - Enable "Use Proxies" checkbox
   - Reduce number of threads
   - Increase delays in `config/settings.json`

---

#### Issue: Notifications Not Showing

**Symptoms:** No desktop notifications appear

**Solution:**

```powershell
# Install notification library
pip install plyer

# Test notifications
python -c "from plyer import notification; notification.notify(title='Test', message='Working!', timeout=10)"
```

**Windows Settings:**
1. Open Settings (Win + I)
2. Go to System → Notifications & actions  
3. Enable "Get notifications from apps and other senders"
4. Make sure Python.exe is allowed

**Still not working?**
- Notifications are optional - scraper works fine without them
- Check Action Center (Win + A) - notifications may be there
- Disable Focus Assist (system tray icon)

---

#### Issue: Proxy Errors

**Error:** `ProxyConnectionError` or `Proxy authentication failed`

**Solutions:**

1. **Test Proxies First:**
   ```python
   from src.scraper.proxy_manager import ProxyManager
   pm = ProxyManager()
   pm.test_proxies()  # Removes dead proxies
   ```

2. **Check Proxy Format:**
   ```
   ✅ http://proxy.com:8080
   ✅ http://user:pass@proxy.com:8080
   ✅ socks5://proxy.com:1080
   ❌ proxy.com:8080  (missing protocol)
   ```

3. **Use Fewer Proxies:**
   - Some free proxies are unreliable
   - Better to have 2-3 working proxies than 50 dead ones

---

#### Issue: CSV File Won't Open

**Error:** "File is corrupted" or weird characters

**Solution:**

1. **Open with UTF-8 Encoding:**
   - Excel: Data → Get External Data → From Text
   - Select UTF-8 encoding
   - Import as CSV

2. **Use Google Sheets:**
   - Upload CSV to Google Sheets
   - Automatically handles UTF-8

3. **Use LibreOffice Calc:**
   - Better UTF-8 support than Excel
   - Free alternative to Excel

---

#### Issue: Memory Errors

**Error:** `MemoryError` or system slowdown

**Solutions:**
- Reduce number of threads (try 2)
- Reduce max results per query (try 10-20)
- Close other applications
- Enable headless mode
- Restart application between large scraping sessions

---

#### Issue: Import Errors After Update

**Error:** `ImportError` or `AttributeError`

**Solution:**
```powershell
# Remove old packages
pip uninstall -y customtkinter playwright pandas openpyxl

# Reinstall fresh
pip install -r requirements.txt --upgrade --force-reinstall

# Reinstall Playwright browsers
playwright install chromium
```

### Performance Optimization

#### Optimal Settings

For best performance:

| Setting | Small Jobs (1-5 queries) | Large Jobs (10+ queries) |
|---------|-------------------------|-------------------------|
| Threads | 3 | 5 |
| Max Results | 50 | 20 |
| Headless | Yes | Yes |
| Proxies | No | Yes |

#### Speed vs. Stealth

**Faster (More Detection Risk):**
- More threads (5-10)
- Shorter delays (1-2 seconds)
- No proxies
- Higher max results

**Stealthier (Slower but Safer):**
- Fewer threads (1-3)
- Longer delays (3-5 seconds)
- Use proxies
- Lower max results

### Debug Mode

Enable detailed logging:

1. **Edit `config/settings.json`:**
   ```json
   {
       "log_level": "DEBUG"
   }
   ```

2. **Check logs in `logs/` folder** for detailed information

3. **Console output** will show all operations including:
   - Page navigation
   - Element searches
   - Data extraction
   - Worker thread activity

### Getting Help

If you're still stuck:

1. **Check log files** in `logs/` folder
2. **Enable DEBUG logging** (see above)
3. **Run validation script:** `python validate_structure.py`
4. **Check Python version:** Should be 3.10+
5. **Verify virtual environment is activated:** Command prompt should show `(env)`

**Include this info when asking for help:**
- Python version (`python --version`)
- Error message (full stack trace)
- Log file contents
- Steps to reproduce

## ⚖️ Legal & Ethical Considerations

### Terms of Service

**Important:** This tool is for educational and research purposes only.

- **Read Google's Terms of Service** before using
- **Respect robots.txt** and rate limiting
- **Don't overload servers** - use reasonable delays
- **Commercial use** may require permission
- **Personal use only** - don't resell scraped data

### Best Practices

✅ **DO:**
- Use for research and personal projects
- Respect rate limits (enable delays)
- Use proxies for large-scale jobs
- Give credit when using scraped data
- Test with small queries first

❌ **DON'T:**
- Scrape aggressively (causes server load)
- Ignore rate limiting or bans
- Resell scraped data commercially
- Use for spam or malicious purposes
- Circumvent explicit blocking

### Responsible Scraping

This tool includes anti-detection not to bypass security, but to:
- Reduce false positives (legitimate use flagged as bot)
- Minimize server load through efficient requests
- Provide stable, reliable data extraction

**Use responsibly.** If a website asks you to stop, respect that.

## 🔒 Privacy & Security

### Data Handling

- **Local Only** - All data stays on your machine
- **No Telemetry** - No usage data sent anywhere
- **No API Keys** - Doesn't use Google Maps API (which requires payment)
- **Open Source** - Inspect the code yourself

### Proxy Security

- **HTTPS Proxies** recommended for encrypted traffic
- **Paid Proxies** more reliable than free ones
- **Test Proxies** before adding to `proxies.txt`
- **Rotate Regularly** to avoid bans

### Logs

- Logs contain scraped data and queries
- Stored locally in `logs/` folder
- Delete old logs if they contain sensitive info
- No logs sent externally

## 🔄 Updates & Maintenance

### Keeping Updated

Google Maps changes frequently. To keep scraper working:

```powershell
# Update Python packages
pip install -r requirements.txt --upgrade

# Update Playwright browsers
playwright install chromium --force

# Check for code updates
git pull  # if using git
```

### Changelog

**v3.0 (Current)**
- ✅ Three-column modern UI layout
- ✅ Dual interface detection and handling
- ✅ Per-task CSV auto-save
- ✅ Desktop notifications (plyer)
- ✅ Queue-based thread-safe logging
- ✅ Color-coded log messages
- ✅ Real-time worker status monitoring
- ✅ Windows desktop user agents
- ✅ Click-based stable extraction

**v2.0**
- Multi-threaded scraping
- Proxy support
- CustomTkinter GUI
- Data export formats

**v1.0**
- Initial release
- Basic scraping functionality

### Known Issues

1. **Google Maps Updates**
   - Google changes their layout occasionally
   - XPath selectors may need updating
   - Check logs for extraction errors

2. **Windows Focus Assist**
   - May block desktop notifications
   - Disable Focus Assist in system tray

3. **Large Result Sets**
   - Memory usage increases with results
   - Export/clear regularly for long sessions

### Reporting Issues

If you find a bug:

1. Check if it's already in Known Issues
2. Enable DEBUG logging
3. Reproduce the issue
4. Collect logs from `logs/` folder
5. Note your Python version and OS

## 📚 Documentation

### Additional Resources

- **ARCHITECTURE.md** - Detailed system architecture
- **IMPLEMENTATION_SUMMARY.md** - Implementation details
- **CHECKLIST.md** - Development checklist
- **QUICKSTART.md** - Quick start guide
- **NOTIFICATIONS.md** - Notification system documentation

### Code Documentation

All modules have detailed docstrings:

```python
# View documentation for any module
python -c "from src.scraper.google_maps import GoogleMapsScraper; help(GoogleMapsScraper)"
```

### Logging Levels

| Level | When to Use | Example |
|-------|-------------|---------|
| DEBUG | Development, troubleshooting | Element locations, timing |
| INFO | Normal operation | Task started, results found |
| WARNING | Minor issues | Slow response, missing data |
| ERROR | Failures | Network errors, extraction failed |
| CRITICAL | Severe issues | Browser crash, system error |

## 🤝 Contributing

While this is primarily an educational project, improvements are welcome:

**Areas for Enhancement:**
- Additional data fields extraction
- More export formats (XML, SQLite)
- Enhanced anti-detection techniques
- UI/UX improvements
- Performance optimization
- Better error handling
- Additional platforms (Yelp, TripAdvisor, etc.)

**Coding Standards:**
- Follow PEP 8 style guide
- Add docstrings to all functions
- Include type hints
- Write descriptive commit messages
- Test before submitting

## 🙏 Acknowledgments

### Technologies Used

- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - Modern, beautiful GUI framework
- **[Playwright](https://playwright.dev/)** - Reliable browser automation
- **[Pandas](https://pandas.pydata.org/)** - Powerful data processing
- **[Openpyxl](https://openpyxl.readthedocs.io/)** - Excel file handling
- **[Plyer](https://github.com/kivy/plyer)** - Cross-platform notifications
- **[Playwright-Stealth](https://github.com/AtuboDad/playwright_stealth)** - Anti-detection plugin

### Inspiration

Built to demonstrate:
- Modern async Python patterns
- Thread-safe GUI development
- Professional software architecture
- Ethical web scraping practices

## 📄 License

**Educational Use Only**

This project is provided as-is for educational and research purposes. The authors are not responsible for misuse or any violations of third-party terms of service.

**MIT License** - See LICENSE file for details.

---

## 🚀 Quick Command Reference

```powershell
# Setup
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium

# Run
python main.py

# Update
pip install -r requirements.txt --upgrade
playwright install chromium --force

# Validate
python validate_structure.py

# Enable Notifications
pip install plyer

# Debug
# Edit config/settings.json: "log_level": "DEBUG"
```

---

**Made with ❤️ for learning and research**

**Version 3.0** | **Last Updated:** October 2025

---

## ⭐ Star This Project

If you found this useful, consider giving it a star! It helps others find the project.

---

**Happy Scraping! �️✨**

*Remember: Scrape responsibly and ethically. Respect website terms of service and rate limits.*
