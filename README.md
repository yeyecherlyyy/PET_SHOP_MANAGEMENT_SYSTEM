# Pet Shop Management System (PSMS)

## Project Overview
The Pet Shop Management System (PSMS) is a secure, console based application designed to streamline the operations of a small to medium-sized pet shop. Its primary focus is on maintaining accurate inventory, tracking financial performance, and strictly managing user permissions through a robust access control mechanism. 

The system is built on a simple, layered architecture to separate the user interface, business logic, and data access. This structure ensures high reliability and data integrity throughout all operations.

## Key Features
The PSMS includes strict Role Based Access Control (RBAC) to manage three distinct user types, ensuring operational security and data segmentation.

### Role-Based Access & Security
- Admin: Has full, unrestricted access to the entire system, including sensitive financial and employee management features. Admins are the only users who can access profitability reports.
- Staff: Access is limited to day-to-day operational tasks, such as managing inventory, logging pet health checkups, and tracking recurring costs.
- User/Customer: Access is strictly read-only, restricted to browsing available pets, viewing general information, and submitting non-critical feedback.

### Financial and Reporting
The system includes a critical and secured financial function for high-level oversight:

- Profit Calculation (prof()): This highly sensitive function calculates aggregated revenue, various costs (e.g., NourishmentCost), and the net profit. This report is available exclusively to Administrators.

### Inventory Management
The PSMS enforces data consistency through centralized control over all modifications and detailed tracking:

- Centralized Modification (modify(t)): A single, atomic function is used to handle all data updates across various database tables (pets, employees, costs), which is key to ensuring system consistency and preventing data fragmentation.
- Health and Cost Tracking: Staff members are able to log detailed health checkup results (hcheck()) for pets and efficiently track recurring expenses like nourishment costs (ncost()) and veterinary bills.

### Reliability and Atomicity
-Guaranteed Transactions: All multi-step database operations are wrapped in explicit transactions. This guarantees full data rollback in case of any error (such as a network failure or an integrity violation), preventing the storage of partial or corrupted data. This ensures high system resilience.

## Technologies & Tools Used
The application is primarily implemented using Python for its core logic, console interface, and business rules execution. For persistent data storage, the system relies on a reliable MySQL or MariaDB database server.

- Backend/Logic: Python
- Database: MySQL / MariaDB
- Database Connector: A standard Python Database Connector (e.g., pymysql) is used to facilitate secure connections and execute SQL queries.
- Architecture: The design follows a 4-Layered Architecture, providing clear structural separation between Presentation, Business Logic, Data Access, and the Database Layers for enhanced maintainability.

## Installation & Running the Project
To set up and run the PSMS application locally, follow these steps:

### Prerequisites
- Ensure you have Python 3.x installed on your system.
- A running instance of a MySQL-compatible database server is required.
- Install the necessary database connector library, typically using pip install pymysql.

### Setup Steps

Clone the project repository from GitHub and navigate into the project directory.

Database Configuration:
- Create a new database instance named PSMS_DB.
- Run the database initialization script (usually named db_setup.sql) to create all required tables, such as EmployeeList and AvailablePets.
- Update the database connection parameters (host, user, and password) within the project's configuration file.

Run the application by executing the main Python script (python main.py). The application will then launch in your console, prompting you for your login credentials.

## Instructions for Testing
Testing should focus on both the functional modules (user roles) and the non-functional requirements (integrity and resilience).

### A. Functional Testing (Role Verification)
- Admin Check: An Admin must successfully run the prof() financial report and see accurate results.
- Staff Block: A Staff user attempting to execute the Admin-only prof() function must receive an "Access Denied" error and be safely returned to the Staff menu.
- Customer Constraint: A Customer attempting to execute any data update or deletion function must receive a "Read-Only Access" message, and no data changes should occur.

### B. Non-Functional Testing (Integrity & Resilience)

Atomicity Test (Transaction Rollback):
- Identify a transaction that updates two or more related database records.
- During the update process, simulate a failure (e.g., trigger an integrity error by entering invalid data).
- Verification: Check the database to confirm that neither record was updated. The system must have successfully rolled back to the state before the transaction began.

Centralized Modification Test:
- Use the modify(t) function to update multiple, diverse data points across different tables (e.g., updating a pet's price, an employee's salary, and the nourishment quantity).
- Verification: Confirm that only the explicitly targeted fields are updated correctly in the database, without affecting other unrelated data.
<img width="1280" height="526" alt="image" src="https://github.com/user-attachments/assets/ec39503f-2bb1-4707-9db3-57cf53a7bafc" />
<img width="972" height="714" alt="image" src="https://github.com/user-attachments/assets/b0b23ad1-a6d8-47cb-ac48-29c5cff26825" />

<img width="555" height="395" alt="image" src="https://github.com/user-attachments/assets/e5b61985-c527-40a2-ae03-17186308a415" />

<img width="1071" height="842" alt="image" src="https://github.com/user-attachments/assets/421a7195-76f7-4ae1-adf0-275e259a1ec6" />
<img width="928" height="792" alt="image" src="https://github.com/user-attachments/assets/a7becb31-c137-4f0a-b94e-3c920cd8f367" />
<img width="1102" height="683" alt="image" src="https://github.com/user-attachments/assets/e2ecef78-68c9-4439-ae7b-3f95ce18bba1" />
<img width="979" height="501" alt="image" src="https://github.com/user-attachments/assets/10f57df3-26d0-481e-85ca-29e38bc6d879" />
<img width="647" height="451" alt="image" src="https://github.com/user-attachments/assets/1b5d1345-d0b0-4c59-a171-4b3c73e80faf" />
<img width="985" height="509" alt="image" src="https://github.com/user-attachments/assets/05298e39-03c7-469a-800f-5593373cd27a" />
<img width="1051" height="786" alt="image" src="https://github.com/user-attachments/assets/a38f6505-f0c9-4df1-b852-bbde0121bed1" />
<img width="1079" height="793" alt="image" src="https://github.com/user-attachments/assets/98b3e421-f8a0-4048-a792-81c55dce577e" />
<img width="1001" height="825" alt="image" src="https://github.com/user-attachments/assets/52e96e50-7916-4656-9995-65bad8daa49d" />
<img width="1001" height="825" alt="image" src="https://github.com/user-attachments/assets/7b10b2e6-8a52-4eaa-a6ab-a799ae770741" />
<img width="1067" height="707" alt="image" src="https://github.com/user-attachments/assets/a46c5c7e-14ec-4591-9db0-b3df89a99e6a" />
<img width="1280" height="626" alt="image" src="https://github.com/user-attachments/assets/b38b341c-3fd6-4f83-b370-8589a27696f8" />
<img width="849" height="866" alt="image" src="https://github.com/user-attachments/assets/48400df1-8e5f-4446-8521-25d0ac87382c" />

<img width="932" height="423" alt="image" src="https://github.com/user-attachments/assets/28dbd79c-4238-4617-a64d-9d8be5f7e6e3" />


