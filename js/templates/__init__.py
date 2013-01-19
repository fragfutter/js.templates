from fanstatic import Library, Resource

library = Library('templates', 'resources')

resources = Resource(library,
                     'tmpl.js',
                     minified='tmpl.min.js')
