def generate_summary():

    total_events = 0
    tampering = 0
    unauthorized = 0

    with open("logs/activity.log", "r") as f:
        for line in f:
            total_events += 1
            if "Integrity Violation" in line:
                tampering += 1
            if "Unauthorized" in line:
                unauthorized += 1

    print("\n========== FINAL AUDIT REPORT ==========")
    print("Total Events:", total_events)
    print("Integrity Violations:", tampering)
    print("Unauthorized Movements:", unauthorized)
    print("========================================")
