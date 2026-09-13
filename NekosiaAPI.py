import requests

url = "https://api.nekosia.cat/api/v1/images/"
#url = "https://cdn.nekosia.cat/api/v1/images"
class Nekosia:  

    @staticmethod
    def get_image(tag):
        url_with_tag = url + tag
        r = requests.get(url_with_tag)
        return r.json()

    @staticmethod
    def get_image_url(tag):
        url_one_image = url + tag
        r = requests.get(url_one_image)
        data = r.json()
        if not data.get("success"):
            raise ValueError (data.get("message","API error"))
        return data.get("image",{}).get("original",{}).get("url")
    
    @staticmethod
    def get_list_of_tags():
        taglist = ["random", "catgirl", "foxgirl", "wolfgirl", "animal-ears", "tail", "tail-with-ribbon", "tail-from-under-skirt",
            "cute", "cuteness-is-justice"," blue-archive", "girl", "young-girl", "maid", "maid-uniform", 
                   "vtuber", "w-sitting", "lying-down", "hands-forming-a-heart", "wink", "valentine", "headphones",
            "thigh-high-socks", "knee-high-socks"," white-tights", 
                   "black-tights", "heterochromia", "uniform", "sailor-uniform", "hoodie", 
                   "ribbon", "white-hair", "blue-hair", "long-hair", 
                   "blonde", "blue-eyes", "purple-eyes"]

        return taglist

    @staticmethod
    def get_image_with_count(tag,count):
        count_url = url + tag + f"?count={count}"
        r = requests.get(count_url)
        return r.json()


