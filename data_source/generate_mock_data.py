from bson.timestamp import Timestamp
from faker import Faker
fake = Faker()

ID = 'id'
CURRENCY = 'currency'   
PURCHASE_TITLE = 'purchase_title'
PURCHASE_DESCRIPTION = 'purchase_description'
AMOUNT = 'amount'
LOCATION = 'location'
TIMESTAMP = 'time'
dataset = []

class GenerateMockData:

    def __init__(self):
	    self.generate_dataset()

    def generate_dataset(self):
        for item in range(100):

            fake_timestamp = fake.date_time_between(start_date="now", end_date="+3d", tzinfo=None)
            fake_currency = "GBP"
            fake_amount = fake.pydecimal(left_digits=3, right_digits=2, positive=True, min_value=1, max_value=2000)
            fake_location = fake.street_address()
            fake_sentence_generator = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            fake_purchase_desc = fake_sentence_generator
            fake_purchase_title = fake_sentence_generator
            id = fake.msisdn()

            single_data_entry =  {
                ID : id,
                CURRENCY : fake_currency  , 
                PURCHASE_TITLE : fake_purchase_title,
                PURCHASE_DESCRIPTION : fake_purchase_desc,
                AMOUNT : fake_amount,
                LOCATION : fake_location,
                TIMESTAMP : fake_timestamp
            }
            dataset.append(single_data_entry)
            return dataset