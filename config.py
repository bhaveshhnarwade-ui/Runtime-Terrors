# ═══════════════════════════════════════════════════════════════════════════
#   DELIVERY CONFIGURATION  — Edit this file to change server location
# ═══════════════════════════════════════════════════════════════════════════
#
#  📍 HOW TO CHANGE LOCATION (ALWAYS DO THIS):
#  1. Open config.py
#  2. Find the "Restaurant / Server Location" section below
#  3. Go to Google Maps → right-click your shop location → copy the coordinates
#  4. Update SERVER_LAT and SERVER_LNG with EXACTLY those numbers
#  5. Update the "Current Location" comment to match
#  6. Save the file
#  7. Restart the Flask server (stop and run again)
#
#  ⚠️ IMPORTANT: Keep comments updated to avoid confusion!
#
# ═══════════════════════════════════════════════════════════════════════════
import os

# ── Restaurant / Server Location ──────────────────────────────────────────
# Current: 7-Eleven, Thane West, Maharashtra, India
SERVER_LAT = 19.2183   # ← ALWAYS update this with your shop's latitude
SERVER_LNG = 72.9781   # ← ALWAYS update this with your shop's longitude

# ── Delivery Limits ───────────────────────────────────────────────────────
MAX_DELIVERY_KM = 40         # Orders beyond 40 km are rejected

# ── Delivery Charges (in ₹) ───────────────────────────────────────────────
BASE_DELIVERY_CHARGE    = 0  # Free delivery up to VARIABLE_CHARGE_THRESHOLD
VARIABLE_CHARGE_THRESHOLD = 15  # Apply variable charges after 15 km
VARIABLE_CHARGE_PER_KM  = 30    # ₹30 per km beyond VARIABLE_CHARGE_THRESHOLD

# ── Time Components (minutes) ─────────────────────────────────────────────
FIXED_PREP_TIME  = 20       # Kitchen preparation time
TRAVEL_PER_KM    = 3        # 3 min/km  →  ~20 km/h average city speed
HANDOFF_BUFFER   = 5        # Driver finding house / parking

# ── Database Configuration ────────────────────────────────────────────────
# For local development, uses SQLite
# For production (Render), uses PostgreSQL via DATABASE_URL environment variable
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///menu.db')
# Handle Render's postgres:// → postgresql:// scheme change
if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
