import xml.etree.ElementTree as ET

def load_user_data(xml_file):
    tree = ET.parse(xml_file)
    user = tree.getroot().find('user')
    return {
        'first_name': user.find('firstname').text,
        'last_name': user.find('lastname').text,
        'email': user.find('email').text,
        'gender': user.find('gender').text,
        'mobile': user.find('mobile').text,
        'subject': user.find('subject').text,
        'hobbies': [h.text for h in user.find('hobbies').findall('hobby')]
    }

