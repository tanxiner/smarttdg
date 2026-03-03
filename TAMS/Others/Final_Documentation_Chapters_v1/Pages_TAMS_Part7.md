# Page Functionality Reference

## **Login.aspx.cs**
### **User Actions**
- Enter username and password credentials.
- Submit login form to authenticate.

### **Data Flow**
- Validates entered credentials against a database.
- Redirects to the dashboard if authentication is successful; displays an error message otherwise.

---

## **MaintainCompany.aspx.cs**
### **User Actions**
- Search for companies using filters.
- Clear search criteria to reset the form.
- Edit or manage company records.

### **Data Flow**
- Queries the database to retrieve company records based on search criteria.
- Encrypts company IDs for secure data handling.
- Updates or modifies company records in the database upon submission.

---

## **MaintainCompanyDetails.aspx.cs**
### **User Actions**
- Update specific company details.
- Navigate back to the company list.

### **Data Flow**
- Loads company details by ID from the database.
- Applies changes to the database upon form submission.
- Redirects to the company list page after updates.

---

## **MaintainUser.aspx.cs**
### **User Actions**
- Search for users using filters.
- Clear search criteria to reset the form.
- Edit or manage user records.

### **Data Flow**
- Queries the database to retrieve user records based on search criteria.
- Encrypts user IDs for secure data handling.
- Updates or modifies user records in the database upon submission.

---

## **MaintainUserDetails.aspx.cs**
### **User Actions**
- Update specific user details.
- Navigate back to the user list.

### **Data Flow**
- Loads user details by ID from the database.
- Applies changes to the database upon form submission.
- Redirects to the user list page after updates.

---

## **MaintainUserDetails.aspx.cs**
### **User Actions**
- Update specific user details.
- Navigate back to the user list.

### **Data Flow**
- Loads user details by ID from the database.
- Applies changes to the database upon form submission.
- Redirects to the user list page after updates.