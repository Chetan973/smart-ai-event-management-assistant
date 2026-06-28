"""
Application Configuration

This module is responsible for:

1. Loading environment variables
2. Centralizing application configuration
3. Preventing hardcoded secrets

sqlite:///event_management.db
"""

from pathlib import Path

from dotenv import load_dotenv
import os

# ----------------------------------------------------
# Load Environment Variables
# ----------------------------------------------------

load_dotenv()

# ----------------------------------------------------
# Project Root Directory
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------------------
# Application Information
# ----------------------------------------------------

APP_NAME = "Smart AI Event Management Assistant"

APP_VERSION = "1.0.0"

# ----------------------------------------------------
# Google Gemini
# ----------------------------------------------------

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ----------------------------------------------------
# Database
# ----------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError(
        "DATABASE_URL not found in .env"
    )
# ----------------------------------------------------
# Email
# ----------------------------------------------------

SMTP_EMAIL = os.getenv("SMTP_EMAIL")

SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# ----------------------------------------------------
# Razorpay
# ----------------------------------------------------

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")

RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")