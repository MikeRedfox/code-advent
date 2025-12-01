def get_data(file_path: str):
    with open(file_path) as f:
        data = f.readlines()
        data = [i[:-1] for i in data]
        return data
