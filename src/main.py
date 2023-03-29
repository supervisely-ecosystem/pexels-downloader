import supervisely as sly

from supervisely.app.widgets import Container

import src.ui.keys as keys
import src.ui.input as input
import src.ui.settings as settings
import src.ui.output as output

layout = Container(widgets=[keys.card, input.card, settings.card, output.card])

app = sly.Application(layout=layout)
