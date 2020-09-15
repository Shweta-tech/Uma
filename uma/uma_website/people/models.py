from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks

class PeoplePage(Page):

    template = "people/people_page.html"

    # heading = models.CharField(max_length=100, null=True, blank=True)
    # description = models.TextField(blank=True)
    
    # content = StreamField(
    #     [
    #         ("reportss", blocks.ReportsBlock()),
    #         ("full_richtext", blocks.RichtextBlock()),
    #     ],
    #      null=True,
    #      blank=True
    # )
                           

    # content_panels = Page.content_panels + [
    #     FieldPanel("heading"),
    #     FieldPanel("description"),
    #     StreamFieldPanel("content"),
    # ]
    

    class Meta:  #noqa
        verbose_name = "People Page"
        verbose_name_plural = "People Pages"

