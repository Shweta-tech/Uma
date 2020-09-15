from django.db import models
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
# from wagtailimages.blocks import ImageChooserBlock
from streams import blocks

class Eng1Page(Page):
    # Aiei page
    template = "eng1/eng1_page.html"
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    # content = StreamField(
    #     [
    #         ("doc_upload",blocks.DocumentBlock())
    #     ],
    #     null=True,
    #     blank=True,
    # ) 

    content_panels = Page.content_panels + [
         FieldPanel("subtitle"),
         # StreamFieldPanel("content"),
         ]

    class Meta:
         verbose_name = "Eng1 Page"

