# 💖 Donation Button Setup Guide

## Overview

The Google Maps Scraper includes a beautiful, integrated donation button in the GUI. This guide will help you configure it with your preferred donation platform.

## 🎨 Design Features

The donation button includes:
- **Eye-catching orange gradient** design (Coffee-themed colors)
- **Hover effects** for better UX
- **Friendly messaging** that doesn't feel pushy
- **Easy customization** via JSON config
- **Multiple platform support** (Buy Me a Coffee, PayPal, Ko-fi, etc.)

## 📍 Location

The donation button appears at the bottom of the left panel in the GUI:
```
┌─────────────────┐
│  🗺️ Scraper     │
│  ───────────    │
│  [Queries...]   │
│  [Settings...]  │
│  [▶ Start]      │
│  [⏹ Stop]       │
│  ─────────────  │
│  💖 Enjoying    │
│  this tool?     │
│  ☕ Buy Me a    │
│     Coffee      │
│  Your support   │
│  helps!         │
└─────────────────┘
```

## ⚙️ Configuration

### Step 1: Choose Your Platform

Edit `config/donation.json`:

```json
{
  "donation": {
    "enabled": true,
    "platform": "buymeacoffee",  // Change this
    "username": "yourusername",   // Change this
    "custom_url": null,
    "message": "Your support helps keep this project alive! 🚀"
  }
}
```

### Step 2: Supported Platforms

| Platform | Value | URL Format |
|----------|-------|------------|
| **Buy Me a Coffee** | `buymeacoffee` | `https://buymeacoffee.com/{username}` |
| **PayPal** | `paypal` | `https://paypal.me/{username}` |
| **Ko-fi** | `kofi` | `https://ko-fi.com/{username}` |
| **GitHub Sponsors** | `github` | `https://github.com/sponsors/{username}` |
| **Patreon** | `patreon` | `https://patreon.com/{username}` |
| **Custom URL** | `custom` | Uses `custom_url` field |

### Step 3: Examples

#### Buy Me a Coffee (Recommended)
```json
{
  "donation": {
    "enabled": true,
    "platform": "buymeacoffee",
    "username": "johndoe",
    "custom_url": null,
    "message": "Your support helps keep this project alive! 🚀"
  }
}
```
**Result:** `https://buymeacoffee.com/johndoe`

#### PayPal
```json
{
  "donation": {
    "enabled": true,
    "platform": "paypal",
    "username": "johndoe",
    "custom_url": null,
    "message": "Every donation helps improve this tool! 💖"
  }
}
```
**Result:** `https://paypal.me/johndoe`

#### GitHub Sponsors
```json
{
  "donation": {
    "enabled": true,
    "platform": "github",
    "username": "johndoe",
    "custom_url": null,
    "message": "Sponsor this open-source project! 🌟"
  }
}
```
**Result:** `https://github.com/sponsors/johndoe`

#### Custom URL (Any Platform)
```json
{
  "donation": {
    "enabled": true,
    "platform": "custom",
    "username": "",
    "custom_url": "https://donate.stripe.com/your_custom_link",
    "message": "Support via Stripe! 💳"
  }
}
```
**Result:** Uses your custom URL directly

### Step 4: Disable Donations (Optional)

To hide the donation button:
```json
{
  "donation": {
    "enabled": false,
    ...
  }
}
```

## 🎨 Customizing Appearance

### Change Button Colors

Edit `src/gui/main_window.py` (line ~189):

```python
self.donate_btn = ctk.CTkButton(
    donate_frame,
    text="☕ Buy Me a Coffee",
    command=self.open_donate_link,
    font=("Segoe UI", 13, "bold"),
    height=36,
    fg_color=("#FF813F", "#FF6B35"),      # Change these colors
    hover_color=("#FF6B35", "#FF5722"),   # Change these colors
    corner_radius=8,
    border_width=0
)
```

### Popular Color Schemes

#### Blue (PayPal style)
```python
fg_color=("#0070BA", "#003087"),
hover_color=("#003087", "#001C64"),
```

#### Purple (Twitch/Ko-fi style)
```python
fg_color=("#9146FF", "#772CE8"),
hover_color=("#772CE8", "#5A1EA6"),
```

#### Green (Money/Success)
```python
fg_color=("#10B981", "#059669"),
hover_color=("#059669", "#047857"),
```

