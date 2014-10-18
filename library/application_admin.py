
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _

class MyApplicationAdmin(ApplicationAdmin):
  
    name = 'Camelot Library'
    application_url = 'http://library.alinefreitas.com.br'
    help_url = 'http://www.python-camelot.com/docs.html'
    author = 'Aline Freitas'
    domain = 'alinefreitas.com.br'
    
    def get_sections(self):
        from camelot.model.memento import Memento
        from camelot.model.i18n import Translation
        from library.model import Author, Books, Publisher
        from library.importer import ImportCovers
        return [ 
            Section( _('Books'),
                self,
                Icon('tango/22x22/mimetypes/x-office-presentation.png'),
                items = [ Books, 
                          Author,
                          Publisher,
                          ImportCovers() ] ),
            Section( _('Configuration'),
                self,
                Icon('tango/22x22/categories/preferences-system.png'),
                items = [Memento, Translation] )
            ]


