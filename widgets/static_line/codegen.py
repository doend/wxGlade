# codegen.py: code generator functions for wxStaticLine objects
#
# Copyright (c) 2002 Alberto Griggio <albgrig@tiscalinet.it>
# License: GPL (see license.txt)

import common

def python_code_generator(obj):
    """\
    generates the python code for wxStaticLine objects
    """
    pygen = common.code_writers['python']
    prop = obj.properties
    id_name, id = pygen.generate_code_id(obj)
    if obj.is_toplevel:
        l = ['self.%s = %s(self, %s)\n' % (obj.name, obj.klass, id)]
        if id_name: l.append(id_name)
        return l, [], []
    size = pygen.generate_code_size(obj)
    if not obj.parent.is_toplevel: parent = 'self.%s' % obj.parent.name
    else: parent = 'self'
    style = prop.get("style", "wxLI_HORIZONTAL")
    if not style: style = "wxLI_HORIZONTAL"
    init = ['self.%s = wxStaticLine(%s, %s, size=%s, style=%s)\n' %
            (obj.name, parent, id, size, style) ]
    if id_name: init.append(id_name)
    props_buf = []
    if prop.has_key('foreground'):
        props_buf.append(pygen.generate_code_foreground(obj))
    if prop.has_key('background'):
        props_buf.append(pygen.generate_code_background(obj))
    return init, props_buf, []
    

def initialize():
    common.class_names['EditStaticLine'] = 'wxStaticLine'

    # python code generation functions
    pygen = common.code_writers.get("python")
    if pygen:
        pygen.add_widget_handler('wxStaticLine', python_code_generator)
    
