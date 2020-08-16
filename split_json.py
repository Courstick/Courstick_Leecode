"""递归处理 json 数据 所有 key-value 都只取冒号后的数据"""
test_data = {
    "k:key1": "vv:value",
    "kk2:key12": {
        "kkk:key21": "vvv:value21",
        "kkk1:key22": "vvv:value22"
    },
    "kk3:key13": [
        {
            "kkkk:key31": "vvv:value31",
            "kkk:key32": {
                "kkkk:key41": "vv:vv:value41",
                "kkkk1:key42": "value42"
            }
        }
    ]
}


def split_colon(data):
    result = dict()
    if isinstance(data, dict):
        for key, value in data.items():
            result[key.split(":")[1]] = split_colon(value)
    elif isinstance(data, list):
        for item in data:
            return split_colon(item)
    else:
        return data.split(":")[1] if data.find(':') != -1 else data
    return result


print(split_colon(test_data))
