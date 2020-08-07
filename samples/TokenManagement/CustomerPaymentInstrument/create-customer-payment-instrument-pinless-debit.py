from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def create_customer_payment_instrument_pinless_debit():
    customerTokenId = "AB695DA801DD1BB6E05341588E0A3BDC"

    cardExpirationMonth = "12"
    cardExpirationYear = "2031"
    cardType = "001"
    cardIssueNumber = "01"
    cardStartMonth = "01"
    cardStartYear = "2020"
    cardUseAs = "pinless debit"
    card = Tmsv2customersEmbeddedDefaultPaymentInstrumentCard(
        expiration_month = cardExpirationMonth,
        expiration_year = cardExpirationYear,
        type = cardType,
        issue_number = cardIssueNumber,
        start_month = cardStartMonth,
        start_year = cardStartYear,
        use_as = cardUseAs
    )

    billToFirstName = "John"
    billToLastName = "Doe"
    billToCompany = "CyberSource"
    billToAddress1 = "1 Market St"
    billToLocality = "San Francisco"
    billToAdministrativeArea = "CA"
    billToPostalCode = "94105"
    billToCountry = "US"
    billToEmail = "test@cybs.com"
    billToPhoneNumber = "4158880000"
    billTo = Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo(
        first_name = billToFirstName,
        last_name = billToLastName,
        company = billToCompany,
        address1 = billToAddress1,
        locality = billToLocality,
        administrative_area = billToAdministrativeArea,
        postal_code = billToPostalCode,
        country = billToCountry,
        email = billToEmail,
        phone_number = billToPhoneNumber
    )

    instrumentIdentifierId = "7010000000016241111"
    instrumentIdentifier = Tmsv2customersEmbeddedDefaultPaymentInstrumentInstrumentIdentifier(
        id = instrumentIdentifierId
    )

    requestObj = PostCustomerPaymentInstrumentRequest(
        card = card.__dict__,
        bill_to = billTo.__dict__,
        instrument_identifier = instrumentIdentifier.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CustomerPaymentInstrumentApi(client_config)
        return_data, status, body = api_instance.post_customer_payment_instrument(customerTokenId, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling CustomerPaymentInstrumentApi->post_customer_payment_instrument: %s\n" % e)

if __name__ == "__main__":
    create_customer_payment_instrument_pinless_debit()
