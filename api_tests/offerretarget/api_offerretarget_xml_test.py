from sender.request_sender import Sender
from xml.etree import ElementTree as et
import pprint


def setup_module():
    global code
    global jsondump
    global schema
    global curdir
    global xml
    pp = pprint.PrettyPrinter()
    print('----------------------------------------------------------------------')
    print('setup module ' + __name__)
    sender = Sender()
    request = sender.get("/api/rest/webmaster/xml/offertarget/4325?")
    raw_xml = request.text
    pp.pprint(raw_xml)
    code = request.status_code
    xml = et.fromstring(raw_xml)


def test_offerretarget_xml_status():
    assert code == 200


def test_offerretarget_xml_status():
    status = int(xml.find('status').text)
    assert status != 500
    assert status is not ''
    assert status != 400


def test_promo_xml_data():
    error = xml.find('.//error').text
    assert error is None

    items = xml.find('.//data/items/item/service_area')
    for item in items:
        assert len(item.find('id').text) > 0
        assert len(item.find('code').text) > 0
        assert len(item.find('title').text) > 0















