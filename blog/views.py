from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        'image': 'albert.png',
        'author': 'Manish',
        'date': date(2022, 2, 5),
        'title': 'Hike in the mountains',
        'excerpt': "There's nothing like the views you get when hiking the mountains.",
        'content': """ Adventures in the desert can be an exhilarating and unique experience that offers a stark contrast to the lush greenery of other terrains. The vast, arid landscapes of the desert can be both challenging and rewarding, from sandboarding down dunes to camel riding across the endless expanse. The tranquility of the desert at night can also be a memorable experience, camping under a clear, starry sky. However, it's important to be well-prepared for the extreme temperatures and limited resources of the desert, and to take necessary safety precautions before embarking on any adventure in this environment. The International Dark-Sky Association certified Death Valley National Park at its highest level, meaning visitors can enjoy a near-pristine sky while standing in the desert destination. Falconry in the Dubai Desert, UAE, is a perfect place to rest and relax after a day of desert adventures. The most popular desert trip involves an overnighter from the small sandy village of Merzouga, located about 400 miles east of Marrakech. Antarctica is the land of icebergs, penguins, and raw, arctic landscapes, and it’s one of the best destinations in the world if you seek adventure.
         
        There are plenty of ways to explore Arizona's Grand Canyon National Park, but perhaps the most coveted is a multiday rafting trip down the Colorado River. While shorter trips will take you from Diamond Creek to Lake Mead in two to five days, the ultimate white water adventure through the sandstone and this landscape is no small feat. Before you head into the park to discover glaciers and spot caribou, you’ll be required to talk with a ranger about your plans and watch a video on the backcountry. Horseback riding is also a great way to discover the diverse landscape as early explorers did. During the spring, summer, and fall months, you can find guided rides from Many Glacier, Lake McDonald, and Apgar. The desert offers a unique experience that can be both challenging and rewarding, but it's important to be well-prepared and take necessary safety precautions before embarking on any adventure in this environment.
        """
    },
    {
        "slug": "exploring-the-jungle",
        'image': 'manish.jpg',
        'author': 'Samantha',
        'date': date(2022, 3, 12),
        'title': 'Exploring the jungle',
        'excerpt': "Discover the secrets of the rainforest as you explore its lush landscapes.",
        'content': """ Exploring the jungle can be an enchanting experience, but it comes with danger and underlying risks. Hiking and trekking through rugged and dense forests might sound adventurous, but jungle life can be unpredictable. It's important to be well-prepared for a successful jungle adventure. To explore untouched and unparalleled jungle ecosystems is a unique privilege as a human being. Most have remained fundamentally unchanged since the dawn of time. However, it's important to be aware of the dangers of the jungle, including jungle animals and plants that could harm or kill you. If you're into mammals, everything from wild boars to jaguars and cougars can be found in the jungle. Therefore, it's important to take necessary safety precautions before embarking on any jungle adventure.
        When preparing for a jungle adventure, it's important to research the area you plan to explore. The definition of a jungle is a dense forest with tangled vegetation and a tropical climate. Therefore, it's important to be aware of the weather conditions and terrain of the jungle you plan to explore. It's also important to bring necessary equipment, such as insect repellent, a first aid kit, and a map or GPS device. Additionally, it's important to be aware of the local customs and laws of the area you plan to explore. This can help you avoid any cultural misunderstandings or legal issues.
        While exploring the jungle, it's important to take necessary safety precautions. This includes staying on marked trails, avoiding contact with wild animals, and being aware of poisonous plants. It's also important to stay hydrated and well-fed, as the jungle can be a physically demanding environment. It's important to respect the jungle ecosystem and leave no trace of your visit. Exploring the jungle can be a unique and unforgettable experience, but it's important to be well-prepared and take necessary safety precautions before embarking on any jungle adventure.
        """
    },
    {
        "slug": "adventures-in-the-desert",
        'image': 'albert.png',
        'author': 'John',
        'date': date(2022, 4, 20),
        'title': 'Adventures in the desert',
        'excerpt': "Experience the beauty and challenges of the world's driest landscapes.",
        'content': """ Adventures in the desert can be an exhilarating and unique experience. The vast, arid landscapes of the desert offer a stark contrast to the lush greenery of other terrains, and the harsh conditions can be both challenging and rewarding. From sandboarding down dunes to camel riding across the endless expanse, there are many activities to explore in the desert. Camping under a clear, starry sky and experiencing the tranquility of the desert at night can also be a memorable experience. However, it's important to be well-prepared for the extreme temperatures and limited resources of the desert, and to take necessary safety precautions before embarking on any adventure in this environment.
        When preparing for a desert adventure, it's important to research the area you plan to explore. The desert can be unforgiving if you're not properly prepared. Therefore, it's important to be aware of the weather conditions and terrain of the desert you plan to explore. It's also important to bring necessary equipment, such as sunscreen, a hat, and plenty of water. Additionally, it's important to be aware of the local customs and laws of the area you plan to explore. This can help you avoid any cultural misunderstandings or legal issues.
        While exploring the desert, it's important to take necessary safety precautions. This includes staying on marked trails, avoiding contact with wild animals, and being aware of poisonous plants. It's also important to stay hydrated and well-fed, as the desert can be a physically demanding environment. It's important to respect the desert ecosystem and leave no trace of your visit. Exploring the desert can be a unique and unforgettable experience, but it's important to be well-prepared and take necessary safety precautions before embarking on any desert adventure.
"""
    },
]

def get_date(post):
    return post.get('date')

# Create your views here.


def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date,reverse=True)
    latest_posts=sorted_posts[:3]
    return render(request, 'blog/home.html',{
        'posts':latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html',{
        'all_posts':all_posts
    })


def post_detail(request, slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request, 'blog/post-detail.html',{
        'post':identified_post
    })
