from  NekosiaAPI import Nekosia

#print(Nekosia.get_image("catgirl"))
#print("="*20)
#print(Nekosia.get_image_with_count(tag="headphones",count=5))
#r = Nekosia.get_image_with_count("headphones",count=5)

#urls = [img["image"]["original"]["url"] for img in r["images"]]
#print(urls)


r = Nekosia.get_image_url("foxgirl")

print(r)
