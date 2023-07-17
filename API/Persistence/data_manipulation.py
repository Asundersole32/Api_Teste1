from Persistence import file_manipulation


def ids_manipulation_w(ids_data):
    try:
        file_manipulation.ids_w(ids_data)
        return True
    except Exception as Error:
        return Error
    
def user_manipulation_r(workers_data):
    try:
        users = file_manipulation.users_r()
        return users
    except Exception as Error:
        return Error