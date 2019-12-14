import requests

def jp2en_transrator(string):
    result = requests.get('https://script.google.com/macros/s/AKfycbxjITyi5QlS-NhSAzg6BRQbiWPSK05qnOF1DYl9H_FC_4tzlOM/exec?text=' + string + '&source=ja&target=en')
    result.encoding

    return result.text