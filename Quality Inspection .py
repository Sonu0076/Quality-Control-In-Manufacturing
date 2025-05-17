class Product:
    def _init_(self, product_id, weight):
        self.product_id = product_id
        self.weight = weight
        self.status = "Unchecked"

class QualityInspector:
    def _init_(self, min_weight, max_weight):
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.passed = []
        self.failed = []

    def inspect(self, product):
        if self.min_weight <= product.weight <= self.max_weight:
            product.status = "Pass"
            self.passed.append(product)
        else:
            product.status = "Fail"
            self.failed.append(product)

    def report(self):
        print("Quality Inspection Report")
        print("========================")
        print(f"Total Products Inspected: {len(self.passed) + len(self.failed)}")
        print(f"Passed: {len(self.passed)}")
        print(f"Failed: {len(self.failed)}")
        print("\nFailed Items:")
        for item in self.failed:
            print(f"  - ID: {item.product_id}, Weight: {item.weight}, Status: {item.status}")

# Sample usage
if _name_ == "_main_":
    # Define acceptable weight range
    inspector = QualityInspector(min_weight=9.5, max_weight=10.5)

    # Sample products (in real-world, these might come from sensors or a CSV file)
    products = [
        Product(product_id="P001", weight=10.0),
        Product(product_id="P002", weight=10.7),
        Product(product_id="P003", weight=9.3),
        Product(product_id="P004", weight=10.2),
    ]

    # Inspect all products
    for p in products:
        inspector.inspect(p)

    # Generate report
    inspector.report()