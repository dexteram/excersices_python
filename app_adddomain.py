import requests
import json
import xmltodict
import os

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('config.env')
load_dotenv(dotenv_path=dotenv_path)

url_mssl = os.getenv('URL_MSSL')
username_mssl = os.getenv('USERNAME_MSSL')
password_mssl = os.getenv('PASSWORD_MSSL')


def lambda_handler(event, context):
    body = event
    print(event)
    

    soap_tagname = "AddDomainToProfile"
    headers = {'content-type': 'text/xml'}

    profile_id = body["profile_id"]
    domain_name = body["domain_name"]
    vetting_level = body["vetting_level"]
    vetting_type = body["vetting_type"]
    # userid = body["userid"]
    first_name = body["first_name"]
    last_name = body["last_name"]
    phone = body["phone"]
    email = body["email"]

    data = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="https://system.globalsign.com/kb/ws/v1/">
        <soapenv:Header/>
        <soapenv:Body>
            <v1:{soap_tagname}>
                <Request>
                    <OrderRequestHeader>
                    <AuthToken>
                        <UserName>{username_mssl}</UserName>
                        <Password>{password_mssl}</Password>
                    </AuthToken>
                    </OrderRequestHeader>
                    <MSSLProfileID>{profile_id}</MSSLProfileID>
                    <DomainName>{domain_name}</DomainName>
                    <VettingLevel>{vetting_level}</VettingLevel>
                    <VettingType>{vetting_type}</VettingType>
                    <ContactInfo>
                    <FirstName>{first_name}</FirstName>
                    <LastName>{last_name}</LastName>
                    <Phone>{phone}</Phone>
                    <Email>{email}</Email>
                    </ContactInfo>
                </Request>
            </v1:{soap_tagname}>
        </soapenv:Body>
    </soapenv:Envelope>"""

    xml_resp = requests.post(url_mssl, data, headers)
    res = json.loads(json.dumps(xmltodict.parse(xml_resp.content)))
    try:
        res = res["soap:Envelope"]["soap:Body"][f"ns2:{soap_tagname}Response"]["Response"]
    except Exception as err:
        print("Error formatting response", err)

    return {
        "statusCode": 200,
        "body": json.dumps(res),
    }
