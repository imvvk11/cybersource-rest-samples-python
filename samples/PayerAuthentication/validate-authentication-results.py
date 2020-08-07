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

def validate_authentication_results():
    clientReferenceInformationCode = "pavalidatecheck"
    clientReferenceInformation = Riskv1authenticationsetupsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsTotalAmount = "200.00"
    orderInformationAmountDetails = Riskv1authenticationsOrderInformationAmountDetails(
        currency = orderInformationAmountDetailsCurrency,
        total_amount = orderInformationAmountDetailsTotalAmount
    )


    orderInformationLineItems = []
    orderInformationLineItems1 = Riskv1authenticationresultsOrderInformationLineItems(
        unit_price = "10",
        quantity = 2,
        tax_amount = "32.40"
    )

    orderInformationLineItems.append(orderInformationLineItems1.__dict__)

    orderInformation = Riskv1authenticationresultsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        line_items = orderInformationLineItems
    )

    paymentInformationCardType = "002"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2025"
    paymentInformationCardNumber = "5200000000000007"
    paymentInformationCard = Riskv1authenticationresultsPaymentInformationCard(
        type = paymentInformationCardType,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,
        number = paymentInformationCardNumber
    )

    paymentInformation = Riskv1authenticationresultsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    consumerAuthenticationInformationAuthenticationTransactionId = "PYffv9G3sa1e0CQr5fV0"
    consumerAuthenticationInformationResponseAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5YTAwYTYzMC0zNzFhLTExZTYtYTU5Ni1kZjQwZjUwMjAwNmMiLCJpYXQiOjE0NjY0NDk4MDcsImlzcyI6Ik1pZGFzLU5vRFYtS2V5IiwiUGF5bG9hZCI6eyJPcmRlckRldGFpbHMiOnsiT3JkZXJOdW1iZXIiOjE1NTc4MjAyMzY3LCJBbW91bnQiOiIxNTAwIiwiQ3VycmVudENvZGUiOiI4NDAiLCJUcmFuc2FjdGlvbklkIjoiOVVzaGVoRFFUcWh1SFk5SElqZTAifX0sIk9yZ1VuaXRJZCI6IjU2NGNkY2JjYjlmNjNmMGM0OGQ2Mzg3ZiIsIk9iamVjdGlmeVBheWxvYWQiOnRydWV9.eaU8LZJnMtY3mPl4vBXVCVUuyeSeAp8zoNaEOmKS4XY"
    consumerAuthenticationInformationSignedPares = "eNqdmFmT4jgSgN+J4D90zD4yMz45PEFVhHzgA2zwjXnzhQ984Nvw61dAV1"
    consumerAuthenticationInformation = Riskv1authenticationresultsConsumerAuthenticationInformation(
        authentication_transaction_id = consumerAuthenticationInformationAuthenticationTransactionId,
        response_access_token = consumerAuthenticationInformationResponseAccessToken,
        signed_pares = consumerAuthenticationInformationSignedPares
    )

    requestObj = ValidateRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        consumer_authentication_information = consumerAuthenticationInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PayerAuthenticationApi(client_config)
        return_data, status, body = api_instance.validate_authentication_results(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PayerAuthenticationApi->validate_authentication_results: %s\n" % e)

if __name__ == "__main__":
    validate_authentication_results()
