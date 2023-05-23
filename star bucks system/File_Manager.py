import classes


class FM:
    def read_users(filename="WebUsers.txt"):
        try:
            # Define empty lists to store the user data
            User=[]
            
            # Open the file for reading
            with open(filename, "r") as file:
                # Loop through each line in the file
                for line in file:
                    # Split the line into ID, name, and password using the comma as the delimiter
                    user_data = line.strip().split(",")
            
                    # Add the ID, name, and password to their respective lists
                    user=classes.User(userId=user_data[0],username=user_data[1],password=user_data[2])
                    User.append(user)
            # Return the three lists as a tuple
            return User
        except Exception as e:
            print(f"Error reading from file: {e}")
            return None

    def write_user( users,filename="WebUsers.txt"):
        # Open the file for writing, creating it if it doesn't exist and overwriting it if it does
        with open(filename, "w") as file:
            # Loop through the users and write their data to the file
            for user in users:
                # Write the user's ID, name, and password to the file, separated by commas
                file.write(f"{user.user_id},{user.username},{user.password}\n")


    def write_records(employee_accounts_list,customer_accounts_list,filename="Records.txt"):
        """
    Writes the employee and customer account information to the specified file in the following format:

    <emirate>,<telephone>,<email>,<account_balance>,<membership_id>,<isFamilyAccount>,<familyId>,<job_title>,<accountType>

    Parameters:
    filename (str): The name of the file to write the account information to.
    employee_accounts_list (list): A list of EmployeeAccount objects to write to the file.
    customer_accounts_list (list): A list of CustomerAccount objects to write to the file.

    Returns:
    bool: True if the data was written successfully, False otherwise.
    """
        try:
            with open(filename, "w") as file:
                for account in employee_accounts_list:
                    file.write(f"{account.name},{account.emirate},{account.telephone},{account.email},{account.account_balance},{account.membership_id},{account.isFamilyAccount},{account.familyId},{account.job_title},{account.accountType}\n")
                for account in customer_accounts_list:
                    file.write(f"{account.name},{account.emirate},{account.telephone},{account.email},{account.account_balance},{account.membership_id},{account.isFamilyAccount},{account.familyId},None,{account.accountType}\n")
                return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False


    def read_records(filename="Records.txt"):
        """
    Reads employee and customer account records from a text file and returns them as a tuple of lists. Each account record
    is represented as an instance of the EmployeeAccount or CustomerAccount class.

    Args:
        filename (str): The name of the text file to read from.

    Returns:
        tuple: A tuple containing two lists. The first list contains instances of the EmployeeAccount class, and the
        second list contains instances of the CustomerAccount class. If an error occurs during file reading, None is
        returned.

    Raises:
        None
    """
        employee_accounts_list = []
        customer_accounts_list = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    attributes = line.strip().split(",")
                    name,emirate, telephone, email, account_balance, membership_id, isFamilyAccount, familyId, job_title, accountType = attributes
                    if accountType == "Employee":
                        account = classes.Employee(name=name,email=email,emirate=emirate,telephone=telephone,membership_id=membership_id,familyId=familyId,job_title=job_title,isFamilyAccount=isFamilyAccount,account_balance=account_balance,accountType=accountType)
                        employee_accounts_list.append(account)
                    elif accountType == "Customer":
                        account = classes.Customer(name=name,email=email,emirate=emirate,telephone=telephone,membership_id=membership_id,familyId=familyId,account_balance=account_balance,isFamilyAccount=isFamilyAccount)
                        customer_accounts_list.append(account)
                    else:
                        print(f"Error: Unknown account type '{accountType}'")
                        return None
        except Exception as e:
            
            print(f"Error reading from file: {e}")
            return None
        
       
        return (employee_accounts_list, customer_accounts_list)


    def write_memberships_to_file(memberships, filename="Membership&Rewards.txt"):
        """
    Write a list of Membership objects to a text file.

    Arguments:
    memberships -- A list of Membership objects to write to the file.
    filename -- The name of the file to write to. If not provided, defaults to "Membership&Rewards.txt".

    Returns:
    None if an error occurs, or the number of Membership objects written to the file.
    """
        try:
            with open(filename, "w") as file:
                for membership in memberships:
                    file.write(f"{membership.membershipId},{membership.rewardPoints}\n")
        except Exception as e:
            
            print(f"Error reading from file: {e}")
            return None

    def read_memberships_from_file(filename="Membership&Rewards.txt"):
        """Reads `Membership` objects from a text file with the given filename.

    Args:
        filename (str): The name of the file to read from,defaults to "Membership&Rewards.txt".

    Returns:
        A list of `Membership` objects read from the file, or None if an error occurs.

    Raises:
        None

    The function opens the file with the given filename in read mode, and reads each line
    as a comma-separated list of values representing a `Membership` object. Each `Membership`
    object is constructed from the values in the list and added to a list of `Membership`
    objects. If an error occurs while reading the file, the function prints an error message
    and returns None.
    """
        memberships = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    membership_data = line.strip().split(",")
                    membership = classes.Membership(membership_data[0], int(membership_data[1]))
                    memberships.append(membership)
            return memberships

        except Exception as e:
            
            print(f"Error reading from file: {e}")
            return None

    def write_purchases_to_file(purchases):
        """Writes a list of `Purchase` objects to a text file named Product-Purchased.txt.

        Args:
            purchases (list): A list of `Purchase` objects to write to the file.

        Returns:
            None

        Raises:
            None

        The function creates a new file named Product-Purchased.txt in write mode and writes each
        `Purchase` object in the list to a separate line in the file. Each line contains the following
        comma-separated values in order: membership ID, total bill, discount, payable bill, and a list
        of product names separated by semicolons.
        """
        try:
            with open("Product-Purchased.txt", "w") as file:
                for purchase in purchases:
                    product_names = ";".join(purchase.productList)
                    line = f"{purchase.membershipId},{purchase.totalBill},{purchase.discount},{purchase.payableBill},{product_names}\n"
                    file.write(line)

        except Exception as e:
            print(f"Error writing to file: {e}")
    
    def read_purchases_from_file(filename="Product-Purchased.txt"):
        """Reads a list of `Purchase` objects from a text file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        A list of `Purchase` objects, or None if there was an error reading from the file.

    Raises:
        None

    The function reads data from a file named Product-Purchased.txt and returns a list of `Purchase`
    objects. Each line of the file is assumed to contain the following comma-separated values in order:
    membership ID, total bill, discount, payable bill, and a list of product names separated by semicolons.
    """
        try:
            purchases = []
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    purchase_data = line.split(",")
                    product_names = purchase_data[4].split(";")
                    purchase = classes.Purchase(purchase_data[0], float(purchase_data[1]), float(purchase_data[2]), float(purchase_data[3]), product_names)
                    purchases.append(purchase)
            return purchases

        except Exception as e:
            print(f"Error reading from file: {e}")
            return None

