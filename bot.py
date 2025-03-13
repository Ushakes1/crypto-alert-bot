import requests
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

# Binance API
BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"

# List of favorite cryptocurrencies to track
FAVORITE_CRYPTO = [
    "DOGEUSDT", "POPCATUSDT", "TRXUSDT", "SUIUSDT", "AVAXUSDT", "BNBUSDT", "BTCUSDT", 
    "ETHUSDT", "SOLUSDT", "XRPUSDT", "TRUMPUSDT", "ALGOUSDT", "VETUSDT", "RAYUSDT", 
    "ADAUSDT", "FLOKIUSDT", "SHIBUSDT", "WIFUSDT"
]

# Price drop threshold (modify as needed)
PRICE_DROP_THRESHOLD = 5  # Alert if price drops more than 5%

# Email configuration
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_RECEIVER = "ash335728@gmail.com"
EMAIL_PASSWORD = "Rudransh2019"  # Use App Password if using Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Twilio WhatsApp configuration
TWILIO_ACCOUNT_SID = "ACdf08a3961e214b4f9457c66133733e0d"
TWILIO_AUTH_TOKEN = "f74faf8f59224ec93fa6934547a637f9"
WHATSAPP_NUMBER = "+918288826334"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"

def send_email(subject, message):
    """Send email alert."""
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        print("Email alert sent!")

    except Exception as e:
        print("Failed to send email:", e)

def send_whatsapp_alert(message):
    """Send WhatsApp alert using Twilio."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=WHATSAPP_NUMBER
        )
        print("WhatsApp alert sent!")

    except Exception as e:
        print("Failed to send WhatsApp alert:", e)

def get_crypto_prices():
    """Fetches latest prices and sends alerts if price drops significantly."""
    try:
        response = requests.get(BINANCE_API_URL)  # Indented
        data = response.json()  # Indented
    except Exception as e:
       print("Error fetching crypto prices:", e)
       data = {}  # Avoid crash
    except Exception as e:
       print("Error fetching crypto prices:", e)
       data = {}  # Return empty data to prevent crashing

if not isinstance(data, list):
    print("Unexpected API response:", data)
    return

alerts = []
for crypto in data:
    try:
        symbol = crypto.get("symbol", "UNKNOWN")
        price = float(crypto.get("price", 0))
        if symbol in FAVORITE_CRYPTO:
            alerts.append(f"{symbol}: ${price}")
    except Exception as e:
        print(f"Error processing crypto data: {e}")

message = "\n".join(alerts)
print("Latest Crypto Prices:\n", message)
# Send alerts
   send_email("Crypto Price Alert", message)
   send_whatsapp_alert(message)

except Exception as e:
         print("Error fetching crypto prices:", e)

if __name__ == "__main__":
    get_crypto_prices()
