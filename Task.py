import unittest
import requests

class BookTests(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/books/"
        self.book_dict = {
    "title": "Ender’s Game",
    "author": "Orson Scott Card"
}

    def testCreateBook(self):
        response = requests.post(self.base_url, data=self.book_dict)
        self.assertEqual(response.status_code, 201)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        self.assertEqual(self.book_dict, resp_dict)
        requests.delete(self.base_url + "{}".format(self.book_dict["id"]))

    def testCreateBookNoAuthor(self):
        dict = {
            "title": "Ender’s Game",
            "author": ""
        }
        response = requests.post(self.base_url, data=dict)
        self.assertEqual(response.status_code, 400)

    def testCreateBookNoTitle(self):
        dict = {
            "title": "",
            "author": "Orson Scott Card"
        }
        response = requests.post(self.base_url, data=dict)
        self.assertEqual(response.status_code, 400)

    def testCreateBookNoData(self):
        dict = {
            "title": "",
            "author": ""
        }
        response = requests.post(self.base_url, data=dict)
        self.assertEqual(response.status_code, 400)

    def testCreateBookEmptyDict(self):
        dict = {}
        response = requests.post(self.base_url, data=dict)
        self.assertEqual(response.status_code, 400)

    def testCreateBookWrongURL(self):
        url = "http://pulse-rest-testing.herokuapp.com/boooks/"
        response = requests.post(url, data=self.book_dict)
        self.assertEqual(response.status_code, 404)


    def testReadBook(self):
        response = requests.post(self.base_url, data=self.book_dict)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        response = requests.get(self.base_url + str(resp_dict["id"]))
        self.assertEqual(response.status_code, 200)
        resp_dict = response.json()
        self.assertEqual(self.book_dict, resp_dict)
        requests.delete(self.base_url + "{}".format(self.book_dict["id"]))

    def testReadBookWrongID(self):

        response = requests.get(self.base_url + "99999")
        self.assertEqual(response.status_code, 404)

    def testReadBookWrongURL(self):
        url = "http://pulse-rest-testing.herokuapp.com/boooks/"
        response = requests.post(self.base_url, data=self.book_dict)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        response = requests.get(url + str(self.book_dict["id"]))
        self.assertEqual(response.status_code, 404)
        requests.delete(self.base_url + "{}".format(self.book_dict["id"]))

    def testUpdateBook(self):
        response = requests.post(self.base_url, data=self.book_dict)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        response = requests.put(self.base_url + str(self.book_dict["id"]), data={"title": "Speaker for the Dead"})
        self.book_dict["title"] = "Speaker for the Dead"
        self.assertEqual(response.status_code, 200)
        resp_dict = response.json()
        self.assertEqual(self.book_dict["title"], resp_dict["title"])
        requests.delete(self.base_url + "{}".format(self.book_dict["id"]))

    def testUpdateBookWrongURL(self):
        url = "http://pulse-rest-testing.herokuapp.com/boooks/"
        response = requests.post(self.base_url, data=self.book_dict)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        response = requests.put(url + str(self.book_dict["id"]), data={"title": "Speaker for the Dead"})
        self.assertEqual(response.status_code, 404)
        requests.delete(self.base_url + "{}".format(self.book_dict["id"]))

    def testUpdateBookWrongID(self):
        response = requests.post(self.base_url, data=self.book_dict)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        response = requests.put(self.base_url + "99999", data={"title": "Speaker for the Dead"})
        self.assertEqual(response.status_code, 404)
        requests.delete(self.base_url + "{}".format(self.book_dict["id"]))

    def testUpdateBookWrongData(self):
        response = requests.post(self.base_url, data=self.book_dict)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        response = requests.put(self.base_url + str(self.book_dict["id"]), data={"year": "1986"})
        self.assertEqual(response.status_code, 200)
        requests.delete(self.base_url + "{}".format(self.book_dict["id"]))

    def testUpdateBookEmptyDict(self):
        dict = {}
        response = requests.post(self.base_url, data=self.book_dict)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        response = requests.put(self.base_url + str(self.book_dict["id"]), data=dict)
        self.assertEqual(response.status_code, 200)
        requests.delete(self.base_url + "{}".format(self.book_dict["id"]))

    def testDeleteBook(self):
        response = requests.post(self.base_url, data=self.book_dict)
        resp_dict = response.json()
        self.book_dict["id"] = resp_dict["id"]
        response = requests.delete(self.base_url + str(self.book_dict["id"]))
        self.assertEqual(response.status_code, 204)
        response = requests.get(self.base_url)
        book_list = response.json()
        for book in book_list:
            self.assertNotEqual(book, self.book_dict)


class RoleTests(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/roles/"
        self.role_dict = {
    "name": "Roland Deschain",
    "type": "The Gunslinger",
    "level": 80,
    "book": 422
}

    def testCreateRole(self):
        response = requests.post(self.base_url, data=self.role_dict)
        self.assertEqual(response.status_code, 201)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        self.assertEqual(self.role_dict, resp_dict)
        requests.delete(self.base_url + "{}".format(self.role_dict["id"]))

    def testCreateRoleNoName(self):
        dict = {
    "name": "",
    "type": "The Gunslinger",
    "level": 80,
    "book": 422
}
        response = requests.post(self.base_url, data=dict)
        self.assertEqual(response.status_code, 400)

    def testCreateRoleNoType(self):
        dict = {
    "name": "Roland Deschain",
    "type": "",
    "level": 80,
    "book": 422
}
        response = requests.post(self.base_url, data=dict)
        self.assertEqual(response.status_code, 400)

    def testCreateRoleNoData(self):
        dict = {
    "name": "",
    "type": "",
    "level": "",
    "book": ""
}
        response = requests.post(self.base_url, data=dict)
        self.assertEqual(response.status_code, 400)

    def testCreateRoleEmptyDict(self):
        dict = {}
        response = requests.post(self.base_url, data=dict)
        self.assertEqual(response.status_code, 400)

    def testCreateRoleWrongURL(self):
        url = "http://pulse-rest-testing.herokuapp.com/roooles/"
        response = requests.post(url, data=self.role_dict)
        self.assertEqual(response.status_code, 404)


    def testReadRole(self):
        response = requests.post(self.base_url, data=self.role_dict)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        response = requests.get(self.base_url + str(resp_dict["id"]))
        self.assertEqual(response.status_code, 200)
        resp_dict = response.json()
        self.assertEqual(self.role_dict, resp_dict)
        requests.delete(self.base_url + "{}".format(self.role_dict["id"]))

    def testReadRoleWrongID(self):

        response = requests.get(self.base_url + "99999")
        self.assertEqual(response.status_code, 404)

    def testReadRoleWrongURL(self):
        url = "http://pulse-rest-testing.herokuapp.com/roooles/"
        response = requests.post(self.base_url, data=self.role_dict)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        response = requests.get(url + str(self.role_dict["id"]))
        self.assertEqual(response.status_code, 404)
        requests.delete(self.base_url + "{}".format(self.role_dict["id"]))

    def testUpdateRole(self):
        response = requests.post(self.base_url, data=self.role_dict)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        response = requests.put(self.base_url + str(self.role_dict["id"]), data={"level": 88})
        self.role_dict["level"] = 88
        self.assertEqual(response.status_code, 200)
        resp_dict = response.json()
        self.assertEqual(self.role_dict["level"], resp_dict["level"])
        requests.delete(self.base_url + "{}".format(self.role_dict["id"]))

    def testUpdateRoleWrongURL(self):
        url = "http://pulse-rest-testing.herokuapp.com/roooles/"
        response = requests.post(self.base_url, data=self.role_dict)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        response = requests.put(url + str(self.role_dict["id"]), data={"level": 88})
        self.assertEqual(response.status_code, 404)
        requests.delete(self.base_url + "{}".format(self.role_dict["id"]))

    def testUpdateRoleWrongID(self):
        response = requests.post(self.base_url, data=self.role_dict)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        response = requests.put(self.base_url + "99999", data={"level": 88})
        self.assertEqual(response.status_code, 404)
        requests.delete(self.base_url + "{}".format(self.role_dict["id"]))

    def testUpdateRoleWrongData(self):
        response = requests.post(self.base_url, data=self.role_dict)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        response = requests.put(self.base_url + str(self.role_dict["id"]), data={"year": "1986"})
        self.assertEqual(response.status_code, 200)
        requests.delete(self.base_url + "{}".format(self.role_dict["id"]))

    def testUpdateRoleEmptyDict(self):
        dict = {}
        response = requests.post(self.base_url, data=self.role_dict)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        response = requests.put(self.base_url + str(self.role_dict["id"]), data=dict)
        self.assertEqual(response.status_code, 200)
        requests.delete(self.base_url + "{}".format(self.role_dict["id"]))

    def testDeleteRole(self):
        response = requests.post(self.base_url, data=self.role_dict)
        resp_dict = response.json()
        self.role_dict["id"] = resp_dict["id"]
        response = requests.delete(self.base_url + str(self.role_dict["id"]))
        self.assertEqual(response.status_code, 204)
        response = requests.get(self.base_url)
        role_list = response.json()
        for role in role_list:
            self.assertNotEqual(role, self.role_dict)


if __name__ == "__main__":
    unittest.main()