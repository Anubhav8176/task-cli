import json
import sys
import datetime


def loadAllData(data):
    try:
        with open("data", "r") as f:
            data = json.load(f)
        return data
    except(FileNotFoundError, json.JSONDecodeError):
        print("No data found!")


def addData(description):
    try:
        with open("data", "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Calculate next ID
    max_id = max((item['id'] for item in existing_data), default=0)
    new_id = max_id + 1

    # Create new entry
    current_time = datetime.datetime.now()
    data_added = {
        "id": new_id,
        "description": description,
        "status": "in-progress",
        "createdAt": str(current_time),
        "updatedAt": str(current_time)
    }

    # Append to existing data
    existing_data.append(data_added)

    # Write back to file
    with open("data", "w") as f:
        json.dump(existing_data, f, indent=2)

    print(f"Added item with ID: {new_id}")


def updateData(arg_id, new_description):
    try:
        with open("data", "r") as f:
            file_data = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        print("No data found for update!")

    new_data = []

    for d in file_data:
        if int(arg_id) == d["id"]:
            d.pop("description")
            d.pop("updatedAt")
            print(type(d["id"]))

            d["description"] = new_description
            d["updatedAt"] = str(datetime.datetime.now())

        new_data.append(d)

    with open("data", "w") as f:
        json.dump(new_data, f, indent=2)


def loadDataByStatus(status):
    try:
        with open("data", "r") as f:
            file_data = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        print("No file found!")

    required_data = []

    for d in file_data:
        if d["status"]==status:
            required_data.append(d)

    return required_data


def deleteData(arg_id):
    try:
        with open("data", "r") as f:
            file_data = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        print("No data found to delete!")

    new_data = []

    for d in file_data:
        if int(arg_id) != d["id"]:
            new_data.append(d)

    with open("data", "w") as f:
        json.dump(new_data, f, indent=2)


def updateStatus(arg_id, new_status):
    try:
        with open("data", "r") as f:
            file_data = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        print("No data found to delete!")

    new_data = []

    for d in file_data:
        if int(arg_id)==d["id"]:
            d.pop("status")
            d["status"]=new_status

        new_data.append(d)

    with open("data", "w") as f:
        json.dump(new_data, f, indent=2)


if __name__ == '__main__':
    data = []

    command = sys.argv[1].lower()

    match command:
        case "list":
            data = loadAllData(data)
            if len(sys.argv)<3:
                if data is not None:
                    print(data)
            else:
                status = sys.argv[2].lower()
                new_data = loadDataByStatus(status)
                if new_data is not None:
                    print(new_data)


        case "add":
            description = sys.argv[2]
            addData(description)

        case "delete":
            arg_id = sys.argv[2]
            deleteData(arg_id)

        case "update":
            arg_id = sys.argv[2]
            new_description = sys.argv[3]
            updateData(arg_id, new_description)

        case _:
            arg_id = sys.argv[2]
            new_status = sys.argv[1].split("-", 1)[1]
            print(f"New status => {new_status}")
            updateStatus(arg_id, new_status)

