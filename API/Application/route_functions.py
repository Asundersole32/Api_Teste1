from Persistence import file_manipulation, data_manipulation


def presentation_function():
    try:
        ids = file_manipulation.ids_r()
        message = "workers cadastrados: "+str(len(ids['workers']))+" projects cadastrados: "+str(len(ids['projects']))\
                  +" sectors cadastrados: "+str(len(ids['sectors']))

        return message
    except Exception as Error:
        ids = {
            'workers': [],
            'projects': [],
            'sectors': []
        }

        data_manipulation.ids_manipulation(ids)
        return presentation_function()
