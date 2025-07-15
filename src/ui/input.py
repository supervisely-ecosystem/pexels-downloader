import requests

import supervisely as sly

from supervisely.app.widgets import Input, Container, Card, Text, Button, RadioGroup

import src.ui.keys as keys
import src.globals as g

query_message = Text(status="error", text="Please, enter the search query.")
query_message.hide()

entity_types = [RadioGroup.Item(mode) for mode in g.PEXELS_API_ENDPOINTS]
entity_type_selector = RadioGroup(entity_types)

search_query_input = Input(minlength=1, placeholder="Enter the search query")


search_button = Button("Check number of images")


search_results = Text(status="info")
search_results.hide()

# Main card for all input widgets.
card = Card(
    title="2️⃣ Search query",
    description="Please, enter the search query to find media files on Pexels.",
    content=Container(
        widgets=[
            entity_type_selector,
            search_query_input,
            query_message,
            search_button,
            search_results,
        ],
        direction="vertical",
    ),
    lock_message="Please, enter API key and check the connection to the Pexels API.",
)
card.lock()


@entity_type_selector.value_changed
def entity_type_changed(value: str):
    """Changes the application mode based on the selected entity type.

    :param value: The selected entity type, either "images" or "videos".
    :type value: str
    """
    sly.logger.debug(f"Entity type changed to: {value}.")
    g.app_mode = value

    from src.ui.output import destination_images, destination_videos
    from src.ui.settings import batch_size_input

    if g.app_mode == "images":
        destination_images.show()
        destination_videos.hide()
        search_button.text = "Check number of images"

        batch_size_input.value = g.IMAGE_BATCH_SIZE

    elif g.app_mode == "videos":
        destination_images.hide()
        destination_videos.show()
        search_button.text = "Check number of videos"

        batch_size_input.value = g.VIDEO_BATCH_SIZE


@search_button.click
def get_number_of_results():
    """Gets the number of images found by the search query."""
    query_message.hide()

    search_query = search_query_input.get_value()

    sly.logger.debug(
        f"Button was clicked. Search query: {search_query}, license: {license}."
    )

    if search_query:
        # Specifying request parameters and headers.
        headers = {"Authorization": keys.pexels_api_key}
        params = {"query": search_query}

        # Making a request to the Pexels API.
        response = requests.get(g.get_pexels_api_url(), headers=headers, params=params)
        try:
            # Getting the number of requests left fot the API key.
            rate_remaining = int(response.headers["X-Ratelimit-Remaining"])
            sly.logger.info(
                f"Pexels API announced that {rate_remaining} requests left."
            )
        except KeyError:
            sly.logger.error(f"Headers not found in the response: {response.headers}.")

        # Getting the number of images found by the search query.
        number_of_results = response.json().get("total_results")

        sly.logger.info(
            f"Pexels API returned {number_of_results} images for the search query: {search_query}."
        )
        if number_of_results == 8000:
            search_results.text = (
                "At least 8000 images were found. Pexels API "
                "limits the number of search results to 8000, but it may be more."
            )
        else:
            search_results.text = f"Number of images found: {number_of_results}."
        search_results.show()

    if not search_query:
        # Showing the error message if the search query is empty.
        query_message.show()
