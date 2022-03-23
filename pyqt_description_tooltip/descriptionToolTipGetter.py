
class DescriptionToolTipGetter:
    @staticmethod
    def getToolTip(title: str = '', shortcut: str = '', description: str = '',
                   shortcut_color: str = '#AAA', description_color: str = '#AAA'):
        tooltip_str = f'''
        <p>{title} <span style=\'color: {shortcut_color};\'>{shortcut}</span></p>
        <p style=\'color: {description_color};\'>{description}</p>
        '''
        return tooltip_str