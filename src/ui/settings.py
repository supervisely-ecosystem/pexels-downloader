import os
from supervisely.app.widgets import (
    Checkbox,
    Container,
    Card,
    Text,
    RadioGroup,
    Field,
    InputNumber,
    Select,
)

import src.globals as g

# Image size selector.
image_sizes = [
    Select.Item(value=size, label=size.capitalize()) for size in g.IMAGE_SIZES
]
image_size_select = Select(items=image_sizes)

# Field for choosing image size.
image_size_field = Field(
    title="Image size",
    description="Choose the size of the image to download.",
    content=image_size_select,
)

# Field for choosing starting number for searching images.
start_number_input = InputNumber(value=0, min=0, precision=0)
start_number_field = Field(
    title="Starting image number to search",
    description="Offset for searching images (from which search result number to start).",
    content=start_number_input,
)

upload_method_radio = RadioGroup(
    items=[
        RadioGroup.Item(value=method, label=description)
        for method, description in g.DOWNLOAD_TYPES.items()
    ],
    direction="vertical",
)
upload_method_radio.set_value(value="files")

# Field for choosing the method of downloading images.
upload_method_field = Field(
    title="Choose the download method",
    description="Add only links is faster, but it may cause data loss if the source file will be deleted.",
    content=upload_method_radio,
)

# Info text about blocked checkboxes.
owner_info_note = Text(
    status="info",
    text="Information about the owner of the image will be added to the "
    "metadata because it is a requirement of the license.",
)

# Generate blocked checkboxes for required metadata fields.
disabled_chekboxes = {}
for field in g.REQUIRED_METADATA_FIELDS:
    disabled_chekboxes[field] = Checkbox(content=field, checked=True)
for checkbox in disabled_chekboxes.values():
    checkbox.disable()
disabled_chekboxes_container = Container(
    widgets=disabled_chekboxes.values(), direction="vertical"
)

# Generate checkboxes for optional metadata fields.
checkboxes = {}
for field in g.OPTIONAL_METADATA_FIELDS:
    checkboxes[field] = Checkbox(content=field)
for checkbox in checkboxes.values():
    checkbox.check()
checkboxes_container = Container(widgets=checkboxes.values(), direction="vertical")

# Field for choosing image metadata fields to add.
metadata_field = Field(
    title="Image metadata fields",
    description="Select metadata fields to add for downloaded images.",
    content=Container(
        widgets=[owner_info_note, disabled_chekboxes_container, checkboxes_container],
        direction="vertical",
    ),
)

# Field for choosing number of images to find.
images_number_input = InputNumber(value=1, min=1, precision=0)
images_number_field = Field(
    title="Number of images",
    description="How many images to find on Pexels.",
    content=images_number_input,
)

# Inputs for changing default settings.
batch_size_input = InputNumber(value=500, min=1, precision=0)
max_workers_input = InputNumber(value=os.cpu_count(), min=1, precision=0)
batch_size_input.disable()
max_workers_input.disable()

# Checkbox for unlocking default settings inputs.
default_settings_checkbox = Checkbox(content="Use default settings", checked=True)

# Text tooltips for default settings inputs.
batch_size_text = Text("Batch size for uploading images:")
max_workers_text = Text(
    "Maximum number of workers for uploading image files in parallel:"
)

# Field for choosing upload settings.
upload_settings_field = Field(
    title="Upload settings",
    description="Use the default settings or change them to your needs.",
    content=Container(
        widgets=[
            default_settings_checkbox,
            batch_size_text,
            batch_size_input,
            max_workers_text,
            max_workers_input,
        ],
        direction="vertical",
    ),
)

# Main card for all settings widgets.
card = Card(
    content=Container(
        widgets=[
            image_size_field,
            images_number_field,
            start_number_field,
            metadata_field,
            upload_method_field,
            upload_settings_field,
        ],
        direction="vertical",
    ),
    title="3️⃣ Search settings",
    description="Additional settings for searching and downloading images.",
    lock_message="Please, enter API key and check the connection to the Pexels API.",
)
card.lock()


@default_settings_checkbox.value_changed
def unlock_settings(checked):
    if checked:
        batch_size_input.value = 500
        max_workers_input.value = os.cpu_count()
        batch_size_input.disable()
        max_workers_input.disable()
    else:
        batch_size_input.enable()
        max_workers_input.enable()
