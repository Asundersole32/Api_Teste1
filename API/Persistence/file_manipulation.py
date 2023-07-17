import json
import os


def administrators_w(adm_data, adm_id):
    try:
        with open("DataBase\Administrators\_adm_"+str(adm_id)+".json", "w") as outfile:
            json.dump(adm_data, outfile, indent=4)

    except:
        return False

def administrators_r(adm_id):
    try:
        with open("DataBase\Administrators\_adm_"+str(adm_id)+".json", "r") as infile:
            json_adm = json.load(infile)

        return json_adm

    except:
        return False

def administrators_d(adm_id):
    try:
        os.remove("DataBase\Administrators\_adm_"+str(adm_id)+".json")

    except:
        return False

def commons_w(commons_data, commons_id):
    try:
        with open("DataBase\Commons\_com_"+str(commons_id)+".json", "w") as outfile:
            json.dump(commons_data, outfile, indent=4)

    except:
        return False

def commons_r(commons_id):
    try:
        with open("DataBase\Commons\_com_"+str(commons_id)+".json", "r") as infile:
            json_commons = json.load(infile)

        return json_commons
    except:
        return False

def commons_d(commons_id):
    try:
        os.remove("Commons\_com_"+str(commons_id)+".json")

    except:
        return False

def projects_w(projects_data, projects_id):
    try:
        with open("DataBase\Projects\_proj_"+str(projects_id)+".json", "w") as outfile:
            json.dump(projects_data, outfile, indent=4)

    except:
        return False

def projects_r(projects_id):
    try:
        with open("DataBase\Projects\_proj_"+str(projects_id)+".json", "r") as infile:
            json_project = json.load(infile)

        return json_project

    except:
        return False

def projects_d(projects_id):
    try:
        os.remove("DataBase\Commons\_proj_"+str(projects_id)+".json")

    except:
        return False

def sectors_w(sectors_data, sectors_id):
    try:
        with open("DataBase\Sectors\_sec_"+str(sectors_id)+".json", "w") as outfile:
            json.dump(sectors_data, outfile, indent=4)

    except:
        return False

def sectors_r(sectors_id):
    try:
        with open("DataBase\Sectors\_sec_"+str(sectors_id)+".json", "r") as infile:
            json_sector = json.load(infile)

        return json_sector

    except:
        return False

def sectors_d(sectors_id):
    try:
        os.remove("DataBase\Sectors\_sec_"+str(sectors_id)+".json")

    except:
        return False

def ids_w(ids_data):
    try:
        with open("DataBase\Others\ids.json", "w") as outfile:
            json.dump(ids_data, outfile, indent=4)

    except:
        return False

def ids_r():
    try:
        with open("DataBase\Others\ids.json", "r") as infile:
            json_ids = json.load(infile)

        return json_ids

    except:
        return False

def users_w(users_data):
    try:
        with open("DataBase\Others\users.json", "w") as outfile:
            json.dump(users_data, outfile, indent=4)

    except:
        return False
    
def users_r():
    try:
        with open("DataBase\Others\users.json", "r") as infile:
            json_users = json.load(infile)

            return json_users
    except:
        return False
    