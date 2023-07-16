from Persistence import file_manipulation


def ids_manipulation(ids_data):
    try:
        file_manipulation.ids_w(ids_data)
        return True
    except Exception as Error:
        return Exception
