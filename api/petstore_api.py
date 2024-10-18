from playwright.sync_api import APIRequestContext

class PetstoreAPI:
    def __init__(self, api_request_context: APIRequestContext):
        self.api = api_request_context

    def add_pet(self, pet_data):
        response = self.api.post("/v2/pet", data=pet_data)
        return response

    def get_pet(self, pet_id):
        response = self.api.get(f"/v2/pet/{pet_id}")
        return response

    def update_pet(self, pet_data):
        response = self.api.put("/v2/pet", data=pet_data)
        return response

    def delete_pet(self, pet_id):
        response = self.api.delete(f"/v2/pet/{pet_id}")
        return response