#### Pink (Heart theme)
```python
fg_color=("#EC4899", "#DB2777"),
hover_color=("#DB2777", "#BE185D"),
```

### Change Button Text

Edit line ~187:
```python
text="☕ Buy Me a Coffee",  # Change this
```

Examples:
- `"💖 Support This Project"`
- `"🎁 Donate"`
- `"⭐ Sponsor Me"`
- `"💰 Tip the Developer"`
- `"☕ Coffee Fund"`

### Change Message Text

Edit line ~198:
```python
thank_label = ctk.CTkLabel(
    donate_frame,
    text="Your support helps keep this project alive! 🚀",  # Change this
    ...
)
```

## 📱 Testing

1. **Update config:**
   ```json
   {
     "donation": {
       "platform": "buymeacoffee",
       "username": "test"
     }
   }
   ```

2. **Run the app:**
   ```powershell
   python main.py
   ```

3. **Click the donate button** - should open: `https://buymeacoffee.com/test`

4. **Check logs** - should see: `"💖 Thank you for considering a donation!"`

## 🚀 Distribution

When distributing the executable:

1. **Include donation.json** in the package
2. **Users can modify** their own donation settings
3. **Or hardcode** values in the code for permanent configuration

### Hardcoding (Permanent Setup)

If you don't want a config file, replace the `open_donate_link` method:

```python
def open_donate_link(self):
    """Open donation link in browser"""
    # Hardcoded donation URL
    donation_url = "https://buymeacoffee.com/yourusername"
    
    try:
        webbrowser.open(donation_url)
        self.logger.info("💖 Thank you for considering a donation!")
    except Exception as e:
        self.logger.error(f"Failed to open donation link: {e}")
```

## 🎁 Best Practices

### 1. **Don't Be Pushy**
- Keep messaging friendly and grateful
- Use positive emojis (💖 ☕ 🚀)
- Thank users, don't guilt them

### 2. **Make It Optional**
- Easy to close/ignore
- No popups or interruptions
- Subtle but visible placement

### 3. **Show Value**
- Mention what donations support
- Examples:
  - "Helps keep servers running"
  - "Supports future updates"
  - "Funds development time"

### 4. **Multiple Options**
- Consider supporting multiple platforms
- Some users prefer PayPal, others prefer Ko-fi
- Add a dropdown menu if desired

## 📊 Analytics (Optional)

Track donation button clicks:

```python
def open_donate_link(self):
    """Open donation link in browser"""
    try:
        # Track analytics (optional)
        self.logger.info(f"Donation button clicked at {datetime.now()}")
        
        # Your existing code...
        donation_url = "..."
        webbrowser.open(donation_url)
        
    except Exception as e:
        self.logger.error(f"Failed to open donation link: {e}")
```

## 🔧 Advanced: Multiple Platforms

To support multiple donation platforms with a dropdown:

```python
# In _create_left_panel, replace donate button with:

platform_var = ctk.StringVar(value="Buy Me a Coffee ☕")
platform_menu = ctk.CTkOptionMenu(
    donate_frame,
    variable=platform_var,
    values=["Buy Me a Coffee ☕", "PayPal 💳", "GitHub Sponsors ⭐"],
    command=self.open_selected_donation,
    font=FONTS['small']
)
platform_menu.pack(fill="x", pady=2)

# Add method:
def open_selected_donation(self, choice):
    urls = {
        "Buy Me a Coffee ☕": "https://buymeacoffee.com/yourusername",
        "PayPal 💳": "https://paypal.me/yourusername",
        "GitHub Sponsors ⭐": "https://github.com/sponsors/yourusername"
    }
    webbrowser.open(urls.get(choice, urls["Buy Me a Coffee ☕"]))
```

## 📸 Screenshot

The button looks like this:

```
╔════════════════════════════╗
║                            ║
║   💖 Enjoying this tool?   ║
║                            ║
║  ┌────────────────────┐   ║
║  │ ☕ Buy Me a Coffee │   ║  ← Orange gradient
║  └────────────────────┘   ║
║                            ║
║  Your support helps keep   ║
║  this project alive! 🚀    ║
║                            ║
╚════════════════════════════╝
```

## 🎉 You're All Set!

Your donation button is now ready to receive support from grateful users! 💖

---

**Questions?** Check the main README.md or create an issue on GitHub.
