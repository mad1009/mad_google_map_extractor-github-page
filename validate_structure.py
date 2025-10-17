"""
Project Structure Validator
Verifies all necessary files and directories exist
"""
from pathlib import Path


def validate_structure():
    """Validate project structure"""
    base_dir = Path(__file__).parent
    
    required_items = {
        'files': [
            'main.py',
            'requirements.txt',
            'README.md',
            'QUICKSTART.md',
            '.gitignore',
            '.env',
            'setup.ps1',
            'run.ps1',
            'config/settings.json',
            'config/proxies.txt',
            'src/__init__.py',
            'src/core/__init__.py',
            'src/core/config.py',
            'src/core/worker.py',
            'src/scraper/__init__.py',
            'src/scraper/google_maps.py',
            'src/scraper/stealth.py',
            'src/scraper/proxy_manager.py',
            'src/utils/__init__.py',
            'src/utils/logger.py',
            'src/utils/data_processor.py',
            'src/utils/exporter.py',
            'src/gui/__init__.py',
            'src/gui/main_window.py',
            'src/gui/styles.py',
            'src/gui/components/__init__.py',
        ],
        'directories': [
            'src',
            'src/core',
            'src/scraper',
            'src/utils',
            'src/gui',
            'src/gui/components',
            'config',
            'output',
            'logs',
        ]
    }
    
    print("🔍 Validating Project Structure...\n")
    
    all_valid = True
    
    # Check directories
    print("📁 Checking directories...")
    for directory in required_items['directories']:
        dir_path = base_dir / directory
        if dir_path.exists():
            print(f"  ✓ {directory}")
        else:
            print(f"  ✗ {directory} - MISSING")
            all_valid = False
    
    print()
    
    # Check files
    print("📄 Checking files...")
    for file in required_items['files']:
        file_path = base_dir / file
        if file_path.exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - MISSING")
            all_valid = False
    
    print("\n" + "="*50)
    
    if all_valid:
        print("✅ Project structure is complete!")
        print("\nNext steps:")
        print("  1. Run: .\\setup.ps1")
        print("  2. Run: .\\run.ps1")
    else:
        print("❌ Some files or directories are missing!")
        print("Please ensure all files are properly created.")
    
    print("="*50)
    
    return all_valid


if __name__ == "__main__":
    validate_structure()
