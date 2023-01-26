from cnab.models import Cnab


def convert_file(request):
    uploaded_file = request.FILES["file"]

    for line in uploaded_file:
        str_line = line.decode()

        data = {
            "type": str_line[0],
            "date": str_line[1:9],
            "value": str_line[9:19],
            "cpf": str_line[19:30],
            "card": str_line[30:42],
            "hour": str_line[42:48],
            "owner": str_line[48:62].rstrip(),
            "store_name": str_line[62:80].rstrip(),
        }

        validate_value(data)

        instance = Cnab.objects.create(**data)
        instance.save()


def validate_value(data):

    if data["type"] == "2" or data["type"] == "3" or data["type"] == "9":
        data["value"] = "-" + data["value"]
