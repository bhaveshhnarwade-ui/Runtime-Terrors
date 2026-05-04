# How to Change Server Location

## Quick Guide (Just 3 Steps!)

### Step 1: Get Your GPS Coordinates
1. Open **Google Maps**
2. Right-click on your shop location
3. Copy the coordinates (format: `19.XXXX, 72.XXXX`)

### Step 2: Update config.py
Open `config.py` and find this section:

```python
# ── Restaurant / Server Location ──────────────────────────────────────────
# Current: 7-Eleven, Thane West, Maharashtra, India
SERVER_LAT = 19.2183   # ← ALWAYS update this with your shop's latitude
SERVER_LNG = 72.9781   # ← ALWAYS update this with your shop's longitude
```

**Replace the numbers** with your shop's coordinates:
- `SERVER_LAT` = latitude number
- `SERVER_LNG` = longitude number

**Also update the comment** so you remember where this is:
```python
# Current: Your Shop Name, Your City, State
```

### Step 3: Restart the Server
- Stop the Flask server (Ctrl+C in terminal)
- Run it again: `python App.py`
- That's it! 🎉

---

## Delivery Settings (Already Updated)

The website is now configured as follows:

| Setting | Value | What it means |
|---------|-------|---------------|
| **Max Delivery Distance** | 40 km | Orders beyond 40 km are rejected |
| **Free Delivery** | Up to 15 km | No charge for orders within 15 km |
| **Extra Charge** | ₹30/km | For each km beyond 15 km, add ₹30 |

### Example: How Charges Work
- Order from 10 km away → **Free** ✅
- Order from 15 km away → **Free** ✅
- Order from 20 km away → (20-15) × 30 = **₹150** 💰
- Order from 35 km away → (35-15) × 30 = **₹600** 💰
- Order from 50 km away → **Rejected** ❌ (exceeds 40 km limit)

---

## ⚠️ Important Reminders

1. **Always update the comment** with the new location name
2. **Always restart the server** after changes
3. **Check app.js loading** - the charges will automatically display on the receipt
4. **Test locally first** - order from your phone to verify charges and location

---

## Still Having Issues?

If outdated information appears:
- Restart your browser completely (close and reopen)
- Clear browser cache (Ctrl+Shift+Del)
- Make sure the server restarted after your changes
