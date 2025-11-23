# Problem Statement
The manual or fragmented management processes currently used by small to medium-sized pet shops lead to significant operational inefficiencies, including inaccurate inventory counts, difficulties in tracking specialized costs (like pet nourishment and health checks), and a lack of standardized financial reporting. This results in unreliable profit margin calculation and high risk of data inconsistencies due to decentralized data modification. Furthermore, the absence of robust, role-based access control exposes sensitive financial and employee data to unauthorized personnel, posing a serious security risk. The primary problem is the lack of a unified, secure, and resilient system to manage the complete lifecycle of pet shop operations.

# Scope of the Project
The scope of the Pet Shop Management System (PSMS) is strictly limited to the console-based management of internal operations and read-only customer interaction.

- Inclusions: The system includes full employee and pet inventory management, detailed cost tracking, multi-user authentication with strict RBAC, and atomic transaction processing for database reliability.
- Exclusions: The project specifically excludes the development of a Graphical User Interface (GUI) or a web-based interface. It does not handle external payment processing, advanced predictive analytics, or integration with third-party logistics services. All interaction occurs via the command-line console.

# Target Users
The system is designed for three distinct, internal and external user groups, each with tightly controlled access permissions.

- Administrators (Admins): Owners, senior managers, or auditors requiring full system control. Their primary need is accessing sensitive financial reports and performing employee management.
-  Staff: Day-to-day operators responsible for physical inventory, pet health logging, and recording operational expenses. They require read-write access to operational tables but are denied access to profitability data.
- Customers: Individuals browsing the available stock and system information. They are strictly limited to read-only functions for pet availability and general shop information.

# High-Level Features
The system is defined by its core functional pillars: Security, Data Integrity, and Reporting.

- Role-Based Access Control (RBAC): Implementation of a mandatory login system classifying users as Admin, Staff, or Customer, ensuring that permissions are automatically enforced upon successful authentication.
- Atomic Data Modification (modify(t)): A single, centralized function that handles all insert, update, and delete operations across all primary tables, guaranteeing transactional consistency across the database.
- Financial Profit Reporting (prof()): An Admin-exclusive feature that calculates and displays the net profit based on revenue, operational costs, and tracked expenses, providing a clear financial snapshot.
- Real-Time Inventory Management: Tools for Staff to track pet acquisition, sale, health status, and special recurring costs like NourishmentCost.
- Transaction Resilience: All critical, multi-step operations (e.g., selling a pet, which updates inventory and sales records) are wrapped in database transactions to guarantee immediate rollback if any part of the process fails.
