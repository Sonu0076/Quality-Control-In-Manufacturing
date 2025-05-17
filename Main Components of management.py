class QualityPlanning:
    def _init_(self, requirements):
        self.requirements = requirements

    def define_quality_goals(self):
        print("Defining quality goals based on requirements...")
        for req in self.requirements:
            print(f"Goal: Ensure '{req}' is met.")

class QualityControl:
    def _init_(self, product_data):
        self.product_data = product_data

    def inspect_products(self):
        print("\nPerforming quality control inspection...")
        for i, product in enumerate(self.product_data):
            status = "PASS" if product['quality'] >= 80 else "FAIL"
            print(f"Product {i+1}: Quality = {product['quality']} -> {status}")

class QualityAssurance:
    def _init_(self, processes):
        self.processes = processes

    def audit_processes(self):
        print("\nAuditing processes for compliance...")
        for name, compliant in self.processes.items():
            result = "Compliant" if compliant else "Non-compliant"
            print(f"Process '{name}': {result}")

class QualityImprovement:
    def _init_(self, feedback):
        self.feedback = feedback

    def analyze_feedback(self):
        print("\nAnalyzing customer feedback for improvements...")
        for issue in self.feedback:
            print(f"Issue reported: {issue} -> Action: Investigate and resolve.")

# Example usage

# Step 1: Quality Planning
requirements = ["Product durability", "Customer satisfaction", "Regulatory compliance"]
planner = QualityPlanning(requirements)
planner.define_quality_goals()

# Step 2: Quality Control
sample_products = [{'quality': 85}, {'quality': 75}, {'quality': 90}]
qc = QualityControl(sample_products)
qc.inspect_products()

# Step 3: Quality Assurance
process_compliance = {"Manufacturing": True, "Packaging": False, "Logistics": True}
qa = QualityAssurance(process_compliance)
qa.audit_processes()

# Step 4: Quality Improvement
customer_feedback = ["Late delivery", "Defective packaging"]
qi = QualityImprovement(customer_feedback)
qi.analyze_feedback()