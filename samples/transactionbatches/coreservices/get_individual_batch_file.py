from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def get_individual_batch_file():
    try:
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        transction_api_obj = TransactionBatchApi(details_dict1)
        id="Owcyk6pl"
        return_data, status, body =transction_api_obj.pts_v1_transaction_batches_id_get(id)
        print(status)
        print(body)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    get_individual_batch_file()
