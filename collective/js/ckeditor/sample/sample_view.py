from zope import component
from Products.Five.browser import BrowserView


class SampleView(BrowserView):
    """Sample view is used as base view to manage some needed
    information like the site url"""

    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        self.portal_state = component.getMultiAdapter((self.context, self.request),
                                                      name="plone_portal_state")
        self.portal_url = self.portal_state.portal_url()
        self.sample_url = '%s/++resources++collective.js.ckeditor/samples' % self.portal_url
