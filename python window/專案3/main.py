import datasource as ds


def main():
    print("這裏是main function")
    list_data = ds.get_forcast_data(ds.tw_county_names["基隆"])
    for item in list_data:
        print(item['dt_txt'])
