try:
    with open('myfile.txt') as file:
        file_data = file.read()
    print(file_data)
except Exception as error:
    print('Some other error occured.', str(error))
