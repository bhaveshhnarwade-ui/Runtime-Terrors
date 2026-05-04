# Deployment & Setup Guide

## ✅ What's Been Updated

Your website now has:
- ✅ Server location set to **7-Eleven, Thane West** (19.2183°, 72.9781°)
- ✅ Max delivery range: **40 km**
- ✅ **Free delivery** up to 15 km
- ✅ **₹30/km charge** for distances beyond 15 km
- ✅ Delivery charges displayed on receipt

---

## How to Deploy Locally (For Testing)

### Step 1: Install Requirements
```bash
cd "c:\Users\user\OneDrive\Desktop\test\Menu"
pip install -r requirements.txt
```

### Step 2: Start the Server
```bash
python App.py
```

You'll see:
```
* Running on http://127.0.0.1:5000
```

### Step 3: Open in Browser
Click: **http://127.0.0.1:5000**

### Step 4: Test the App
1. Enter your name
2. Click "Begin Ordering"
3. Allow location access when prompted
4. Add items to cart
5. Proceed to checkout
6. You'll see the delivery charge calculated!

---

## How to Deploy to Production

### Option 1: Using Heroku (Easiest for Beginners)

1. **Install Heroku CLI** from https://devcenter.heroku.com/articles/heroku-cli

2. **Create a Procfile** in the Menu folder:
```
web: gunicorn App:app
```

3. **Add gunicorn to requirements.txt**:
```bash
echo "gunicorn" >> requirements.txt
```

4. **Login to Heroku**:
```bash
heroku login
```

5. **Deploy**:
```bash
heroku create your-app-name
git push heroku main
```

Your site will be live at: `https://your-app-name.herokuapp.com`

### Option 2: Using AWS (More Professional)

1. Create an EC2 instance
2. SSH into the instance
3. Install Python and dependencies
4. Upload your code
5. Run with Gunicorn/Nginx

### Option 3: Using PythonAnywhere (Fastest)

1. Go to https://www.pythonanywhere.com
2. Upload your files
3. Configure Flask app in Web tab
4. Website is live!

---

## Testing Before Deployment

✅ **Run these checks**:

```bash
# Check all imports work
python -c "from config import *; print('✅ Config loaded')"

# Check Flask loads
python -c "from App import app; print('✅ Flask app created')"

# Start server and test
python App.py
# Open browser to http://127.0.0.1:5000
```

---

## Troubleshooting

### "Module not found" error?
```bash
pip install -r requirements.txt
```

### Server not starting?
```bash
# Check if port 5000 is in use
netstat -ano | findstr :5000
# If in use, change port in App.py:
# app.run(debug=True, port=5001)
```

### Location not working?
- Must use **HTTPS** in production (browsers block geolocation on HTTP)
- User must **allow location permission**
- Test with phone location services enabled

### Delivery charges not showing?
- Hard refresh browser: **Ctrl+Shift+R**
- Clear browser cache
- Restart Flask server
- Check browser console for errors (F12)

---

## File Structure

```
Menu/
├── App.py                 ← Main Flask application
├── config.py             ← SERVER LOCATION & DELIVERY SETTINGS (Edit this!)
├── menu.db              ← Database (auto-created)
├── requirements.txt     ← Python dependencies
├── LOCATION_GUIDE.md    ← How to change location (YOU NEED THIS!)
├── templates/
│   ├── index.html
│   └── walkthrough.html
└── static/
    ├── app.js           ← Frontend logic
    ├── p.css            ← Styling
    └── images/
```

---

## Key Files to Remember

| File | Purpose | Edit When? |
|------|---------|-----------|
| **config.py** | Location, delivery limits, charges | Changing shop location or delivery settings |
| **App.py** | Flask backend | Adding new features |
| **static/app.js** | Frontend logic | Changing how page looks/behaves |
| **templates/index.html** | HTML structure | Changing page layout |

---

## Next Steps

1. ✅ You've set location to Thane 7-Eleven
2. ✅ You've enabled tiered delivery charges
3. 👉 **Read LOCATION_GUIDE.md** to learn how to change location anytime
4. 👉 Test locally before going live
5. 👉 Deploy using one of the options above

---

**Need help?** Check the console output (F12) for errors!
