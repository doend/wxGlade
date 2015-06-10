"""\
wxCheckListBox widget configuration

@copyright: 2014 Carsten Grohmann
@copyright: 2015 Franco Bugnano
@license: MIT (see license.txt) - THIS PROGRAM COMES WITH NO WARRANTY
"""

config = {
    'wxklass': 'wxPropertyGridManager',
    'style_defs': {
        'wxPG_AUTO_SORT': {
            'desc': _('This will cause Sort() automatically after an item is added.'),
        },
        'wxPG_HIDE_CATEGORIES': {
            'desc': _('Categories are not initially shown (even if added).'),
        },
        'wxPG_ALPHABETIC_MODE': {
            'desc': _('This style combines non-categoric mode and automatic sorting.'),
        },
        'wxPG_BOLD_MODIFIED': {
            'desc': _('Modified values are shown in bold font.'),
        },
        'wxPG_SPLITTER_AUTO_CENTER': {
            'desc': _('When wxPropertyGrid is resized, splitter moves to the center.'),
        },
        'wxPG_TOOLTIPS': {
            'desc': _('Display tool tips for cell text that cannot be shown completely.'),
        },
        'wxPG_HIDE_MARGIN ': {
            'desc': _('Disables margin and hides all expand/collapse buttons that would appear outside the margin (for sub-properties).'),
        },
        'wxPG_STATIC_SPLITTER': {
            'desc': _('This style prevents user from moving the splitter.'),
        },
        'wxPG_STATIC_LAYOUT': {
            'desc': _('Combination of other styles that make it impossible for user to modify the layout.'),
        },
        'wxPG_LIMITED_EDITING': {
            'desc': _('Disables wxTextCtrl based editors for properties which can be edited in another way.'),
        },
        'wxPG_TOOLBAR': {
            'desc': _('wxPropertyGridManager only: Show tool bar for mode and page selection.'),
        },
        'wxPG_DESCRIPTION': {
            'desc': _('wxPropertyGridManager only: Show adjustable text box showing description or help text, if available, for currently selected property.'),
        },
        'wxPG_NO_INTERNAL_BORDER': {
            'desc': _('''wxPropertyGridManager only: don't show an internal border around the property grid.'''),
        },
    },
    'box_label': _('Style'),
    'style_list': ['wxPG_AUTO_SORT', 'wxPG_HIDE_CATEGORIES', 'wxPG_ALPHABETIC_MODE',
                   'wxPG_BOLD_MODIFIED', 'wxPG_SPLITTER_AUTO_CENTER', 'wxPG_TOOLTIPS',
                   'wxPG_HIDE_MARGIN', 'wxPG_STATIC_SPLITTER', 'wxPG_STATIC_LAYOUT',
                   'wxPG_LIMITED_EDITING', 'wxPG_TOOLBAR', 'wxPG_DESCRIPTION',
                   'wxPG_NO_INTERNAL_BORDER'],
}


