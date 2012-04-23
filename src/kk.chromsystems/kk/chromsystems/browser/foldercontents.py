from plone.app.content.browser.foldercontents import FolderContentsView, FolderContentsTable
from Acquisition import aq_parent, aq_inner
from Products.ATContentTypes.interface import IATTopic
from plone.app.content.browser.tableview import Table, TableKSSView

class ChFolderContentsView(FolderContentsView):

    def contents_table(self):
        table = ChFolderContentsTable(aq_inner(self.context), self.request)
        return table.render()
       
       
class ChFolderContentsTable(FolderContentsTable):

    def __init__(self, context, request, contentFilter={}):
        self.context = context
        self.request = request
        if not contentFilter.get('sort_on', None):
            contentFilter['sort_on'] = 'sortable_title'
        self.contentFilter = contentFilter
        self.items = self.folderitems()

        url = context.absolute_url()
        view_url = url + '/@@folder_contents'
        self.table = Table(request, url, view_url, self.items,
                           show_sort_column=self.show_sort_column,
                           buttons=self.buttons)
