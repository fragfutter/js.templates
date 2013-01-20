from fanstatic import Library, Resource

library = Library('js_templates', 'resources')

resources = Resource(library,
                     'tmpl.js',
                     minified='tmpl.min.js')
