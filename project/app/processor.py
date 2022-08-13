import ftd
import ftd_django

@ftd_django.processor("simple_processor")
def simple_processor(doc_id, section, interpreter):
    return ftd.string_to_value("Hello World!!")