from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家, 返回国家代码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家, 就返回 None
    return None

print(get_country_code("China"))