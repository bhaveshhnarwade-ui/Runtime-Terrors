# Deploy to Render Using GitHub

## Step 1: Push Code to GitHub

### 1.1 Create a GitHub Repository
1. Go to **https://github.com/new**
2. Repository name: `gourmet-bites` (or any name you like)
3. Description: `Luxury Food Delivery App`
4. Choose **Public** (easier for Render integration)
5. Click **Create repository**
6. **Copy the HTTPS URL** (looks like: `https://github.com/YOUR-USERNAME/gourmet-bites.git`)

### 1.2 Push Your Code to GitHub

Open PowerShell in the Menu folder and run:

```powershell
cd "c:\Users\user\OneDrive\Desktop\test\Menu"

# Configure Git (do this once)
git config user.name "Your Name"
git config user.email "your-email@example.com"

# Check git status
git status

# Add all files
git add .

# Commit
git commit -m "Initial commit: Gourmet Bites app with Thane delivery"

# Push to GitHub (paste your repository URL)
git remote add origin https://github.com/YOUR-USERNAME/gourmet-bites.git
git branch -M main
git push -u origin main
```

**Replace:**
- `YOUR-USERNAME` with your GitHub username
- `gourmet-bites` with your repo name if different

---

## Step 2: Deploy on Render

### 2.1 Connect GitHub to Render
1. Go to **https://render.com**
2. Click **Sign Up** → Choose **GitHub** → Authorize
3. You'll see your repositories listed

### 2.2 Create Web Service
1. Click **New +** → **Web Service**
2. Select your repository (`gourmet-bites`)
3. Click **Connect**

### 2.3 Configure Render Settings

**Fill in these fields:**

| Field | Value |
|-------|-------|
| **Name** | `gourmet-bites` (or any name) |
| **Environment** | `Python 3` |
| **Region** | `Singapore` (or closest to you) |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn App:app` |

### 2.4 Environment Variables (Optional but Recommended)

Click **Advanced** → **Add Environment Variable**

```
FLASK_ENV=production
```

### 2.5 Deploy!
1. Click **Create Web Service**
2. Wait 2-5 minutes for deployment
3. You'll see logs showing build progress
4. Once done, you'll get a URL like: `https://gourmet-bites-xxxx.onrender.com`

---

## Step 3: Test Your Deployment

1. **Open your Render URL** in browser
2. Enter your name and start ordering
3. **Test delivery** from a location in Thane:
   - Should show free delivery (≤15 km)
   - Should show ₹30/km charge for >15 km
   - Should reject orders >40 km

---

## Common Issues & Fixes

### ❌ Build Failed: "No module named 'flask'"
**Fix:** Requirements not installed properly
```
Check: Build Command = `pip install -r requirements.txt`
```

### ❌ App crashes on Render
**Check logs:**
1. Go to Render dashboard
2. Click your service
3. Check **Logs** tab
4. Fix any errors in App.py

### ❌ Database error on first load
**This is normal!** The app creates `menu.db` automatically on first run.
- Just refresh the page
- If it still fails, check logs for Python errors

### ❌ Location services not working
**Render uses HTTPS automatically** ✅ (browser requires this for geolocation)
- Works perfectly on Render
- Test by allowing location permission

---

## Step 4: Change Location Later (For Future)

**On Render, to change location:**

1. Edit `config.py` locally:
   ```python
   SERVER_LAT = 19.XXXX  # New latitude
   SERVER_LNG = 72.XXXX  # New longitude
   ```

2. Commit and push to GitHub:
   ```powershell
   git add config.py
   git commit -m "Update location to new shop"
   git push
   ```

3. **Render auto-redeploys** when you push! (takes 1-2 minutes)

---

## Files Created for Deployment

These files were created/updated for Render compatibility:

- ✅ **Procfile** - Tells Render how to run the app
- ✅ **.gitignore** - Prevents pushing unnecessary files
- ✅ **requirements.txt** - Lists all dependencies
- ✅ **App.py** - Updated for production

---

## Deployment Checklist

- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Logged in to Render with GitHub
- [ ] Created Web Service on Render
- [ ] Set Build & Start commands correctly
- [ ] Deployed successfully
- [ ] Tested on https://your-app-name.onrender.com
- [ ] Verified delivery charges work
- [ ] Verified geolocation works

---

## Your Deployed App URL

Once deployed, your app will be live at:
```
https://your-app-name.onrender.com
```

**Share this with:**
- College demo judges
- Your team
- Test users for feedback

---

## Support

If you get stuck:
1. Check Render **Logs** (tab in dashboard)
2. Check **App.py errors** (Python syntax)
3. Check **requirements.txt** is complete
4. Make sure Procfile is spelled correctly

All set! 🚀
