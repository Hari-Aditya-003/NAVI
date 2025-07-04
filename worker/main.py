import asyncio
from core.utils import parse_arguments
from mvp import service
from notifier import send_whatsapp_alert  # ✅ NEW

if __name__ == "__main__":
    args = parse_arguments()
    while True:
        jobs = asyncio.run(
            service(
                worker_num=args.workers,
                is_popular=args.popular,
                headless=args.headless
            )
        )

        # ✅ NEW: send job alerts to WhatsApp
        if jobs:
            for job in jobs:
                try:
                    message = f"📢 New Job:\n{job.get('title')}\n{job.get('link')}"
                    send_whatsapp_alert(message)
                except Exception as e:
                    print(f"❌ Error while sending alert: {e}")