import json

import requests
import hashlib
import base64
import uuid
from datetime import datetime
import xmltodict

password = "S7Np+Jbf*8NS"
message_id = str(uuid.uuid4())
nonce = message_id[24:]
timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

pass_sha = hashlib.sha1(
    nonce.encode("utf-8") + timestamp.encode("utf-8") + hashlib.sha1(password.encode("utf-8")).digest()
).digest()
pass_sha_encoded = base64.b64encode(pass_sha).decode("utf-8")
base64_nonce = base64.b64encode(nonce.encode("utf-8")).decode("utf-8")

print('message id: ' + message_id)
print('nonce_base64: ' + base64_nonce)
print('password_sha: ' + pass_sha_encoded)
print('timestamp: ' + timestamp)

# 构建 SOAP 请求消息
soap_request = f'''
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <add:MessageID xmlns:add="http://www.w3.org/2005/08/addressing">{message_id}</add:MessageID>
        <add:Action xmlns:add="http://www.w3.org/2005/08/addressing">http://webservices.amadeus.com/HLOREQ_04_2_1A</add:Action>
        <add:To xmlns:add="http://www.w3.org/2005/08/addressing">https://nodeD2.test.webservices.amadeus.com/1ASIWBOOFUSU</add:To>
        <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
            <oas:UsernameToken xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" oas1:Id="UsernameToken-1">
                <oas:Username>WSFUSBOO</oas:Username>
                <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{base64_nonce}</oas:Nonce>
                <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{pass_sha_encoded}</oas:Password>
                <oas1:Created>{timestamp}</oas1:Created>
            </oas:UsernameToken>
        </oas:Security>
        <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
            <UserID AgentDutyCode="SU" RequestorType="U" PseudoCityCode="LAS1S2414" POS_Type="1"/>
        </AMA_SecurityHostedUser>
        <awsse:Session TransactionStatusCode="Start" xmlns:awsse="http://xml.amadeus.com/2010/06/Session_v3"/>
    </soap:Header>
    <soap:Body>
        <Hotel_List>
            <scrollingInformation>
                <displayRequest>050</displayRequest>
                <maxNumberItems>10</maxNumberItems>
            </scrollingInformation>
            <hotelLocationPrefInfo>
            <locationSelection>
                <cityCode>LON</cityCode>
                <alternateCitiesOption>Y</alternateCitiesOption>
            </locationSelection>
            </hotelLocationPrefInfo>
        </Hotel_List>
    </soap:Body>
</soap:Envelope>
'''

# 发送 SOAP 请求
url = 'https://nodeD2.test.webservices.amadeus.com/1ASIWBOOFUSU'
headers = {'Content-Type': 'text/xml; charset=utf-8', 'SOAPAction': 'http://webservices.amadeus.com/HLOREQ_04_2_1A'}
response = requests.post(url, data=soap_request, headers=headers)

# 解析 SOAP 响应
soap_response = response.content

data = xmltodict.parse(soap_response, attr_prefix="")

print(json.dumps(data))
