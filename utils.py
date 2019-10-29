import numpy as np

def make_seqData(num_customers, max_shopping, p_size, p_list):
    '''
    is to make a virtual sequential transaction dataset

    num_customers: max number of customers(=total transactions)
    max_shopping: max number of shopping by each customers(=max event by customer)
    p_size: size of products list
    p_list: products list

    return: list [[customerID, eventID, [products1, products2, ...]], ...]
    '''
    transactions = []
    for customer in range(num_customers):
        cus = []
        cusID = customer + 1

        num_shopping = np.random.randint(
            low=1, high=max_shopping + 1, size=1) # is changed by each customer

        for shopping in range(num_shopping[0]):
            event = []
            event.append(cusID)

            eventID = shopping + 1
            event.append(eventID)

            buying_size = np.random.randint(
                low=1, high=p_size, size=1) # is changed by each event
            each_shopping = np.random.choice(
                p_list, size=buying_size[0], replace=False)
            event.append(each_shopping.tolist())

            cus.append(event)

        transactions.extend(cus)

    return transactions


def make_Data(num_customers, p_size, p_list):
    '''
    is to make a virtual transaction dataset

    num_customers: max number of customers(=total transactions)
    p_size: size of products list
    p_list: products list

    return: list [[products1, products2, ...], ...]
    '''
    transactions = []
    for _ in range(num_customers):
        buying_size = np.random.randint(
            low=1, high=p_size, size=1)  # is changed by each customer
        each_customer = np.random.choice(
            p_list, size=buying_size[0], replace=False)

        transactions.append(each_customer)

    return transactions