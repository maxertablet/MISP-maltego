from canari.maltego.entities import Hash, Domain, IPv4Address, URL, DNSName, AS, Website, NSRecord, PhoneNumber, EmailAddress, File, Hashtag, Company, Alias, Twitter
from canari.maltego.transform import Transform
# from canari.framework import EnableDebugWindow
from MISP_maltego.transforms.common.entities import MISPEvent
from MISP_maltego.transforms.common.util import get_misp_connection, event_to_entity

__author__ = 'Christophe Vandeplas'
__copyright__ = 'Copyright 2018, MISP_maltego Project'
__credits__ = []

__license__ = 'AGPLv3'
__version__ = '0.1'
__maintainer__ = 'Christophe Vandeplas'
__email__ = 'christophe@vandeplas.com'
__status__ = 'Development'


# @EnableDebugWindow
class AttributeToEvent(Transform):
    # The transform input entity type.
    input_type = None

    def do_transform(self, request, response, config):
        maltego_misp_attribute = request.entity
        misp = get_misp_connection(config)
        # misp.
        events_json = misp.search(controller='events', values=maltego_misp_attribute.value, withAttachments=False)
        for e in events_json['response']:
            response += event_to_entity(e)
        return response

    def on_terminate(self):
        """This method gets called when transform execution is prematurely terminated. It is only applicable for local
        transforms. It can be excluded if you don't need it."""
        pass


class HashToEvent(AttributeToEvent):
    input_type = Hash


class DomainToEvent(AttributeToEvent):
    input_type = Domain


class IPv4AddressToEvent(AttributeToEvent):
    display_name = 'IPv4AddressToEvent'
    input_type = IPv4Address


class URLToEvent(AttributeToEvent):
    display_name = 'URLToEvent'
    input_type = URL


class DNSNameToEvent(AttributeToEvent):
    display_name = 'DNSNameToEvent'
    input_type = DNSName


class ASToEvent(AttributeToEvent):
    display_name = 'ASToEvent'
    input_type = AS


class WebsiteToEvent(AttributeToEvent):
    input_type = Website


class NSRecordToEvent(AttributeToEvent):
    display_name = 'NSRecordToEvent'
    input_type = NSRecord


class PhoneNumberToEvent(AttributeToEvent):
    input_type = PhoneNumber


class EmailAddressToEvent(AttributeToEvent):
    input_type = EmailAddress


class FileToEvent(AttributeToEvent):
    input_type = File


class HashtagToEvent(AttributeToEvent):
    input_type = Hashtag


class AliasToEvent(AttributeToEvent):
    input_type = Alias


class TwitterToEvent(AttributeToEvent):
    input_type = Twitter


class CompanyToEvent(AttributeToEvent):
    input_type = Company
