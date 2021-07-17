import csv, smtplib, ssl


def alert(parameter):
    message = parameter
    from_address = "sadique4mh17mca16@gmail.com"
    password = "Sadiqali@123"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_address, password)
        with open("contacts_file.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for name, email in reader:
                server.sendmail(
                    from_address,
                    email,
                    message.format(name=name),
                )
