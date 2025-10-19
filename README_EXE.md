# Google Maps Scraper - Executable Build Guide

## 📦 Building the Executable

### Requirements
- Python 3.13+ with virtual environment activated
- Playwright browsers installed: `playwright install chromium`
- All dependencies installed: `pip install -r requirements.txt`

### Build Process

1. **Activate Virtual Environment**
   ```powershell
   .\env\Scripts\Activate.ps1
   ```

2. **Build the Executable**
   ```powershell
   .\build_exe.ps1
   ```
   Or manually:
   ```powershell
   pyinstaller build_exe.spec --noconfirm
   ```

### Build Output

**Location:** `dist\GoogleMapsScraper\`

**Contents:**
- `GoogleMapsScraper.exe` - Main executable (11.32 MB)
- `_internal\` - Dependencies and bundled browsers (~746 MB total)
  - `playwright_browsers\` - Bundled Chromium browsers
    - `chromium-1187` - Regular Chromium browser (~300 MB)
    - `chromium_headless_shell-1187` - Headless shell (~100 MB)  
    - `ffmpeg-1011` - Media encoding (~5 MB)
    - `winldd-1007` - Windows linker (~1 MB)

**Total Package Size:** ~746 MB (uncompressed)

### Distribution

To distribute the application:

1. **Compress the folder:**
   ```powershell
   Compress-Archive -Path dist\GoogleMapsScraper -DestinationPath GoogleMapsScraper.zip
   ```
   Compressed size: ~200-300 MB

2. **Share the ZIP file** with users

3. **User Setup:**
   - Extract the ZIP file
   - Run `GoogleMapsScraper.exe`
   - No installation or internet connection required!

## 🎯 Key Features

✅ **Fully Standalone** - No Python installation needed  
✅ **Browser Bundled** - No need to run `playwright install`  
✅ **Offline Ready** - Works without internet (after extraction)  
✅ **Custom Icon** - Professional map pin icon  
✅ **No Setup** - Just extract and run

## 🔧 Technical Details

### Bundled Components

1. **Python Runtime** - Embedded Python 3.13
2. **Dependencies** - All Python packages (NumPy, Pandas, Playwright, etc.)
3. **Chromium Browser** - Full browser with headless shell
4. **FFmpeg** - For media processing
5. **Application Code** - All source files compiled

### Build Configuration

The build process:
- Uses PyInstaller 6.11.1 with custom spec file
- Bundles CustomTkinter assets
- Includes all Playwright browsers from `%LOCALAPPDATA%\ms-playwright`
- Sets `PLAYWRIGHT_BROWSERS_PATH` environment variable at runtime
- Collects NumPy and Pandas with binary dependencies
- Applies custom numpy runtime hook for path resolution

### Environment Variables

When running from the executable:
```python
PLAYWRIGHT_BROWSERS_PATH = <exe_dir>\_internal\playwright_browsers
```

This tells Playwright to use the bundled browsers instead of looking in the default location.

## ⚠️ Known Issues

1. **Large Package Size** (~746 MB)
   - Due to bundling full Chromium browser
   - Compressed ZIP: ~200-300 MB
   - Alternative: Could create installer that downloads browser on first run

2. **Build Time** (~2-3 minutes)
   - Copying large browser files takes time
   - Normal for this type of bundling

3. **Windows Only**
   - Current build is Windows-specific
   - Would need separate builds for Mac/Linux

## 🚀 Quick Test

After building, test the executable:

```powershell
cd dist\GoogleMapsScraper
.\GoogleMapsScraper.exe
```

The app should:
1. Launch the GUI immediately
2. Show no browser installation prompts
3. Successfully scrape Google Maps when you run a search
4. Create logs in `_internal\logs\`

## 📝 Build Modifications

To modify the build:

1. **Edit `build_exe.spec`** for PyInstaller configuration
2. **Update `main.py`** to change browser path logic
3. **Modify `create_icon.py`** to change the icon design

## 🎨 Icon

The application uses a custom map pin icon created by `create_icon.py`:
- 256x256 resolution
- Red pin with white dot
- Saved as `assets/icon.ico`

To regenerate:
```powershell
python create_icon.py
```

## 📊 Performance

**First Launch:**
- Instant launch (no browser download)
- Normal Chromium startup time

**Scraping Performance:**
- Same as non-bundled version
- Uses bundled Chromium browser
- No performance penalty

## 🆘 Troubleshooting

### "Executable doesn't exist" error

If you see:
```
BrowserType.launch: Executable doesn't exist at ...
```

**Solution:** Rebuild with updated `build_exe.spec` that bundles all browser components.

### Build fails with "Permission denied"

**Solution:** 
1. Close any running instances of `GoogleMapsScraper.exe`
2. Use: `taskkill /F /IM GoogleMapsScraper.exe`
3. Rebuild

### Large size concerns

**Options:**
1. Accept the size (most reliable)
2. Create installer that downloads browser on first run (smaller but needs internet)
3. Use UPX compression (may trigger antivirus)

## 📜 License

Same as main project - see parent README.md
