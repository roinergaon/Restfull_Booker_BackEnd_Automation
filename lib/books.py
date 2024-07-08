from config import SESSION


class Books:

    def __init__(self):
        self.bookingIds = "/booking"

    def get_all_booking_ids(self, app_url, token):
        response = SESSION.get(f"{app_url}{self.bookingIds}")
        return response

