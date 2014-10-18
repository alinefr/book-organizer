from camelot.admin.action import Action


class BooksSummary( Action ):    
    verbose_name = 'Summary'

    def model_run(self, model_context):
        from camelot.view.action_steps import PrintHtml
        import datetime
        import os
        from jinja2 import Environment, FileSystemLoader
        from pkg_resources import resource_filename
        import library
        from camelot.core.conf import settings

        fileloader = FileSystemLoader(resource_filename(library.__name__, 'templates'))
        e = Environment(loader=fileloader)
        books = model_context.get_object()
        context = {
                'header':books.title,
                'title':'Book Summary',
                'style':'.label { font-weight:bold; }',
                'author':'<span class="label">Author:</span> {}<br>\
                        <span class="label">ISBN:</span> {}<br>\
                        <span class="label">Pages:</span> {}<br>\
                        <span class="label">Released:</span> {}\
                        <span class="label">Genre:</span> {}\
                        <span class="label">Cover:</span> {}\
                        <span class="label">Translator:</span> {}\
                        <span class="label">Publisher:</span> {}'\
                        .format(books.author, books.isbn, books.pages,\
                        books.copyright_year, books.genre, books.cover,\
                        books.translator, books.publisher),
                # 'cover': os.path.join( settings.CAMELOT_MEDIA_ROOT(), 'covers', books.cover ),
                'footer':'<br>copyright {} - Aline Freitas'.format(datetime.datetime.now().year)
        }
        t = e.get_template('books_summary.html')
        yield PrintHtml( t.render(context) )

