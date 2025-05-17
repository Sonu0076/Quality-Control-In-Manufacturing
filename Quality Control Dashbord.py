import datetime

class QualityInspectionDashboard:
    def _init_(self):
        self.records = []

    def log_inspection(self):
        print("\n--- New Quality Inspection ---")
        product_id = input("Enter Product ID: ")
        inspector = input("Inspector Name: ")
        dimension = float(input("Measured Dimension (mm): "))
        appearance = input("Appearance OK? (yes/no): ").strip().lower()
        functionality = input("Functional Test Passed? (yes/no): ").strip().lower()
        defect = input("Defect Type (if any, else 'none'): ")

        status = "PASS"
        if dimension < 9.5 or dimension > 10.5 or appearance != "yes" or functionality != "yes":
            status = "FAIL"

        record = {
            "timestamp": datetime.datetime.now(),
            "product_id": product_id,
            "inspector": inspector,
            "dimension": dimension,
            "appearance": appearance,
            "functionality": functionality,
            "defect": defect,
            "status": status
        }

        self.records.append(record)
        print(f"Inspection Status: {status}")

    def generate_report(self):
        print("\n--- Inspection Report ---")
        for record in self.records:
            print(f"\nProduct ID: {record['product_id']}")
            print(f"Inspector: {record['inspector']}")
            print(f"Time: {record['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Dimension: {record['dimension']} mm")
            print(f"Appearance: {record['appearance']}")
            print(f"Functionality: {record['functionality']}")
            print(f"Defect: {record['defect']}")
            print(f"Status: {record['status']}")
            print("-" * 30)

# Simulate dashboard usage
dashboard = QualityInspectionDashboard()

while True:
    print("\n--- Digital Quality Inspection Dashboard ---")
    print("1. Log New Inspection")
    print("2. Generate Report")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        dashboard.log_inspection()
    elif choice == "2":
        dashboard.generate_report()
    elif choice == "3":
        print("Exiting dashboard. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")