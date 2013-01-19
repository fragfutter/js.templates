from fanstatic import Library, Resource

library = Library('templates', 'resources')

templates = Resource(library,
                     'tmpl.js',
                     minified='tmpl.min.js')
