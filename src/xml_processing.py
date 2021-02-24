from typing import Union
from xml.dom.minidom import Document, parseString


def get_elements_from_xml(
    xml_doc: Document, tag_name: str, attributes: list[str], get_all: bool = False
) -> Union[list[dict[str, str]], dict[str, str]]:

    root_elements = xml_doc.getElementsByTagName(tag_name)
    result = []

    for el in root_elements:
        attr_dict = {}

        for attr in attributes:
            attr_dict[attr] = el.attributes[attr].value

        if get_all:
            result.append(attr_dict)
        else:
            return attr_dict

    return result


def create_csv_row_from_xml(raw_file):
    decoded_file = raw_file.file.read().decode("utf-8")
    xml_doc = parseString(decoded_file)
    emissor = get_elements_from_xml(xml_doc, "cfdi:Emisor", ["Nombre", "Rfc"])
    invoice = get_elements_from_xml(
        xml_doc, "cfdi:Comprobante", ["SubTotal", "Fecha", "Folio"]
    )

    concepts = get_elements_from_xml(
        xml_doc, "cfdi:Concepto", ["Descripcion"], get_all=True
    )

    concepts_dict = {
        f"Concepto {idx + 1}": concept.get("Descripcion")
        for idx, concept in enumerate(concepts)
    }

    return {**emissor, **invoice, **concepts_dict}
