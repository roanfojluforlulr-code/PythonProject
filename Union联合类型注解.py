from typing import Union
# 语法: Union[类型， 类型····类型]
my_list: list[Union[str, int]] = [1, 2, "asf", 'asdfa']
my_dict: dict[str,Union[int, str]] = {"asf": 1, "asfd": "adsf"}

def func(data: Union[str, int]) -> Union[int, str]:
    pass
func(2)