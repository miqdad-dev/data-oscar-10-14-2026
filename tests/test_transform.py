
import pandas as pd
from src.transform import transform
def test_transform():
    df = pd.DataFrame({'id':[1,2], 'name':['a','abcd']})
    out = transform(df)
    assert list(out['name_len']) == [1,4]
