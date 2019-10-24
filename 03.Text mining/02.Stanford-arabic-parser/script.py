#%%
from Parser import Parser

#%%
ar_model_path = 'arabicFactored.ser.gz'
my_path_to_jar = 'stanford-parser.jar'
my_path_to_models_jar = 'stanford-arabic-corenlp-2018-10-05-models.jar'




#%%
parser = Parser(model_path=ar_model_path, path_to_jar=my_path_to_jar, path_to_models_jar=my_path_to_models_jar)
result = parser.parse_sentence(u'ذهبت الى منزلى الذى كان بعيداً بعد الفجر')
print(result)
