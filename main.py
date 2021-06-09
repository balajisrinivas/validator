import rules as R
from validator import Validator

request = {"project_id": "1234",
           "feature_table_name": "999"}
rules = {"project_id": [R.Required, R.ProjectIDExistsRule],
         "feature_table_name": [R.FeatureTableExistsRule]}

val = Validator(request, rules)
result = val.validate()
print(result)
