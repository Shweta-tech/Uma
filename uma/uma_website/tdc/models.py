from django.db import models
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
# from wagtailimages.blocks import ImageChooserBlock
from streams import blocks

class TDCPage(Page):
    template = "tdc/tdc_page.html"
 
    contents = StreamField(
		[
			("doc",blocks.PresentationBlock())

		],
    null=True,
		blank=True,
  )
    content_panels = Page.content_panels + [
         
        
         StreamFieldPanel("contents"),
        
      ]

    class Meta:
         verbose_name = "TDC Page" 