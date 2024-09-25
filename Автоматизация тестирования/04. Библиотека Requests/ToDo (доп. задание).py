import requests


class ToDo:

    def __init__(self, url):
        self.url = url

    def add(self, title, completed=False):
        return str(requests.post(self.url, json={{"title": title,
                                                  "completed": completed
                                                  }}).json()["id"])

    def rename(self, id, title):
        return requests.patch(self.url + str(id), json={"title": title})

    def delete(self, id):
        return requests.delete(self.url + str(id))

    def list(self):
        return requests.get(self.url).json()

    def task(self, title):
        for i in self.list():
            if i["title"] == title:
                return i

    def comleted(self, id):
        return requests.patch(self.url + str(id), json={"completed": True})

    def uncompleted(self, id):
        return requests.patch(self.url + str(id), json={"completed": False})
