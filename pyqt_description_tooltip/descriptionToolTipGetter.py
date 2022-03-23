
class DescriptionToolTipGetter:
    @staticmethod
    def getToolTip(title: str = '', shortcut: str = '', description: str = '',
                   shortcut_color: str = '#AAA', description_color: str = '#AAA'):
        tooltip_str = f'''
        <p>{title} <span style=\'color: {shortcut_color};\'>{shortcut}</span></p>
        '''
        if description:
            description_str = f'<p style=\'color: {description_color};\'>{description}</p>'
            tooltip_str += description_str
        return tooltip_str