class User:
    def __init__(self, username,password,userId):
        self.username=username
        self.password=password
        self.user_id=userId

class User_Record:
    def __init__(self,name, emirate, telephone, email, account_balance, membership_id, isFamilyAccount, familyId,  accountType):
        self.name=name
        self.emirate = emirate
        self.telephone = telephone
        self.email = email
        self.account_balance = account_balance
        self.membership_id = membership_id
        self.isFamilyAccount = isFamilyAccount
        self.familyId = familyId
        self.accountType = accountType

class Employee(User_Record):
    def __init__(self,name, emirate, telephone, email, membership_id, isFamilyAccount, familyId,  job_title,accountType="Employee", account_balance=0):
        super().__init__(name,emirate, telephone, email, account_balance, membership_id, isFamilyAccount, familyId, "Employee")
        self.job_title = job_title

class Customer(User_Record):
    def __init__(self,name, emirate, telephone, email, membership_id, isFamilyAccount, familyId,accountType="Customer", account_balance=0):
        super().__init__(name,emirate, telephone, email, account_balance, membership_id, isFamilyAccount, familyId,"Customer")

class Membership:
    def __init__(self, membershipId, rewardPoints):
        self.membershipId = membershipId
        self.rewardPoints = rewardPoints

class Purchase:
    def __init__(self, membershipId, totalBill, discount, payableBill, productList):
        self.membershipId = membershipId
        self.totalBill = totalBill
        self.discount = discount
        self.payableBill = payableBill
        self.productList = productList

class Driver:
    def __init__(self):
        self.employeeList = []
        self.customerList = []
        self.membershipList = []
        self.purchaseList = []
        self.userList=[]
    def addEmployee(self, employee):
        self.employeeList.append(employee)

    def removeEmployee(self, employee):
        if employee in self.employeeList:
            self.employeeList.remove(employee)
            return True
        else:
            return False

    def modifyEmployee(self, employee, new_job_title):
        if employee in self.employeeList:
            employee.job_title = new_job_title
            return True
        else:
            return False

    def searchEmployee(self, username):
        for employee in self.employeeList:
            if employee.username == username:
                return employee
        return None

    def addCustomer(self, customer):
        self.customerList.append(customer)

    def removeCustomer(self, customer):
        if customer in self.customerList:
            self.customerList.remove(customer)
            return True
        else:
            return False

    def modifyCustomer(self, customer, new_email):
        if customer in self.customerList:
            customer.email = new_email
            return True
        else:
            return False

    def searchCustomer(self, username):
        for customer in self.customerList:
            if customer.username == username:
                return customer
        return None

    def addMembership(self, membership):
        self.membershipList.append(membership)

    def searchMembership(self, membershipId):
        for membership in self.membershipList:
            if membership.membershipId == membershipId:
                return membership
        return None

    def addPurchase(self, purchase):
        self.purchaseList.append(purchase)

    def searchPurchase(self, membershipId):
        for purchase in self.purchaseList:
            if purchase.membershipId == membershipId:
                return purchase
        return None
