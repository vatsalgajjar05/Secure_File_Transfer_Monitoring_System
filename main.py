import os
import sys
from monitor.file_monitor import start_monitoring
from utils.report_generator import generate_summary




def create_required_directories():
    """
    Ensure required folders exist (like logs directory)
    """
    if not os.path.exists("logs"):
        os.makedirs("logs")
        print("[INFO] Logs directory created.")


def print_banner():
    """
    Display project banner
    """
    print("=" * 60)
    print(" SECURE FILE TRANSFER MONITORING SYSTEM ")
    print("=" * 60)
    print(" Monitoring Started...")
    print(" Press CTRL + C to stop the system.")
    print("=" * 60)


def main():
    try:
        create_required_directories()
        print_banner()
        start_monitoring()

    except KeyboardInterrupt:
        print("\n[INFO] Monitoring stopped by user.")

    except Exception as e:
        print(f"[ERROR] System crashed: {e}")

    finally:
        generate_summary()
        sys.exit(0)


if __name__ == "__main__":
    main()
